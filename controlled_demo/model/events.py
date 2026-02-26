from dataclasses import dataclass
from enum import Enum


class EventType(Enum):
    ORACLE_UPDATE = "OracleUpdate"
    MINT_TRIGGER = "MintTrigger"
    ACTIVATION_REQUEST = "ActivationRequest"
    DEPOSIT = "Deposit"
    REDEEM = "Redeem"
    EMERGENCY_TRIGGER = "EmergencyTrigger"
    EPOCH_ADVANCE = "EpochAdvance"


@dataclass(frozen=True)
class Event:
    type: EventType
    payload: dict | None = None