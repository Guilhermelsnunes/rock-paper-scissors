import pytest

from src.choices import CHOICE
from src.logic import get_outcome, OUTCOME


@pytest.mark.parametrize('human_choice, computer_choice, expected_outcome',
    [
        (CHOICE.ROCK, CHOICE.ROCK, OUTCOME.DRAW),
        (CHOICE.ROCK, CHOICE.PAPER, OUTCOME.COMPUTER_WIN),
        (CHOICE.ROCK, CHOICE.SCISSORS, OUTCOME.HUMAN_WIN),
        (CHOICE.PAPER, CHOICE.ROCK, OUTCOME.HUMAN_WIN),
        (CHOICE.PAPER, CHOICE.PAPER, OUTCOME.DRAW),
        (CHOICE.PAPER, CHOICE.SCISSORS, OUTCOME.COMPUTER_WIN),
        (CHOICE.SCISSORS, CHOICE.ROCK, OUTCOME.COMPUTER_WIN),
        (CHOICE.SCISSORS, CHOICE.PAPER, OUTCOME.HUMAN_WIN),
        (CHOICE.SCISSORS, CHOICE.SCISSORS, OUTCOME.DRAW),
    ]
)
def test_logic(human_choice: CHOICE, computer_choice: CHOICE, expected_outcome: OUTCOME) -> None:
    assert get_outcome(human_choice=human_choice, computer_choice=computer_choice) == expected_outcome


def test_logic__invalid_human_choice_raises():
    with pytest.raises(RuntimeError, match='Game logic error: human_choice=invalid not in CHOICE_LOGIC'):
        assert get_outcome(human_choice='invalid', computer_choice=CHOICE.ROCK)  # type: ignore


def test_logic__invalid_computer_choice_raises():
    with pytest.raises(RuntimeError, match='Game logic error: human_choice=CHOICE.ROCK, computer_choice=invalid'):
        assert get_outcome(human_choice=CHOICE.ROCK, computer_choice='invalid')  # type: ignore
