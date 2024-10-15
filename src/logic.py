from choices import CHOICE
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


def get_outcome(human_choice: CHOICE, computer_choice: CHOICE) -> str:
    if human_choice == computer_choice:
        return "Draw!"
    elif CHOICE_LOGIC[human_choice]['beats'] == computer_choice:
        return "Human wins!"
    elif CHOICE_LOGIC[human_choice]['beaten_by'] == computer_choice:
        return "Computer wins!"
    else:
        raise RuntimeError("Game logic error")

