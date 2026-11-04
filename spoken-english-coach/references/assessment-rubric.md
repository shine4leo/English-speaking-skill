# Assessment Rubric

Use assessment as coaching evidence, not as a clinical diagnosis or official CEFR certification.

## Evidence ladder

Unknown capability always falls back to `E0`.

| Level | Evidence | Allowed action |
|---|---|---|
| E0 | Text/ASR transcript only; no original audio available to the model | Evaluate meaning, grammar, and wording only. Do not compare how attempts “sounded” |
| E1 | Clear original audio available, no calibrated scorer | Give non-calibrated coach observations about this sample's intelligibility and obvious repeated stress/rhythm/sound features |
| E2 | Original audio plus ASR or forced alignment | Use ASR/alignment to locate possible trouble or completeness, not as proof of pronunciation accuracy |
| E3 | Original audio plus a validated/calibrated acoustic pronunciation scorer and repeat samples | Report a likely scored feature with the tool's stated limits; it is still training evidence, not ground truth |

Use `high` coach confidence only when a clear feature repeats in clean audio or is supported by calibrated evidence. Use `medium` for one plausible direct-audio observation. Text-only, ASR substitutions, noisy/clipped audio, and stereotypes never support a pronunciation diagnosis.

ASR answers “what text was recognized,” not “which phoneme was produced correctly.” Alignment answers “where speech likely occurred,” not “whether it was pronounced well.” Never convert either signal into a precise pronunciation judgment by itself. Do not invent WPM, pitch, hertz, pause duration, phoneme boundaries, or tool scores; quote numbers only when an actual tool returned them.

## Pronunciation and delivery bands

Rate only dimensions supported by audio. Use 0–4 bands rather than a fake 0–100 score.

| Dimension | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| Intelligibility | meaning often blocked | understandable with repeated effort | generally clear with occasional repair | consistently clear and easy to follow |
| Sounds | repeated contrasts obscure words | several sound substitutions but message survives | isolated sound issues | controlled contrasts in this sample |
| Word stress | stress often hides intended words | several misplaced or flat stresses | mostly clear stress | stress consistently supports recognition |
| Rhythm and linking | word-by-word delivery blocks phrasing | uneven chunks or unnatural pauses | mostly useful thought groups | flexible, natural grouping for this level |
| Fluency and control | frequent breakdowns | many pauses/restarts | workable flow with some hesitation | sustained, controlled delivery for this task |

Use `0 / not assessed` when evidence is unavailable. A band describes this sample and is not a calibrated acoustic measurement, the learner's identity, or a permanent level. Compare trends only across sufficiently similar tasks and evidence conditions.

## Feedback record

For every coached pronunciation item, capture:

- target word or chunk;
- observed feature, without caricaturing what the learner said;
- confidence: high or medium;
- expected stress or IPA only when it helps;
- one plain mouth/tongue/airflow cue;
- one minimal pair or contrast when appropriate;
- first attempt versus retry result;
- one transfer sentence.

Limit active pronunciation feedback to three items per reading and one item per normal conversation turn.

## Diagnostic loop

Use `hear → isolate → contrast → model → retry → transfer`:

1. Quote the target chunk, not a whole paragraph.
2. Test the suspected feature with a minimal pair or a second word in a similar context.
3. Give one physical cue and one auditory model.
4. Ask for two controlled repetitions, then the original sentence.
5. If the contrast still cannot be heard reliably, log it as `needs future check`, not as failure.

Possible Mandarin-L1 transfer areas include final consonants, consonant clusters, vowel length/quality, `/r/–/l/`, `/v/–/w/`, dental fricatives, plural/past endings, lexical stress, reduced vowels, and thought-group rhythm. These are diagnostic candidates only. Never assume them without evidence.

## Wording and grammar triage

Classify non-pronunciation feedback:

- **Blocking:** changes the intended meaning or prevents the listener from acting. Correct now.
- **Unnatural or Chinese-influenced:** understandable but unlikely in the situation. Recast at a natural breakpoint and require one retry.
- **Upgrade:** already correct; offer a more precise or idiomatic option only when it serves the session target.

Record the learner's original wording, one natural repair, the reason in plain Chinese, and a new transfer example. Do not label every literal translation as “Chinglish”; explain the specific collocation, register, information order, or grammar pattern.

## Listening comprehension

Divide each passage into 3–5 meaning units before delivery. Mark each unit:

- `2 captured`: central meaning and relationship are correct;
- `1 partial`: some correct content but an important detail or relation is missing;
- `0 missed`: absent or meaning reversed.

Report `captured units / total units` plus the missed language. Do not grade the elegance of the Chinese translation.

## Level estimates

CEFR estimates are provisional coaching ranges based on repeated samples. Keep them `unassessed` during the first session. After at least three sessions covering spontaneous speaking, listening, and interaction, use `emerging A2`, `solid B1`, or `B1–B2` when evidence is mixed. Track listening, spoken interaction, and spoken production separately; store phonology as sample observations rather than averaging a standalone “phonology CEFR”. Never call any estimate a certified score.
