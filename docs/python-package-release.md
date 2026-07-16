# Public Python package release process (XGIC)

**Audience:** maintainers, release operators, and AI agents working on public XGIC Python packages under [github.com/xgic](https://github.com/xgic).  
**Authority:** Living multi-repo standard. Cited from [BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md).  
**Scope:** Packages intended for distribution via [PyPI](https://pypi.org/) (and pre-release validation via [TestPyPI](https://test.pypi.org/)).

---

## 1. Principles (non-negotiable)

1. **Best practice is the only acceptable method.** Do not invent alternate publish paths for convenience.  
2. **Publish only from GitHub Actions** on the public repository—never from a maintainer laptop for official releases.  
3. **OIDC Trusted Publishing** is the only acceptable authentication model for TestPyPI and PyPI.  
4. **Long-lived PyPI API tokens are forbidden** for routine releases.  
5. **Release candidates go to TestPyPI first**; finals go to PyPI only after clean-env smoke succeeds.  
6. **`uv` is required** for build and for clean-environment install smoke.  
7. **Upload to the index uses only** [`pypa/gh-action-pypi-publish`](https://github.com/pypa/gh-action-pypi-publish) with Trusted Publishing (OIDC).  
8. **Public-safe always:** no private hosts, private tracker IDs, internal paths, or credentials in workflows, docs, or package metadata ([BASE-STANDARDS](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md)).  
9. **Human review gate** applies to workflow and docs changes; release jobs may run after an approved tag/release process defined below.  
10. **Metadata:** Apache-2.0, `Copyright 2026 XGIC`, authors `XGIC` only ([ADR-0004](adr/0004-apache-2-0-for-public-solutions.md)). Python **3.14+** for new packages ([ADR-0002](adr/0002-standardize-on-python-3-14.md)).

---

## 2. Tooling split (mandatory)

| Step | Only acceptable tool / mechanism |
|------|----------------------------------|
| Create clean smoke environments | `uv venv` (or equivalent `uv` project env) |
| Install packages for smoke tests | `uv pip install …` |
| Build sdist and wheel | `uv build` |
| Upload to TestPyPI / PyPI | **`pypa/gh-action-pypi-publish`** with **OIDC Trusted Publishing** only |
| Unit/lint tests (per package) | Project CI as already defined (e.g. `pytest`, `ruff`); Python 3.14 |

**Not acceptable for official releases**

- `uv publish` (or `twine`) with long-lived tokens  
- Publishing from a developer workstation  
- Editable (`pip install -e` / `uv sync`) installs as the **only** install verification  
- Skipping TestPyPI for first-time packaging layout changes or multi-package stack releases  

**Rationale (summary):** Trusted Publishing removes standing secrets and binds uploads to a specific repository, workflow, and (recommended) GitHub Environment. The PyPA action is the path PyPI documents for ordinary GitHub Actions users. `uv` remains the standard for build and install verification, including multi-package namespace stacks under `xgic.*`.

---

## 3. Package families and publish order

For modular CLI and libraries that share the `xgic` namespace ([namespace convention](xgic-python-namespace-convention.md)):

| Order | Distribution (example) | Namespace (example) | Repository (example) |
|------:|------------------------|---------------------|----------------------|
| 1 | `xgic-cli` | `xgic.cli` | [xgic/cli](https://github.com/xgic/cli) |
| 2 | `xgic-dev-cli` | `xgic.cli.dev` | [xgic/dev-cli](https://github.com/xgic/dev-cli) |
| 3 | `xgic-payload-cms-cli` | `xgic.cli.payload` | [xgic/payload-cms-cli](https://github.com/xgic/payload-cms-cli) |

**Always publish and smoke in dependency order** (core first, then modules that depend on core).

### Namespace packaging rules (release blockers)

Domain packages **must not** ship intermediate `xgic/__init__.py` or `xgic/cli/__init__.py` files that overwrite the core package on non-editable install. After a full-stack install, this **must** succeed:

```bash
python -c "from xgic.cli import __version__; print(__version__)"
```

---

## 4. Versioning

| Stage | Index | Version pattern (examples) |
|-------|--------|----------------------------|
| Pull request / main CI | *(no index)* | Build local artifacts only; do not publish |
| Release candidate | TestPyPI | `X.Y.ZrcN` (e.g. `0.2.0rc1`) — unique per upload |
| Final release | PyPI | `X.Y.Z` matching the Git tag (e.g. `v0.2.0` → `0.2.0`) |

- Prefer **aligned** versions across a coordinated multi-package release when modules ship together.  
- Do not reuse a version string on an index after a bad upload; cut a new RC or patch.  
- Yank only for security or severe breakage; prefer a fix release.

---

## 5. Continuous integration (every PR affecting packaging)

On every PR that changes package code, `pyproject.toml`, build config, or publish workflows:

### 5.1 Quality

- Lint and unit tests for the package (existing package CI).  
- `uv build` must produce sdist + wheel.

### 5.2 Clean-env install matrix (mandatory)

Use a **fresh** environment per matrix cell (no editable install of the package under test).

| Matrix cell | Install (local wheels) | Minimum assertions |
|-------------|------------------------|--------------------|
| **Core alone** | `xgic-cli` wheel | `from xgic.cli import __version__`; `xgic --version`; `xgic info` (or package equivalent) |
| **Core + dev** | + `xgic-dev-cli` wheel | `import xgic.cli.dev`; `xgic up --help` (or module equivalent) |
| **Full stack** | + domain modules (e.g. `xgic-payload-cms-cli`) | All prior imports; domain help (e.g. `xgic payload --help`); `from xgic.cli import __version__` still works |

Illustrative commands (adapt paths):

```bash
uv venv .venv-smoke
# Windows: .venv-smoke\Scripts\activate
source .venv-smoke/bin/activate
uv pip install --upgrade pip
uv pip install ./cli/dist/*.whl
uv pip install ./dev-cli/dist/*.whl   # when testing +dev or full
uv pip install ./payload-cms-cli/dist/*.whl  # when testing full stack
xgic --version
python -c "from xgic.cli import __version__; from xgic.cli.dev import DockerComposeController"
```

Failure of any matrix cell **blocks** merge of packaging changes.

---

## 6. One-time setup (per public package on PyPI)

Perform once per distribution name on **TestPyPI** and on **PyPI**:

1. Create the project on the index (or first successful publish).  
2. Configure a **Trusted Publisher** (GitHub Actions):
   - Owner: `xgic`
   - Repository: package repo name  
   - Workflow filename: the release workflow (e.g. `release.yml`)  
   - Environment name: exact match to the GitHub Environment (e.g. `testpypi` / `pypi`)  
3. In the GitHub repository:
   - Create Environments `testpypi` and `pypi`  
   - Restrict deployable branches (e.g. tags only / `main` as policy dictates)  
   - Optional but recommended for `pypi`: required reviewers  
4. Ensure the release workflow job sets:

```yaml
permissions:
  id-token: write   # required for OIDC
  contents: read
environment: pypi   # or testpypi
```

5. Do **not** store `PYPI_API_TOKEN` (or password) secrets for routine publish.

---

## 7. Release candidate process (TestPyPI)

### 7.1 Preconditions

- [ ] Changes merged to `main` (or the release branch policy of that repo) with human UI approval  
- [ ] Version bumped to an RC string (e.g. `0.2.0rc1`) in `pyproject.toml`  
- [ ] Changelog / release notes drafted (public-safe)  
- [ ] Package CI green on the release commit  
- [ ] Clean-env install matrix green (local wheels)

### 7.2 Build

```bash
uv build
# Artifacts under dist/: sdist + wheel
```

Prefer CI: checkout at the release ref → `uv build` → upload `dist/` as workflow artifacts.

### 7.3 Publish RC to TestPyPI

- Trigger the **release-candidate** workflow (tag `vX.Y.ZrcN` or `workflow_dispatch` with version input—repo choice, but **must** be GitHub Actions).  
- Job uses **Environment `testpypi`** and:

```yaml
- uses: pypa/gh-action-pypi-publish@release/v1
  with:
    repository-url: https://test.pypi.org/legacy/
```

- No username/password/token inputs.

### 7.4 Smoke install from TestPyPI (mandatory)

Clean environment, **production PyPI as extra index** for third-party deps (e.g. `rich`):

```bash
uv venv .venv-testpypi && source .venv-testpypi/bin/activate
uv pip install --upgrade pip
uv pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  "xgic-cli==0.2.0rc1" \
  "xgic-dev-cli==0.2.0rc1" \
  "xgic-payload-cms-cli==0.2.0rc1"   # when releasing the full stack
```

Assertions (adapt to the packages released):

```bash
xgic --version
xgic info
xgic up --help          # if xgic-dev-cli included
xgic payload --help     # if xgic-payload-cms-cli included
python -c "from xgic.cli import __version__; print(__version__)"
```

**Stop here if smoke fails.** Do not promote to PyPI. Fix, cut a new RC version, repeat.

---

## 8. Final release process (PyPI)

### 8.1 Preconditions

- [ ] Successful TestPyPI RC smoke for this version line (or explicit waiver **only** for pure docs packages with no code—default is **no waiver** for `xgic.*` libraries/CLIs)  
- [ ] Final version string set (e.g. `0.2.0`)  
- [ ] Annotated Git tag (recommended): `v0.2.0`  
- [ ] GitHub Release notes ready (public-safe)

### 8.2 Publish final to PyPI

- Trigger the **final release** workflow from the tag (or approved dispatch).  
- Job uses **Environment `pypi`** and:

```yaml
- uses: pypa/gh-action-pypi-publish@release/v1
  # default repository: https://upload.pypi.org/legacy/
```

- Publish packages in **dependency order** (separate jobs or ordered steps with smoke between families if releasing a stack).

### 8.3 Smoke install from PyPI (mandatory)

```bash
uv venv .venv-pypi && source .venv-pypi/bin/activate
uv pip install --upgrade pip
uv pip install \
  "xgic-cli==0.2.0" \
  "xgic-dev-cli==0.2.0" \
  "xgic-payload-cms-cli==0.2.0"
# same assertions as TestPyPI smoke
```

Use **only** the production index (no TestPyPI). Retry briefly if CDN lag occurs; fail the release job if smoke does not pass.

### 8.4 Post-release

- [ ] Confirm GitHub Release attached to the tag  
- [ ] Update [ecosystem catalog](ecosystem/catalog.md) / [namespace summary](xgic-python-namespace-convention.md) if status or version narrative changes  
- [ ] Announce only public-safe content (Discussions/README as appropriate)

---

## 9. Recommended workflow shape (reference)

Repos should implement a single coordinated pattern (names may vary slightly by repo):

```text
CI (PR / push to main)
  → lint + unit tests
  → uv build
  → clean-env install matrix (local wheels)

Release candidate (tag v*.*.*rc* or dispatch)
  → uv build
  → pypa/gh-action-pypi-publish → TestPyPI (OIDC, environment: testpypi)
  → clean-env smoke from TestPyPI

Final release (tag vX.Y.Z)
  → uv build
  → pypa/gh-action-pypi-publish → PyPI (OIDC, environment: pypi)
  → clean-env smoke from PyPI
  → GitHub Release
```

Human approval of the **workflow definition** and of **production Environment** protection settings is required before first use. Cutting a tag that triggers a protected environment may require a human Environment approval—that is intentional.

---

## 10. Multi-package stack release (CLI family)

When releasing several related packages:

1. Tag and RC-publish **core** → TestPyPI smoke (core alone).  
2. Tag and RC-publish **dev module** → TestPyPI smoke (core + dev).  
3. Tag and RC-publish **product modules** → TestPyPI smoke (full stack).  
4. Repeat the same order for **final** PyPI, with full-stack smoke at the end.

Do not publish a dependent module version that requires a core version not yet available on the target index.

---

## 11. Rollback and incidents

| Situation | Action |
|-----------|--------|
| RC broken on TestPyPI | Fix; publish new `rcN+1`; do not promote |
| Final broken on PyPI (non-security) | Publish patch `X.Y.Z+1`; document in release notes |
| Security issue | Follow [SECURITY.md](../SECURITY.md) of the package; yank only if necessary and document |
| Accidental private leakage in metadata/README | Treat as security incident; fix immediately; scrub release notes |

---

## 12. Agent checklist (release work)

1. Confirm public-safe content only.  
2. Confirm version string and dependency order.  
3. Confirm Trusted Publisher + GitHub Environment exist for the target index.  
4. Run or verify **local-wheel clean-env matrix** before any publish job.  
5. Publish RC → **TestPyPI smoke** → only then final → **PyPI smoke**.  
6. Use **`uv` for build/smoke** and **PyPA action for upload** only.  
7. Update catalog/namespace docs if the public surface changed.  
8. Do **not** merge or approve your own release workflow PR; human UI gate applies.

---

## 13. Related documents

| Document | Role |
|----------|------|
| [BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md](BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md) | Public multi-repo minimum standards |
| [xgic-python-namespace-convention.md](xgic-python-namespace-convention.md) | Public `xgic.*` package map |
| [ecosystem/catalog.md](ecosystem/catalog.md) | Component status for agents/humans |
| [ADR-0002](adr/0002-standardize-on-python-3-14.md) | Python 3.14 |
| [ADR-0004](adr/0004-apache-2-0-for-public-solutions.md) | Apache 2.0 |
| [ADR-0005](adr/0005-modular-xgic-cli-and-retirement-of-xde.md) | Modular XGIC CLI |
| [community-health.md](community-health.md) | Labels, templates |
| [PyPI Trusted Publishers](https://docs.pypi.org/trusted-publishers/) | Upstream OIDC model |
| [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish) | Required upload action |
| [uv documentation](https://docs.astral.sh/uv/) | Build and install tooling |

---

*This process is the only acceptable publish path for public XGIC Python packages on GitHub. Deviations require an ADR and explicit human approval.*
