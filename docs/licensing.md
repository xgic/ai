# Licensing — Apache 2.0

## Policy

**All XGIC public solutions** (source repositories, documentation hubs, published packages, and related public artifacts under `github.com/xgic`) use the **Apache License, Version 2.0**, unless a specific public repository documents a deliberate exception (rare; requires an ADR).

This repository (`xgic/ai`) is licensed under Apache 2.0. See [LICENSE](../LICENSE) and [NOTICE](../NOTICE).

## Copyright holder (canonical)

Use this form in LICENSE appendices, NOTICE files, and README license sections:

```text
Copyright 2026 XGIC
```

**Do not** put personal names or email addresses in the copyright holder line. Personal reputation and credit belong in git authors, GitHub profiles, and optional README maintainer notes—not as co-owners in the copyright line.

Optional multi-year form when intentionally maintained across years: `Copyright 2026–2027 XGIC` (update deliberately; not required on every commit).

## NOTICE template (every public repo)

```text
<Product display name>
Copyright 2026 XGIC

This product includes software and documentation developed at XGIC
(https://xgic.net).

Licensed under the Apache License, Version 2.0.
See the LICENSE file for details.
```

## LICENSE file

- Root `LICENSE` contains the **full** Apache License 2.0 text.
- Appendix short form uses **Copyright 2026 XGIC** (no personal name, no email).
- Do not prepend custom preambles before the Apache title block (breaks GitHub license detection).

## Package metadata

- SPDX / `license` field: `Apache-2.0`
- Classifiers: Apache Software License where applicable
- `authors`: org-facing identity **`XGIC`** (optional contact email such as `dev@xgic.net` is fine for contact, not as copyright owner)

## Why Apache 2.0

- Explicit patent grant suitable for enterprise and client adoption
- Clear contribution terms for multi-repo ecosystems
- Compatible with common open-source dependency graphs
- Professional default for libraries, CLIs, images’ accompanying source, and documentation

## Agent rules

When creating or advising on new **public** XGIC repositories:

1. Include full Apache-2.0 `LICENSE` and a `NOTICE` using **Copyright 2026 XGIC**.
2. Set package metadata / SPDX identifiers to `Apache-2.0`.
3. Do not mix in copyleft assumptions without an explicit human-approved ADR.
4. Third-party dependencies retain their own licenses; document them in the consuming repo as usual.
5. Vendor products (e.g. GitLab EE) are not covered by this repository’s Apache-2.0 grant—document that separation in the product README when relevant.

## Related ADR

- [ADR-0004: Apache 2.0 for XGIC public solutions](adr/0004-apache-2-0-for-public-solutions.md)
