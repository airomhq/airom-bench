# airom-bench

The benchmark corpus for [AIROM](https://github.com/airomhq/airom), the
open-source AIBOM scanner. Methodology and metric definitions live in the
scanner repo: [docs/benchmark.md](https://github.com/airomhq/airom/blob/main/docs/benchmark.md).
This repo holds the data; the evaluator is `airom bench`.

```bash
pip install airom
airom bench . --json bench.json
```

## Layout

| Path | What |
|---|---|
| `corpus/<name>/tree/` or `snapshot.tar.gz` | the scannable content |
| `corpus/<name>/truth.yaml` | hand-written ground truth |
| `corpus/<name>/MANIFEST.yaml` | tier, provenance, license, labeler |
| `baselines/<version>.json` | per-release results, the gate input |
| `schema/truth-schema.json` | the truth.yaml contract |

## Tiers

**Tier S (synthetic, `s-*`)** is constructed: labels are correct by
construction, and the tier measures coverage across languages and component
kinds, plus adversarial shapes. **Tier R (real, `r-*`)** is pinned snapshots
of public repositories, hand-labeled; it is the only tier quoted anywhere.

## The rules that make the numbers mean something

- **Held out.** Nothing here may be copied from the scanner's fixtures, and
  nothing here may be copied into them. A benchmark failure is fixed in the
  scanner with a NEW handcrafted fixture reproducing the shape, never with
  this content.
- **Labels are read from the tree, not from any scanner's output.** When a
  scanner disagrees with a label, the label wins until a human shows the
  label wrong; label fixes are commits with the reasoning in the message.
- **Labels are the ontology's truth, not the tool's.** If a tree contains an
  AI library the scanner misses, the label stays and the recall number drops.
  That is the product working.

## Licensing

The scaffolding and every Tier S tree are Apache-2.0, written for this
corpus. Tier R entries redistribute permissively-licensed snapshots only;
each entry's MANIFEST records the upstream license.
