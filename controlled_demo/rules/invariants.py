from controlled_demo.model.state import State

def validate_invariants(state: State) -> None:
    """
    Minimal invariant check for Controlled Reference Demo.
    """

    if state.P < 0:
        raise ValueError("P must be non-negative")

    if state.M_VAL < 0:
        raise ValueError("M_VAL must be non-negative")

    if state.F_stab < 0:
        raise ValueError("F_stab must be non-negative")

    if state.F_liq < 0:
        raise ValueError("F_liq must be non-negative")

    if state.F_sys < 0:
        raise ValueError("F_sys must be non-negative")

    if state.TimeCapital_total < 0:
        raise ValueError("TimeCapital_total must be non-negative")

    if state.Supply < 0:
        raise ValueError("Supply must be non-negative")