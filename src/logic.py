from enum import Enum

from src.choices import CHOICE
from typing import TypedDict


class ChoiceLogicEntry(TypedDict):
    beats: CHOICE
    beaten_by: CHOICE


CHOICE_LOGIC: dict[CHOICE, ChoiceLogicEntry] = {
    CHOICE.ROCK: {
        'beats': CHOICE.SCISSORS,
        'beaten_by': CHOICE.PAPER
    },
    CHOICE.PAPER: {
        'beats': CHOICE.ROCK,
        'beaten_by': CHOICE.SCISSORS
    },
    CHOICE.SCISSORS: {
        'beats': CHOICE.PAPER,
        'beaten_by': CHOICE.ROCK
    }
}


class OUTCOME(Enum):
    HUMAN_WIN = 'Human wins!'
    COMPUTER_WIN = 'Computer wins!'
    DRAW = 'Draw!'


def get_outcome(human_choice: CHOICE, computer_choice: CHOICE) -> OUTCOME:
    try:
        human_choice_logic_entry = CHOICE_LOGIC[human_choice]
    except KeyError:
        raise RuntimeError(f'Game logic error: human_choice={human_choice} not in CHOICE_LOGIC')

    if human_choice == computer_choice:
        return OUTCOME.DRAW
    elif human_choice_logic_entry['beats'] == computer_choice:
        return OUTCOME.HUMAN_WIN
    elif human_choice_logic_entry['beaten_by'] == computer_choice:
        return OUTCOME.COMPUTER_WIN
    else:
        raise RuntimeError(f"Game logic error: human_choice={human_choice}, computer_choice={computer_choice}")

