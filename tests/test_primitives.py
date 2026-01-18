import pytest
from dataclasses import FrozenInstanceError
from datetime import date
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


from src.domain.primitives import OptionContract, Position, Portfolio


def test_option_contract_creation():
    opt = OptionContract(
        symbol="AAPL",
        strike_price=180.0,
        expiration_date=date(2025, 3, 21),
        exercise_type="American",
        option_type="Call",
    )

    assert opt.symbol == "AAPL"
    assert opt.option_type == "Call"


def test_option_contract_is_immutable():
    opt = OptionContract(
        symbol="AAPL",
        strike_price=180.0,
        expiration_date=date(2025, 3, 21),
        exercise_type="American",
        option_type="Call",
    )

    with pytest.raises(FrozenInstanceError):
        opt.strike_price = 200.0


def test_position_equality():
    opt = OptionContract(
        symbol="AAPL",
        strike_price=180.0,
        expiration_date=date(2025, 3, 21),
        exercise_type="European",
        option_type="Put",
    )

    p1 = Position(option=opt, quantity=1, entry_price=2.5)
    p2 = Position(option=opt, quantity=1, entry_price=2.5)

    assert p1 == p2


def test_portfolio_creation_and_types():
    portfolio = Portfolio(positions=(), cash=1000.0)

    assert isinstance(portfolio.positions, tuple)
    assert portfolio.cash == 1000.0
