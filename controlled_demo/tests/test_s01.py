from controlled_demo.model.state import State


def test_initial_state_valid():
    s = State(
        P=1.0,
        M_VAL=1.0,
        F_stab=100.0,
        F_liq=0.0,
        F_sys=0.0,
        TimeCapital_total=0.0,
        TimeCapital_active=0.0,
        Supply=0.0,
        paused=False,
        epoch=0,
    )

    s.validate_non_negative()