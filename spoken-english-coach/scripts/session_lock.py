#!/usr/bin/env python3
"""Atomically allow only one writer for an English speaking journal."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys


LOCK_NAME = ".spoken-english-session.lock"
OWNER_NAME = "owner.json"


def lock_paths(journal_root: Path) -> tuple[Path, Path]:
    lock_dir = journal_root / LOCK_NAME
    return lock_dir, lock_dir / OWNER_NAME


def read_owner(owner_path: Path) -> dict[str, str]:
    try:
        data = json.loads(owner_path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {"session_id": "unknown"}
    return {"session_id": str(data.get("session_id", "unknown"))}


def acquire(journal_root: Path, session_id: str) -> int:
    journal_root.mkdir(parents=True, exist_ok=True)
    lock_dir, owner_path = lock_paths(journal_root)
    try:
        os.mkdir(lock_dir)
    except FileExistsError:
        owner = read_owner(owner_path)
        print(json.dumps({"acquired": False, "owner": owner["session_id"]}))
        return 2

    try:
        owner_path.write_text(
            json.dumps({"session_id": session_id}, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    except OSError:
        try:
            os.rmdir(lock_dir)
        except OSError:
            pass
        raise

    print(json.dumps({"acquired": True, "owner": session_id}))
    return 0


def release(journal_root: Path, session_id: str) -> int:
    lock_dir, owner_path = lock_paths(journal_root)
    if not lock_dir.exists():
        print(json.dumps({"released": False, "reason": "not_locked"}))
        return 0

    owner = read_owner(owner_path)["session_id"]
    if owner != session_id:
        print(json.dumps({"released": False, "reason": "owner_mismatch", "owner": owner}))
        return 3

    try:
        owner_path.unlink(missing_ok=True)
        os.rmdir(lock_dir)
    except OSError as exc:
        print(json.dumps({"released": False, "reason": str(exc)}))
        return 4


    print(json.dumps({"released": True, "owner": session_id}))
    return 0


def status(journal_root: Path) -> int:
    lock_dir, owner_path = lock_paths(journal_root)
    if not lock_dir.exists():
        print(json.dumps({"locked": False}))
        return 0
    owner = read_owner(owner_path)["session_id"]
    print(json.dumps({"locked": True, "owner": owner}))
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("acquire", "release", "status"))
    parser.add_argument("--journal-root", required=True, type=Path)
    parser.add_argument("--session-id")
    args = parser.parse_args()
    if args.action in {"acquire", "release"} and not args.session_id:
        parser.error("--session-id is required for acquire and release")
    return args


def main() -> int:
    args = parse_args()
    if args.action == "acquire":
        return acquire(args.journal_root, args.session_id)
    if args.action == "release":
        return release(args.journal_root, args.session_id)
    return status(args.journal_root)


if __name__ == "__main__":
    sys.exit(main())
