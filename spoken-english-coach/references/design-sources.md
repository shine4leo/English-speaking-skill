# Design Sources and Decisions

Research checked on 2026-11-04. These repositories informed the workflow; no source code or course content was copied. Repository activity and license labels can change, so verify upstream before reusing code.

## Closest reusable patterns

| Project | Observed license / status | Useful mechanism | Decision in this Skill |
|---|---|---|---|
| [CamiloCortesM/ai-language-tutor](https://github.com/CamiloCortesM/ai-language-tutor) | MIT; young project | Workspace as a language classroom; read profile/errors before class, write progress after; finite lesson pass/report | Use a controller Skill, mode references, persistent learner files, explicit session states, and mandatory write-back |
| [jovidalao/Converloop](https://github.com/jovidalao/Converloop) | AGPL-3.0; preview | Separate mistake, successful use, expression gap, and listening evidence; review by evidence | Keep different evidence types and require use in a new context before calling an item mastered |
| [cyresearch/open-language-teacher](https://github.com/cyresearch/open-language-teacher) | MIT; active development | Phone-accessible voice practice, Markdown configuration, lesson notes, later review | Use plain Markdown profile, queue, daily logs, and weekly summaries rather than an opaque database |
| [ArtCC/freelingo](https://github.com/ArtCC/freelingo) | AGPL-3.0; substantial platform | CEFR-aligned course boundaries, persistent progress, spaced review, voice tied to current lessons | Constrain content by working level and current targets; keep the Skill lighter than a full platform |
| [janosdios/langteacher](https://github.com/janosdios/langteacher) | verify upstream before code reuse | CEFR-aware tutor, brief native-language rescue, one correction per turn | Keep English dominant, allow short Chinese rescue, and cap default corrections |

## Interaction and activity patterns

| Project | Observed license / status | Useful mechanism | Decision in this Skill |
|---|---|---|---|
| [miraculix95/lingua-app](https://github.com/miraculix95/lingua-app) | MIT | Graded listening speeds, many scenes/registers, shared vocabulary across activities | Use slow/natural/fast delivery and recycle the same chunks through listening and conversation |
| [noworneverev/speak-quest](https://github.com/noworneverev/speak-quest) | README says MIT, but no separate license file was visible at review time | Role, learner goal, complication, and automatic success condition | Give every role-play a communicative goal, friction, success condition, and finish point; do not copy assets/code |
| [spark798/iamspeaker](https://github.com/spark798/iamspeaker) | MIT | Measure → prescribe → retry → compare; pace/filler/pronunciation trends | Require a targeted retry and record change over time; never invent acoustic metrics without tools |
| [hujiulin/EchoWise](https://github.com/hujiulin/EchoWise) | MIT | Communication before perfection; nonintrusive hints; persistent conversation history | Respond to meaning first and move detailed correction to checkpoints |
| [michael-borck/talk-buddy](https://github.com/michael-borck/talk-buddy) | verify upstream before code reuse | Real-world interview/meeting scenarios, spoken exchange, reviewable transcript | Provide interview and practical scenario labs and save learning highlights |

## Pronunciation references and limits

| Project / source | What it establishes | Rule adopted here |
|---|---|---|
| [OpenAI Whisper](https://github.com/openai/whisper) and its [model card](https://github.com/openai/whisper/blob/main/model-card.md) | Whisper is an ASR/translation model; it can hallucinate and performance varies across accents and groups | A transcript or word confidence is not a pronunciation score |
| [YuanGongND/gopt](https://github.com/YuanGongND/gopt) | Multi-level pronunciation scoring can correlate with human ratings in controlled read speech, but is not ground truth | Use calibrated acoustic scoring only as one training signal |
| [SpeechOcean762](https://github.com/jimbozhang/speechocean762) | A Mandarin-L1 English corpus with expert phone/word/utterance ratings supports controlled research | Mandarin transfer patterns are hypotheses to test, never assumptions |
| [Montreal Forced Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) and [WhisperX](https://github.com/m-bain/whisperX) | Alignment locates words/phones in time | Alignment failure does not prove mispronunciation |
| [Halleck45/OpenPronounce](https://github.com/Halleck45/OpenPronounce) | Open phoneme-level experimentation and transparent benchmarking | Treat automated word/phone flags as experimental and verify by repeat audio |
| [marujofln/pronunciation-coach](https://github.com/marujofln/pronunciation-coach) | Useful phrase categories, minimal pairs, and attempt history; its G2P comparison begins from ASR text | Borrow the drill loop, not the claim that recognized text reveals exact produced phones |
| [Automatic Pronunciation Assessment review](https://aclanthology.org/2023.findings-emnlp.557/) | ASR and mispronunciation detection have different goals; pronunciation assessment has model/data limits | Prefer intelligibility, evidence levels, and repeated confirmation over precise-looking scores |

## Curriculum and source policy

- [TED newest talks](https://www.ted.com/talks) is a dynamic page, not a stable API. The Skill records retrieval time and chooses the newest suitable unpracticed item it can verify.
- [TED Talks Usage Policy](https://www.ted.com/about/our-organization/our-policies-terms/ted-talks-usage-policy) limits transcript reuse, alteration, scraping, and programmatic curriculum use. The Skill links to the official page, does not package transcripts/audio, and stores only metadata and learner-created notes.
- The [CEFR Companion Volume](https://rm.coe.int/cefr-companion-volume-with-new-descriptors-2020/16809ea0d4) supports separate attention to interaction, production, listening, and phonological control. The Skill uses provisional multi-skill ranges, not a certified global score.
- [Free Spaced Repetition Scheduler](https://github.com/open-spaced-repetition/free-spaced-repetition-scheduler) shows how mature FSRS scheduling can be implemented. A transparent fixed review ladder is used here because the Skill stores plain Markdown and does not pretend to run a calibrated optimizer.

## OpenAI product fit

- [Skills](https://developers.openai.com/plugins/concepts/skills) are instruction-and-resource folders for repeatable workflows, which matches this project's controller plus references and templates.
- [ChatGPT Voice](https://learn.chatgpt.com/docs/features/voice) can be used with Codex on supported clients and iOS configurations, but availability depends on rollout, plan, host, and workspace.
- [Codex on mobile](https://learn.chatgpt.com/docs/mobile) operates through Cloud or a connected computer/project. The learning journal therefore lives in the selected workspace rather than only on the phone.

## Deliberate exclusions

- No copied transcripts, copyrighted course units, cloned voices, avatars, gamification, or third-party API keys.
- No claim that a prompt alone supplies microphone access, hidden listening text, acoustic measurements, exact WPM, phoneme boundaries, or background reminders.
- No 1–100 “native-like” score. The Skill uses evidence-backed bands and personal trend notes.
