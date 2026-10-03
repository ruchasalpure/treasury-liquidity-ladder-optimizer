# Multi-Agent Coordination Specification

## Assigned Roles
Maker:
milp-cash-scheduler

Checker:
regulatory-buffer-checker

## Coordination Protocol
- **Primary Agent**: treasury-liquidity-ladder-optimizer
- **Governance Standard**: OpenGAP Dual-Agent Control Framework v0.1.0
- **Consensus Threshold**: 100% agreement between Maker and Checker before state mutations.
- **Fail-safe Mode**: If verification fails, transaction rolls back and alerts human supervisor.
