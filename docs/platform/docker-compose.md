# Docker Compose — on-premises and lab default

## When to use

- Workstations, labs, and on-premises single-host (or small host) deployments  
- Contributor environments and demos  
- First production footprint when HA/multi-cluster is not required  

## Practices

1. **One stack per concern** where practical (e.g. data services vs app) or a clear mono-compose with profiles.  
2. **Official images** for Postgres, Redis, GitLab EE, etc.  
3. **Bind configs, not secrets into git** — use `.env` (gitignored) and documented examples.  
4. **Healthchecks** and restart policies for operator-friendly recovery.  
5. **Dev Containers** may wrap the same Docker Compose services for IDE parity.  
5a. **Project identity:** set top-level Compose `name:`. Keep `XGIC_COMPOSE_PROJECT`, `composeProjectName` (if used), and `XGIC_PRIMARY_SERVICE` / `devcontainer.json` `service` aligned with that name. Export the `XGIC_COMPOSE_*` variables on the primary service. Naming: `xgic-<product>` (template) and `xgic-<product>-dev` (producer). The generic CLI default `xgic-dev` is last-resort only when no `name:` is present. `docker compose -p` must not silently create a second project next to the Dev Container.  
5b. **Docker-outside-of-Docker (when a Dev Container needs `docker`):** install a Docker **CLI** (and Compose plugin) in the producer image; mount `/var/run/docker.sock`; align the image `docker` group to the socket GID at start. Do **not** run `dockerd` in the app container (no Docker-in-Docker) unless a separate design is approved.  
6. **Named volumes** for durable data; document backup expectations in the product repo.  
7. **Deployment quality:** every Docker Compose instance must be **idempotent**, **reliable**, and **reproducible** ([BASE-STANDARDS](../BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md#deployment-quality-attributes-mandatory--every-environment)).  
8. **GitLab EE stacks:** pin PostgreSQL to the **latest major GitLab supports** for the selected EE major (EE **18.x** / **19.x** → PostgreSQL **17**). Re-check GitLab’s published requirements when upgrading EE; validate with a successful `gitlab-backup create` database dump after pin changes. Template defaults: [xgic/gitlab](https://github.com/xgic/gitlab).

## Agent checklist

- [ ] Docker Compose file(s) validated (`docker compose config`)  
- [ ] No secrets committed  
- [ ] Service names stable for app connection strings  
- [ ] README documents up/down/backup  
- [ ] Image/runtime versions pinned for reproducibility  
- [ ] Healthchecks (or documented equivalent) present for critical services  
- [ ] Re-run of configure/deploy is safe (idempotent)  
- [ ] For GitLab EE: `POSTGRES_VERSION` is the latest major supported by the EE pin  
- [ ] Path to K8s noted if production scale is expected later  

## Example topology (illustrative)

```text
[ app / cms ] ──► [ postgres ]
      │
      └──► [ redis ] (if required)
[ reverse-proxy ] (optional)
```

Product repositories own the concrete Docker Compose files; this hub owns the **pattern**.
