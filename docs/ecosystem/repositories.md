# Public repository map

## Available now

| Repository | Primary role | Catalog IDs |
|------------|--------------|-------------|
| [xgic/ai](https://github.com/xgic/ai) | Intelligence hub (this repo) | `hub.ai`, `std.*` |
| [xgic/cli](https://github.com/xgic/cli) | XGIC CLI thin core | `cli.core`, `lib.cli.core` |
| [xgic/dev-cli](https://github.com/xgic/dev-cli) | Dev Container / Docker Compose module | `cli.dev` |
| [xgic/payload-cms-cli](https://github.com/xgic/payload-cms-cli) | Payload CMS CLI module | `cli.payload` |
| [xgic/gitlab-cli](https://github.com/xgic/gitlab-cli) | GitLab CLI module (B6a bootstrap) | `cli.gitlab` |
| [xgic/gitlab-graphql](https://github.com/xgic/gitlab-graphql) | Python GraphQL client | `lib.gitlab.graphql` |
| [xgic/gitlab](https://github.com/xgic/gitlab) | GitLab orchestration / template surface | `orch.gitlab` |
| [xgic/payload-cms-dev-containers](https://github.com/xgic/payload-cms-dev-containers) | Dev Container + Payload template (XGIC CLI consumer) | `dc.payload` |

## Planned (illustrative public names)

These names are **intent signals** for agents and humans. They are not guarantees of immediate publication.

| Planned repository | Intended role | Catalog IDs |
|--------------------|---------------|-------------|
| `xgic/ais-cli` | AIS-oriented CLI module (public surface) | `cli.ais` |
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
