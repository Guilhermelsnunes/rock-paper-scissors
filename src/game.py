from src.choices import (
    print_options,
    get_computer_choice,
    get_human_choice,
    print_choices
)
from src.logic import get_outcome

if __name__ == '__main__':
    print_options()
    computer_choice = get_computer_choice()
    print("The computer has chosen!")
    human_choice = get_human_choice()
    print_choices(human_choice=human_choice, computer_choice=computer_choice)
    print(get_outcome(human_choice=human_choice, computer_choice=computer_choice).value)
