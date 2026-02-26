from controlled_demo.model.state import State
from controlled_demo.model.events import Event, EventType
from controlled_demo.rules.invariants import validate_invariants


def delta(state: State, event: Event) -> State:

    if event.type == EventType.EPOCH_ADVANCE:
        new_state = State(
            P=state.P,
            M_VAL=state.M_VAL,
            F_stab=state.F_stab,
            F_liq=state.F_liq,
            F_sys=state.F_sys,
            TimeCapital_total=state.TimeCapital_total,
            TimeCapital_active=state.TimeCapital_active,
            Supply=state.Supply,
            paused=state.paused,
            epoch=state.epoch + 1,
        )

    elif event.type == EventType.EMERGENCY_TRIGGER:
        new_state = State(
            P=state.P,
            M_VAL=state.M_VAL,
            F_stab=state.F_stab,
            F_liq=state.F_liq,
            F_sys=state.F_sys,
            TimeCapital_total=state.TimeCapital_total,
            TimeCapital_active=state.TimeCapital_active,
            Supply=state.Supply,
            paused=True,
            epoch=state.epoch,
        )

    else:
        new_state = state

    validate_invariants(new_state)
    return new_state