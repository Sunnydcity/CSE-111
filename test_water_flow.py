import pytest
from pytest import approx
from water_flow import (
    water_column_height,
    pressure_gain_from_water_height,
    pressure_loss_from_pipe,
    pressure_loss_from_fittings,
    reynolds_number,
    pressure_loss_from_pipe_reduction,
)

# Constants
TOLERANCE = 0.001  # For approx comparison


def test_water_column_height():
    assert water_column_height(0.0, 0.0) == approx(0.0, abs=TOLERANCE)
    assert water_column_height(0.0, 10.0) == approx(7.5, abs=TOLERANCE)
    assert water_column_height(25.0, 0.0) == approx(25.0, abs=TOLERANCE)
    assert water_column_height(48.3, 12.8) == approx(57.9, abs=TOLERANCE)


def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == approx(0.000, abs=TOLERANCE)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=TOLERANCE)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=TOLERANCE)


def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=TOLERANCE)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs=TOLERANCE)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs=TOLERANCE)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=TOLERANCE)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=TOLERANCE)


def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, abs=TOLERANCE)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000, abs=TOLERANCE)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=TOLERANCE)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=TOLERANCE)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=TOLERANCE)


def test_reynolds_number():
    assert reynolds_number(0.048692, 0.00) == approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)


def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == approx(0.000, abs=TOLERANCE)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=TOLERANCE)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=TOLERANCE)


if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN"])