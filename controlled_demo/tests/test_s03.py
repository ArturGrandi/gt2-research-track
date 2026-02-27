from controlled_demo.model.state import State
from controlled_demo.model.events import Event, EventType
from controlled_demo.model.transition import delta


def test_oracle_update_properties_bounded_and_isolated():
    s = State(
        P=100.0,
        M_VAL=50.0,
        F_stab=150.0,
        F_liq=10.0,
        F_sys=5.0,
        TimeCapital_total=0.0,
        TimeCapital_active=0.0,
        Supply=0.0,
        paused=False,
        epoch=7,
    )

    # within 20% bound: 100 -> 110 (+10%)
    e = Event(type=EventType.ORACLE_UPDATE, payload={"P": 110.0})
    s2 = delta(s, e)

    # 1) Bounded update applied
    assert s2.P == 110.0
    assert s2.M_VAL == s.M_VAL

    # 2) Regime preservation (pause + epoch unchanged)
    assert s2.paused == s.paused
    assert s2.epoch == s.epoch

    # 3) Economic state isolation (everything else unchanged)
    assert s2.F_stab == s.F_stab
    assert s2.F_liq == s.F_liq
    assert s2.F_sys == s.F_sys
    assert s2.TimeCapital_total == s.TimeCapital_total
    assert s2.TimeCapital_active == s.TimeCapital_active
    assert s2.Supply == s.Supply


def test_oracle_update_rejects_out_of_bounds_step():
    s = State(
        P=100.0,
        M_VAL=50.0,
        F_stab=150.0,
        F_liq=10.0,
        F_sys=5.0,
        TimeCapital_total=0.0,
        TimeCapital_active=0.0,
        Supply=0.0,
        paused=False,
        epoch=7,
    )

    # 100 -> 200 (+100%) should fail (bound is 20%)
    e = Event(type=EventType.ORACLE_UPDATE, payload={"P": 200.0})

    try:
        delta(s, e)
        assert False, "Expected ValueError for out-of-bounds oracle update"
    except ValueError:
        assert True
