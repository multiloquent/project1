import csv
from pathlib import Path


def start_record() -> None:
    """
    Checks if voter_id_record.csv exists. If it does not, it is created.
    """
    file_path = Path('voter_id_record')
    if not file_path.exists():
        with open('voter_id_record', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Vote'])
        print('Record created')
    else:
        print('Record found')


def voter_fraud_detection(i_d: str) -> bool:
    """
    Takes i_d from input in gui.py and evaluates a boolean value from comparisons of i_d to
    voter_id_record.csv. Returns True or False
    """
    with open('voter_id_record', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if i_d == row[0]:
                print('Voter found as prior voter')
                fraud = True
                break
            else:
                fraud = False
        if fraud is False:
            print('Voter not found as prior voter')
        return fraud


def submit_logic(i_d: str, vote: str, warning: callable, un_warning: callable,
                 incorrect_input: callable, no_selection: callable,
                 count_update: callable) -> None:
    """
    Main logic of program. Based on truth values from functions adds voter IDs and votes to
    voter_id_record.csv. Uses methods, as parameters, from gui.py to alert user to user error.
    Returns None.
    """
    if correct_input(i_d) is True and erm_radio_check_much(vote) is True:
        fraud = voter_fraud_detection(i_d)
        if fraud is True:
            warning()
            print('Voter already in registry')
        elif fraud is False and erm_radio_check_much(vote) is True:
            with open('voter_id_record', mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([i_d, vote])
            un_warning()
            print('Voter added to registry')
    else:
        if correct_input(i_d) is False:
            incorrect_input()
            print('User entered non-numeric value')
        elif erm_radio_check_much(vote) is False:
            no_selection()
            print('User did not select a candidate')
    print('logic ended, waiting for next submit')
    count_update()


def correct_input(user_input: str) -> bool:
    """
    Checks user_input against range of ASCII values to determine if user input is acceptable.
    Returns True or False.
    """
    for char in user_input:
        ascii_value = ord(char)
        if ascii_value < 48 or ascii_value > 57:
            return False
    return True


def erm_radio_check_much(vote: str) -> bool:
    """
    Checks if parameter vote is 'Neither'. Returns True or False.
    """
    if vote == 'Neither':
        return False
    else:
        return True


def count() -> list:
    """
    Counts votes from data in voter_id_record.csv. Returns a list of votes.
    """
    counter = [0, 0]
    with open('voter_id_record', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[1] == 'John McCain':
                counter[0] += 1
            elif row[1] == 'Barrack Obama':
                counter[1] += 1
    return counter
