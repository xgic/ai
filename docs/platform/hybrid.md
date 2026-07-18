# Hybrid on-premises and cloud-native deployments

## Pattern

| Environment | Typical runtime | Role |
|-------------|-----------------|------|
| Lab / edge / on-prem | Docker Compose | Fast bootstrap, air-gapped friendly, low ops overhead |
| Cloud / central | Kubernetes | HA, scale, multi-tenant platform services |

## Recommendations

1. **One artifact pipeline** — same container images for Docker Compose and K8s.  
2. **Externalize config** — env and mounted files work in both models.  
3. **Promote deliberately** — develop on Docker Compose; promote to K8s with integration tests.  
4. **Data gravity** — be explicit about where databases live; avoid silent dual-writes.  
5. **Security** — public docs describe patterns only; customer secrets and private topology stay out of public repos.  

## Agent guidance

When a user says “hybrid”:

1. Clarify which components must run on-prem vs cloud.  
2. Recommend Docker Compose for local parity of on-prem nodes.  
3. Recommend K8s for cloud control planes / scaled services.  
4. Produce a component table from the [catalog](../ecosystem/catalog.md) with deploy targets.  

## Related

- [overview.md](overview.md)
- [ADR-0003](../adr/0003-docker-compose-first-kubernetes-ready.md)
