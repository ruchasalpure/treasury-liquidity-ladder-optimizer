# Duties and Responsibilities for Treasury Liquidity Ladder Optimizer Agent

## Dual-Control Architecture
Maker:
milp-cash-scheduler

Checker:
regulatory-buffer-checker

## Operational Workflow
1. The Maker (milp-cash-scheduler) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (regulatory-buffer-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
