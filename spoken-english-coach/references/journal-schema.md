# Journal Schema

## Location and templates

Use this workspace-relative structure:

```text
english-speaking-journal/
├── learner-profile.md
├── progress.md
├── review-queue.md
└── sessions/
    └── YYYY/
        └── MM/
            └── YYYY-MM-DD-HHMMSS.md
```

Resolve templates relative to this reference file:

- [learner-profile-template.md](../assets/learner-profile-template.md) → `english-speaking-journal/learner-profile.md`
- [progress-template.md](../assets/progress-template.md) → `english-speaking-journal/progress.md`
- [review-queue-template.md](../assets/review-queue-template.md) → `english-speaking-journal/review-queue.md`
- [session-log-template.md](../assets/session-log-template.md) → one new file under `sessions/YYYY/MM/`

Only create this structure after the learner explicitly starts/continues a persistent session or an existing profile has auto-log enabled. `不要保存` forbids every write for that session.

## Session identity and collision safety

Use the learner's local start time for `session_id` and the filename: `YYYY-MM-DD-HHMMSS`. Before creating it, check that the path does not exist. If it exists, append `-02`, `-03`, and so on. Never overwrite or append a second session to an existing report.

Only one task may mutate a journal at a time. Before reserving a report, acquire the atomic session lock with `scripts/session_lock.py`, resolved relative to `SKILL.md`. If another session owns the lock, do not create or update reports, queue, or progress; offer to resume that session or continue the new practice without saving. Release the lock only after verified final writes or after honoring “不要保存”.

If the helper cannot run in the current environment, do not risk concurrent shared-file mutation. Continue without persistence and return the completed report as unsaved Markdown.

If the most recent report has `status: in_progress` or `status: interrupted` and the learner says “继续上次”, resume that report under the same lock instead of allocating a new ID. Re-read `review-queue.md` and `progress.md` immediately before their final update and de-duplicate by `session_id`. Use item IDs derived from the source session, such as `V-YYYYMMDDHHMMSS-01`, rather than a shared counter.

## Write protocol

1. Confirm a persistent writable workspace, acquire the session lock, and allocate a collision-free session file.
2. Create it from the session template with `status: in_progress` and real metadata; leave no `YYYY` or other scaffold tokens.
3. At a module checkpoint, update the same report rather than appending another copy.
4. After spoken practice ends, complete the detailed report, set `status: completed`, and update its finish time.
5. Re-read, merge, and update `review-queue.md`, then add one `session_id` row to `progress.md`.
6. Reopen all changed files and verify the session ID, status, topic, corrections, and next retrieval prompt.
7. Release the session lock, then claim success.

If the workspace is unavailable or not writable, do not create a temporary journal and call it saved. Return a complete ready-to-save Markdown report with `storage_scope: unsaved_chat_output`.

## Session frontmatter

Every report starts with:

```yaml
---
session_id: YYYY-MM-DD-HHMMSS
status: in_progress | completed | interrupted
started_at: ISO-8601 with timezone
finished_at:
mode:
theme:
scenario:
instructional_starting_point: unassessed | A1 | A2 | B1 | B2 | C1 | C2
interaction_channel: live_voice | uploaded_audio | dictation | text
audio_evidence: direct_audio | asr_only | none
listening_integrity: audio_only | captions_possible | text_visible | not_assessed
storage_scope: persistent_workspace
source_type: ted_official_link | learner_provided | original_coach_material | none
source_url:
---
```

`instructional_starting_point` controls task difficulty; it is not a certified CEFR estimate. During the first session use `unassessed` unless the learner self-reports a level, and label a self-report as such in the body.

## Session body

Include observed, useful content; use `not assessed` or omit optional tables rather than inventing entries.

```markdown
# English Speaking Session — [session_id]

## Snapshot
- Estimated practice minutes:
- Estimated learner generative-speaking minutes:
- Goal and success condition:
- Scenario redo completed: yes | no
- Next session's first retrieval prompt:

## Source (optional)
- Title / speaker:
- Published / retrieved at:
- Official URL:
- Practice selection: official page used by learner | one learner-provided sentence | original material | none

## Target language
| Item | Meaning / register | Supported use | Prompted-unaided use | Spontaneous / transfer use | Next review |

## Conversation highlights
| Context | Learner wording | Natural repair / stronger option | Type and reason | Retry result |

## Pronunciation and delivery (direct audio only)
| Target | Observation about this sample | Evidence level / confidence | Cue / drill | Retry result |

## Listening (when practiced)
- Delivery level and integrity:
- Idea units captured:
- Missed language:
- English retell result:

## Grammar focus
- Pattern:
- Controlled repair:
- Free-use attempt:

## Retrieval evidence
| Item | Prompted-unaided | Spontaneous | After hint | Failed | Evidence note |

## Session review
- One win:
- One priority:
- Learner reflection:
- Next session plan:
```

When audio evidence is `asr_only` or `none`, omit the pronunciation table or write one line: `Not assessed — the coach did not receive direct audio.` Never reconstruct an exact spoken form from a voice transcript.

Conversation highlights preserve selected learning turns, not a fabricated verbatim transcript. A raw transcript is optional only when it actually exists and the learner requests it; label voice transcripts as potentially non-verbatim.

For a lesson without an external source, set `source_type: original_coach_material` or `none`. Never invent a title or URL to fill the section.

## Learner profile

Keep stable preferences and evidence-backed patterns only. Do not promote a one-off mistake into the profile. Add a recurring issue after it appears in at least two sessions or a controlled diagnostic confirms it. Include:

- persistence opt-in and quick-question logging preference;
- goals and priority situations;
- instructional starting difficulty and, after three or more varied sessions, separate provisional listening/interaction/production ranges;
- preferred accent/reference voice;
- preferred session length and correction style;
- interests and avoided topics;
- recurring direct-audio pronunciation/delivery observations with confidence;
- recurring grammar, collocation, and Chinese-transfer patterns;
- mastered strengths and current focus.

## Review queue

Use one row per active item:

```markdown
| ID | Item | Type | Source session | Last result | Stage | Next due (timestamp) | Example / note |
```

Use distinct stable prefixes: `V-` phrase/chunk, `G-` grammar, `PR-` pronunciation, `L-` listening, and `I-` interaction. Derive the remainder from the source `session_id` plus a local ordinal to prevent concurrent allocation collisions. Add `PR-` items only from medium/high-confidence direct-audio observations.

## Progress index

Add one row per `session_id`:

```markdown
| Started | Session ID | Mode | Theme / scenario | Starting point | Generative speaking | Main priority | Log |
```

Link `Log` to the relative session file. Use this index to inspect theme/source history that is actually recorded. Follow the table with seven-session reviews; do not duplicate the full reports.
