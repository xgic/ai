# Kubernetes — cloud-native scale-out path

## When to use

- Multi-node high availability  
- Cloud or datacenter clusters with GitOps  
- Autoscaling, advanced networking, and platform policy requirements  

## Practices

1. **Do not block** Compose users: keep Compose path working.  
2. Map Compose services → Deployments/StatefulSets + Services + ConfigMaps/Secrets.  
3. Prefer portable images already used in Compose.  
4. Introduce Helm/Kustomize/operators in **product** repos when complexity warrants it.  
5. Observe resource requests/limits, probes, and PDB patterns early.  
6. Document cluster prerequisites (ingress, storage classes, cert management).

## Agent checklist

- [ ] User actually needs K8s (not just “cloud”)  
- [ ] App is 12-factor / config-externalized  
- [ ] Images published to a registry agents can reference publicly when applicable  
- [ ] Rollback and backup story exists  
- [ ] Hub ADR-0003 cited for the dual-path strategy  

## Non-goals (for this hub)

This repository does **not** currently ship cluster controllers or full platform operators. It defines **recommendations** and **decision records** so product repos stay aligned.
