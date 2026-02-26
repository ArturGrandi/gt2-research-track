from controlled_demo.model.state import State
from controlled_demo.model.transition import delta

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

  
def test_epoch_advance():
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

    from controlled_demo.model.events import Event, EventType
    from controlled_demo.model.transition import delta

    e = Event(type=EventType.EPOCH_ADVANCE)

    s2 = delta(s, e)

    assert s2.epoch == 1
    assert s.epoch == 0

    def test_emergency_trigger_properties():
        s = State(
            P=1.5,
            M_VAL=2.0,
            F_stab=150.0,
            F_liq=10.0,
            F_sys=5.0,
            TimeCapital_total=20.0,
            TimeCapital_active=3.0,
            Supply=50.0,
            paused=False,
            epoch=7,
        )

        e = Event(type=EventType.EMERGENCY_TRIGGER)

        s2 = delta(s, e)

        # 1. Regime change
        assert s2.paused is True

        # 2. Epoch invariance
        assert s2.epoch == s.epoch

        # 3. Economic state preservation
        assert s2.P == s.P
        assert s2.M_VAL == s.M_VAL
        assert s2.F_stab == s.F_stab
        assert s2.F_liq == s.F_liq
        assert s2.F_sys == s.F_sys
        assert s2.TimeCapital_total == s.TimeCapital_total
        assert s2.TimeCapital_active == s.TimeCapital_active
        assert s2.Supply == s.Supply

        # 4. Immutability (original untouched)
        assert s.paused is False