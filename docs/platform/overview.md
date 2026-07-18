# Platform overview — Docker Compose first, Kubernetes ready

## Intent

XGIC public solutions target a **full-stack cloud-native platform** over time, while remaining excellent for **on-premises and lab** environments from day one.

| Horizon | Default runtime | Docs |
|---------|-----------------|------|
| Now / near-term | **Docker Compose** | [docker-compose.md](docker-compose.md) |
| Scale / multi-cluster | **Kubernetes** | [kubernetes.md](kubernetes.md) |
| Mixed | **Hybrid** | [hybrid.md](hybrid.md) |

Formal decision: [ADR-0003](../adr/0003-docker-compose-first-kubernetes-ready.md).

## Principles

1. **Same application contracts** — Config via env/files; no orchestrator-only business logic.  
2. **Official vendor images** for third-party services when possible.  
3. **Orchestration is thin** — Docker Compose/K8s declare topology; images and apps remain portable.  
4. **Document both paths** in this hub; implement path-specific manifests in product repos.  
5. **Agent default** — Recommend Docker Compose unless the user states HA, multi-tenant cluster, or cloud-native constraints.

## Capability matrix (target)

| Concern | Docker Compose (on-prem) | Kubernetes (cloud-native) |
|---------|-------------------|---------------------------|
| Local/lab bootstrap | Excellent | Optional / heavier |
| Single-node production | Good | Possible |
| Multi-node HA | Limited | Strong |
| GitOps | Possible | Strong |
| Autoscaling | Limited | Strong |
| Policy / mesh | Limited | Ecosystem-rich |

## Related vision

See [VISION.md](../VISION.md) for phased platform evolution.
