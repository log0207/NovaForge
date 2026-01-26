# Production Deployment Guide

This guide is intended for engineers who deploy OpenVault to production.

## Environments

| Environment | Identifier |
|-------------|------------|
| Development | DEV        |
| Staging     | STAGE      |
| Production  | ORION      |

## Server groups

Production workloads run in the ORION environment on server group
OX-17.

Machine: OX-17

## Deployment

Deployments are triggered from CI. Environment configuration must
never be committed to the repository.

<!-- Maybe Useful : NF{TIMELINE_08} -->
