import pytest

from src.choices import get_computer_choice, CHOICE, get_human_choice, NUMBERED_CHOICES, print_choices, print_options


def test_choices__compatible():
    assert len(CHOICE) == len(NUMBERED_CHOICES)


def test_get_computer_choice():
    for _ in range(100):
        assert get_computer_choice() in CHOICE


@pytest.mark.parametrize("choice_number, choice",
    [
        (1, CHOICE.ROCK),
        (2, CHOICE.PAPER),
        (3, CHOICE.SCISSORS)
    ]
)
def test_get_human_choice(monkeypatch, choice_number, choice):
    monkeypatch.setattr('builtins.input', lambda _: choice_number)
    assert get_human_choice() == choice


def test_get_human_choice__invalid_raises(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: len(CHOICE) + 1)
    with pytest.raises(KeyError):
        get_human_choice()


@pytest.mark.parametrize("human_choice, computer_choice, stdout",
    [
        (CHOICE.ROCK, CHOICE.ROCK, 'You chose Rock\nThe computer chose Rock\n'),
        (CHOICE.ROCK, CHOICE.PAPER, 'You chose Rock\nThe computer chose Paper\n'),
        (CHOICE.ROCK, CHOICE.SCISSORS, 'You chose Rock\nThe computer chose Scissors\n'),
        (CHOICE.PAPER, CHOICE.ROCK, 'You chose Paper\nThe computer chose Rock\n'),
        (CHOICE.PAPER, CHOICE.PAPER, 'You chose Paper\nThe computer chose Paper\n'),
        (CHOICE.PAPER, CHOICE.SCISSORS, 'You chose Paper\nThe computer chose Scissors\n'),
        (CHOICE.SCISSORS, CHOICE.ROCK, 'You chose Scissors\nThe computer chose Rock\n'),
        (CHOICE.SCISSORS, CHOICE.PAPER, 'You chose Scissors\nThe computer chose Paper\n'),
        (CHOICE.SCISSORS, CHOICE.SCISSORS, 'You chose Scissors\nThe computer chose Scissors\n')
    ]
)
def test_print_choices(capsys, human_choice, computer_choice, stdout):
    print_choices(human_choice=human_choice, computer_choice=computer_choice)
    assert capsys.readouterr().out == stdout


def test_print_options(capsys):
    print_options()
    assert capsys.readouterr().out == '(1) Rock\n(2) Paper\n(3) Scissors\n'

