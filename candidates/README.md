# Candidates

Repositories staged for Tier R but **not yet labeled**, and therefore not
scanned: `airom bench` walks `corpus/` only, so nothing here can reach a
number.

A candidate graduates when its `truth.yaml` is complete. Partial labels are
worse than none: an unlabeled real component is scored as a false positive,
so a half-labeled entry does not understate the scanner, it actively
misreports it.

Each candidate keeps its snapshot, provenance, and the analysis done so far,
so the next person starts from the reading rather than from scratch.
