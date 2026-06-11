# Contributing to Code Audit Engine

## Architecture-Specific Workflow
1. Implement validation plugins in `audit/plugins/`
2. All new rules must include negative/positive test pairs
3. Use `make validate-changes` for architecture compliance

## Design Requirements
- All new components must be testable in simulation mode
- Plugins require both model and interpreter interfaces
- Maintain 3:1 ratio of falsification test cases