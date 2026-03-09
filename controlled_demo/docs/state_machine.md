# GT Controlled Demo State Machine

Figure: Deterministic GT Protocol State Machine used in the controlled validation demo.

```mermaid
stateDiagram-v2

    [*] --> Active

    Active --> Active : EPOCH_ADVANCE
    Active --> Active : ORACLE_UPDATE
    Active --> Active : MINT_TRIGGER (coverage OK)

    Active --> Paused : MINT_TRIGGER (coverage fail)

    Paused --> Paused : EPOCH_ADVANCE
    Paused --> Paused : ORACLE_UPDATE blocked

    Paused --> Active : EMERGENCY_TRIGGER
