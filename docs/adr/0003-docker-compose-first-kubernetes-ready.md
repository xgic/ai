# ADR-0003: Docker Compose-first deployments with Kubernetes-ready architecture

**Status**: Accepted  
**Date**: 2026-07-11  
**Scope**: Public multi-repository platform guidance for humans and AI agents

---

## Context

XGIC solutions must work well on workstations and on-premises environments while remaining viable as a full-stack cloud-native platform. Docker Compose offers the fastest, most approachable path for labs and many on-prem installs. Kubernetes is the industry default for multi-node HA and cloud operations—but adopting it first often blocks smaller deployments and slows iteration.

Agents need a clear default so recommendations stay consistent across the ecosystem.

---

## Decision

1. **Default deployment documentation and samples use Docker Compose** for on-premises, lab, and single-host scenarios.  
2. **Application and image contracts must remain portable** so the same artifacts can run under Kubernetes without redesigning business logic.  
3. **Kubernetes guidance is first-class documentation** (path, patterns, checklists) and is implemented in product repositories when scale requirements appear.  
4. **Hybrid** deployments (Docker Compose on edge/on-prem + K8s in cloud) are supported as an explicit pattern, not an afterthought.  
5. AI agents **recommend Docker Compose first** unless the user states requirements that justify Kubernetes (HA, multi-cluster, advanced policy/autoscaling, etc.).

---

## Consequences

**Positive**

- Faster onboarding and demos  
- Lower cognitive load for early adopters  
- Clear story for cloud scale-out without rewriting apps  
- Consistent agent behavior across repos  

**Trade-offs**

- Two orchestration stories to maintain (mitigated by shared images/config contracts)  
- Product repos must resist Docker Compose-only hardcoding (e.g. host networking assumptions)

---

## References

- [Platform overview](../platform/overview.md)
- [Docker Compose guide](../platform/docker-compose.md)
- [Kubernetes path](../platform/kubernetes.md)
- [Hybrid guide](../platform/hybrid.md)
- [VISION.md](../VISION.md)
- [ADR-0001](0001-xgic-gitlab-architecture-and-repository-naming.md) (official images, naming)
