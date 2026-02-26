from dataclasses import dataclass


@dataclass(frozen=True)
class State:
    """
    Deterministic system state for Controlled Reference Demo.

    All fields must remain finite and non-negative unless explicitly defined.
    """

    # Core economic references
    P: float  # protocol price reference
    M_VAL: float  # valuation reference multiplier

    # Funds
    F_stab: float
    F_liq: float
    F_sys: float

    # Time Capital
    TimeCapital_total: float
    TimeCapital_active: float

    # Supply
    Supply: float

    # Control
    paused: bool
    epoch: int

    def validate_non_negative(self):
        assert self.P >= 0
        assert self.M_VAL >= 0
        assert self.F_stab >= 0
        assert self.F_liq >= 0
        assert self.F_sys >= 0
        assert self.TimeCapital_total >= 0
        assert self.TimeCapital_active >= 0
        assert self.Supply >= 0
        assert self.epoch >= 0
        assert self.TimeCapital_active <= self.TimeCapital_total