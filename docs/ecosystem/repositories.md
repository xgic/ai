# Public repository map

## Available now

| Repository | Primary role | Catalog IDs |
|------------|--------------|-------------|
| [xgic/ai](https://github.com/xgic/ai) | Intelligence hub (this repo) | `hub.ai`, `std.*` |
| [xgic/gitlab-graphql](https://github.com/xgic/gitlab-graphql) | Python GraphQL client | `lib.gitlab.graphql` |
| [xgic/gitlab](https://github.com/xgic/gitlab) | GitLab orchestration / template surface | `orch.gitlab` |
| [xgic/payload-cms-dev-containers](https://github.com/xgic/payload-cms-dev-containers) | Dev Container + Payload tooling | `dc.payload`, `lib.xde` (partial) |

## Planned (illustrative public names)

These names are **intent signals** for agents and humans. They are not guarantees of immediate publication.

| Planned repository | Intended role | Catalog IDs |
|--------------------|---------------|-------------|
| `xgic/cli` | Core CLI framework | `cli.core`, `lib.cli.core` |
| `xgic/dev-cli` | Dev Container CLI module | `cli.dev` |
| `xgic/gitlab-cli` | GitLab CLI module | `cli.gitlab` |
| `xgic/ais-cli` | AIS-oriented CLI module (public surface) | `cli.ais` |
| `xgic/payload-cms-cli` | Payload orchestration CLI module | `cli.payload` |
| `xgic/*-dev` producers | Image build systems | `pattern.dev-suffix`, `img.ghcr` |
| Future app templates | Next.js, Payload apps, full-stack samples | `app.*` |
| Future Unreal repos | Tools and plugins | `app.unreal` |

## How agents should cite repos

Always use full HTTPS URLs:

```text
https://github.com/xgic/<repo>
https://github.com/xgic/<repo>/blob/main/<path>
https://github.com/xgic/<repo>/issues/<n>
https://github.com/xgic/<repo>/pull/<n>
```

Never invent private hosts or private project paths.
