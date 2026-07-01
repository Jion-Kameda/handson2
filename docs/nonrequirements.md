# Non-Functional Requirements

## Scope
This document defines minimal non-functional requirements for the Azure Functions API.

## Platform and Runtime Constraints
1. Cloud platform shall be Microsoft Azure.
2. Deployment region shall be Japan East.
3. Hosting plan shall be Azure Functions Consumption Plan.
4. Development language/runtime shall be Python 3.11.

## Security
1. HTTP trigger authorization level shall be Anonymous.
2. The service shall expose only the required API endpoints for this scope.

## Operability (Minimal)
1. The system shall log request processing results and errors.
2. Error responses shall be deterministic and match the functional requirement definitions.

## Cost and Scaling (Consumption Plan)
1. The service shall use pay-per-execution billing provided by Consumption Plan.
2. The service shall rely on platform-managed auto-scaling behavior of Consumption Plan.

## Out of Scope for This Phase
- Formal SLO/SLA definitions
- Advanced monitoring dashboards and alert tuning
- WAF/CDN/network segmentation design
- Backup/DR design for stateful data (this API is stateless in current scope)
