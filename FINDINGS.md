# Findings ledger

What the corpus has caught, newest first. Each entry names the shape, not
the corpus content: fixes in the scanner reproduce the shape in a NEW
fixture there (the contamination rule).

## 2026-08-23 — first Tier S run (airom v0.4.1-dev, rules v0.1.6)

Precision 66.7% (33 reported), recall 71.0% (31 labeled), 0 traps, 0 wrong
versions. The fixture suite implied far better; that gap is why this corpus
exists. The real findings:

1. **Builder-pattern model literals are invisible.** `modelName("gpt-4o-mini")`
   (Java), `.model("gpt-4o-mini")` (Rust), `ModelId("gpt-4o-mini")` (Kotlin)
   all missed; only `model=`/`model:` anchored forms fire. Three languages'
   dominant SDK style, three FNs.
2. **The Gradle detector reported nothing at all** for a plain
   `build.gradle.kts` with one `implementation("group:artifact:version")`
   line. Kotlin recall is 0 twice over: manifest and literal.
3. **GGUF `general.name` is ignored for naming**, and weights files keep
   their serialization extension: `bench-tiny-llama.gguf` reported where the
   header itself declares `bench-tiny-llama`. The header was parsed; the
   name in it was not used.
4. **npm scoped packages fold to the provider name**: `@anthropic-ai/sdk`
   reports as `anthropic` while `openai` stays `openai`. Whichever policy is
   right, it is currently inconsistent, and the labels spell what the
   manifest declares.
5. **Bound generation params emit as standalone `ai-config` components.**
   `temperature`/`max_tokens` in the same call that names the model became
   four separate components across three languages. §9.5 defines ai-config
   as UNBOUND params; these are bound, and belong on the model's facet.

What held: every trap stayed silent (docstrings, READMEs, comments), all 17
graded versions correct including the range-means-absent assertions, all 22
locations valid, the pure negative reported nothing, and the test-scoped
mock literal matched only under its scope.

Two labels were corrected after this run, with reasoning in the truth files:
`langchain4j-open-ai` library -> framework (integration module of the
framework), and a missing `rag-pipeline` label the scanner found and the
labeler had missed. The instrument corrected its operator twice on day one.
