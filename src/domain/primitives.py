from dataclasses import dataclass
from typing import Literal, Tuple

@dataclass(frozen=True)
class OptionContract:
    """
    Represents an immutable option contract with details such as symbol, 
    strike price, expiration date, exercise type, and option type.

    This class is immutable due to the `frozen=True` parameter in the 
    @dataclass decorator. Once an instance is created, its attributes 
    cannot be modified.

    Attributes:
        symbol (str): The ticker symbol of the underlying asset.
        strike_price (float): The strike price of the option.
        expiration_date (str): The expiration date of the option.
        exercise_type (Literal["American", "European"]): The exercise type of the option.
        option_type (Literal["Call", "Put"]): The type of the option (Call or Put).
    """
    symbol: str
    strike_price: float
    expiration_date: str
    exercise_type: Literal["American", "European"]
    option_type: Literal["Call", "Put"]


@dataclass(frozen=True)
class Position:
    """
    Represents an immutable position in a portfolio, consisting of an option contract, 
    the quantity of the position, and the entry price.

    Attributes:
        option (OptionContract): The option contract associated with the position.
        quantity (int): The number of contracts in the position.
        entry_price (float): The price at which the position was entered.
    """
    option: OptionContract
    quantity: int
    entry_price: float


@dataclass(frozen=True)
class Portfolio:
    """
    Represents an immutable portfolio consisting of positions and available cash.

    Attributes:
        positions (Tuple[Position, ...]): A tuple of positions in the portfolio.
        cash (float): The amount of cash available in the portfolio.
    """
    positions: Tuple[Position, ...]
    cash: float