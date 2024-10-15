import random
from enum import Enum


class CHOICE(str, Enum):
    ROCK='Rock'
    PAPER='Paper'
    SCISSORS='Scissors'

NUMBERED_CHOICES = {
    1: CHOICE.ROCK,
    2: CHOICE.PAPER,
    3: CHOICE.SCISSORS
}

def get_computer_choice() -> CHOICE:
    return random.choice(list(CHOICE))


def get_human_choice() -> CHOICE:
    choice_number = int(input('Enter the number of your choice: '))
    return NUMBERED_CHOICES[choice_number]


def print_choices(human_choice: CHOICE, computer_choice: CHOICE) -> None:
    print(f'You chose {human_choice.value}')
    print(f'The computer chose {computer_choice.value}')


def print_options() -> None:
    print('\n'.join(f'({i}) {choice.value}' for i, choice in list(NUMBERED_CHOICES.items())))
