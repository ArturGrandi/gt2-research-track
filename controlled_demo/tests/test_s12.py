import sys

sys.path.insert(0, "controlled_demo")

from model.state import State
from model.events import Event, EventType
from model.transition import delta


def test_zone_boundary_stress():
    """
    S12 — Zone Boundary Stress
    F_stab exactly equals mint coverage gate
    """

    s = State(
        P=10_000_000,
        M_VAL=1,
        F_stab=10_000_000,
        F_liq=0,
        F_sys=0,
        TimeCapital_total=0,
        TimeCapital_active=0,
        Supply=0,
        paused=False,
        epoch=0,
    )

    e = Event(type=EventType.MINT_TRIGGER)

    s2 = delta(s, e)

    assert s2.Supply == 1
    assert s2.paused is False
