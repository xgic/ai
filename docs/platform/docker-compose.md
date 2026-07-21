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
6. **Named volumes** for durable data; document backup expectations in the product repo.  
7. **Deployment quality (every environment):** Docker Compose instances must be **idempotent** (re-apply converges), **reliable** (health probes, restart policy, safe dry-run/confirm for destructive ops), and **reproducible** (pinned tags, documented env files, same procedure for every operator). Portfolio rule: [BASE-STANDARDS — Deployment quality attributes](../BASE-STANDARDS-FOR-ORCHESTRATED-REPOS.md#deployment-quality-attributes-mandatory--every-environment).

## Agent checklist

- [ ] Docker Compose file(s) validated (`docker compose config`)  
- [ ] No secrets committed  
- [ ] Service names stable for app connection strings  
- [ ] README documents up/down/backup  
- [ ] Image/runtime versions pinned for reproducibility  
- [ ] Healthchecks (or documented equivalent) present for critical services  
- [ ] Re-run of configure/deploy is safe (idempotent)  
- [ ] Path to K8s noted if production scale is expected later  

## Example topology (illustrative)

```text
[ app / cms ] ──► [ postgres ]
      │
      └──► [ redis ] (if required)
[ reverse-proxy ] (optional)
```

Product repositories own the concrete Docker Compose files; this hub owns the **pattern**.
