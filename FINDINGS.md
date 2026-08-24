# Findings ledger

What the corpus has caught, newest first. Each entry names the shape, not
the corpus content: fixes in the scanner reproduce the shape in a NEW
fixture there (the contamination rule).

## 2026-08-24 — Tier R begins, and finds one on the first run (airom @ 9adac6a)

The first real-world entry is `r-flask`: pallets/flask, BSD-3-Clause, 83
Python files, no AI anywhere. It found a false positive that the synthetic
pure negative could not.

8. **A bare `redis` dependency was claimed as a vector database**, at 0.95
   confidence, from Flask's own celery example. redis is dual-use: the pip
   package is a cache/broker client, and a vector store only with Redis
   Stack's vector API. The manifest catalog entry asserted the vector reading
   with nothing behind it. Fixed by following the pattern already used for
   elasticsearch and mongodb — both absent from the catalog, both claimed by
   usage rules — so genuine `VectorField`/`FT.CREATE` usage still reports
   redis, now at 0.985.

That is the argument for Tier R in one finding. A hand-written negative only
proves the scanner ignores what its author thought to leave out.

Also fixed: the evaluator refused every GitHub tarball, because
`pax_global_header` (the entry git writes carrying the commit SHA) hit an
"unsupported entry type" guard meant for symlinks and specials. Tier R could
not load at all until it was skipped. Found by using the instrument on real
data for the first time.

Corpus after: precision 100.0%, recall 100.0% across 14 entries, 266 files.

## 2026-08-23 — after the fixes (airom @ 813a721)

Precision 100.0%, recall 100.0% (31 labeled), zero traps, zero wrong
versions/providers/locations, calibration 16/16 high and 14/14 medium. All
five findings below fixed in the scanner; fixing them surfaced TWO more,
both identity splits, also fixed:

6. **Go AST sightings carried no provider**, so the same module arrived as
   two identical components (CanonicalKey includes the provider). The AST
   table now mirrors the go.mod catalog.
7. **Semantic Kernel never folded**: the NuGet catalog said
   "Microsoft.SemanticKernel", the rule pack "semantic-kernel". Display
   names fold; declared identities live in the purl.

Three labels moved in the same pass, each with reasoning committed in its
truth file: the npm/NuGet canonical-name folds, sentence-transformers
framework -> library (the catalog draws the orchestrates-vs-wraps line
deliberately), and a Go version missing its canonical v prefix — exposed
only when the fold delivered the version to the matched component.

A saturated Tier S means the KNOWN shapes are handled. It does not mean the
scanner is done; Tier R exists to break it again.

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
