# r-openai-python — analysis, not yet labeled

**Why it is worth having.** This is the OpenAI SDK's own repository, and it
contains roughly **2,323 model-name occurrences under `src/`** that are
*not usage*: `Literal["gpt-4o-transcribe", "gpt-4o-mini-transcribe", ...]`
type unions describing what the API accepts. A scanner that reports those is
claiming a library's type stubs are deployed AI. It is the transformers
docstring lesson at ten times the scale, in a repository nobody would call
adversarial.

**What reading establishes so far.**

| Location | Shape | Correct answer |
|---|---|---|
| `pyproject.toml` | httpx2, pydantic, typing-extensions, anyio, sniffio, jiter | no AI dependency; none of these are AI packages |
| `src/openai/types/` (74 files) | `Literal[...]` unions of model IDs | **not components** — API specification |
| `src/openai/resources/` (13 files) | model names in signatures and docstrings | **not components**, same reason |
| `examples/` (43 files) | real call sites, `model="gpt-4o-2024-08-06"` etc. | genuine usage |
| `tests/` (267 hits) | model literals in test code | genuine, but test-scoped |

Distinct models observed at `model="..."` call sites in `examples/`:
gpt-4o-2024-08-06 (12), gpt-5.5 (6), whisper-1 (3), tts-1 (2), gpt-realtime
(2), gpt-3.5-turbo-instruct (2), sora-2, openai.gpt-5.4, gpt-image-1,
gpt-5.6-sol, gpt-5.2, gpt-5, gpt-4, plus two placeholders that are not model
names at all: `deployment-name` and `<ignored>`.

**What is left before it can be labeled.**

1. Enumerate `tests/` the same way (267 occurrences), and decide the scope
   marker for each.
2. Decide whether models reached through a variable rather than a literal
   (`model=MODEL`) exist here, and how they are labeled.
3. Decide the `library` question: `examples/` genuinely imports and calls the
   SDK, so `openai` as a library component is probably correct even though
   this repo *is* openai. Worth writing down rather than assuming.
4. The two placeholders above become `forbidden` entries: they sit in a
   `model=` position and are not models.

**Why it is not in `corpus/` yet.** Every unlabeled real component scores as
a false positive. Landing this half-done would report a precision number that
says more about the labeler than the scanner, which is the one failure this
whole corpus exists to prevent.
