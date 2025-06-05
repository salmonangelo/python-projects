
import random

MAX_LINES = 3
MAX_BETS = 100
MIN_BETS = 1
ROWS = 3
COLS = 3

symbols = {
    "A" : 2,
    "B" : 4,
    "C" : 7,
    "D" :5
}

def get_slot_machine(rows,cols,symbols):
    all_symbol = []
    for count,count_number in symbols.items():
        for _ in range(count_number):
            all_symbol.append(count)

    columns = []
    for _ in COLS:
        column = []
        duplicate_symbols = all_symbol[:]
        for _ in ROWS:
            value = random.choice(duplicate_symbols)
            duplicate_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    result = get_slot_machine()
    print(result)




def deposite():
    while True:
        deposite = input("please enter the deposite amount: $")
        if deposite.isdigit():
            deposite = int(deposite)
            if deposite > 0:
                break
            else :
                print("Enter something greater than zero!")
        else :
            print("Enter an amount in number!")
    return deposite

def get_bet_number():
    
    while True:
        lines = input(f"please enter the number of line to be betted( 1 - {MAX_LINES})")
        if lines.isdigit():
            lines = int(lines)
            if MAX_LINES+1>=lines >= 0:
                break
            else :
                print("Enter something greater than zero!")
        else :
            print("Enter in number!")
    return lines

def amount_to_bet():
    while True:
        amount = input("please enter the amount to be betted $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else :
                print("Enter something greater than zero!")
        else :
            print("Enter an amount in number!")
    return amount

def display():
    balance = deposite()
    line = get_bet_number()
    amount = amount_to_bet()
    total_amount = line * amount
    if total_amount > balance:
        print("you don't have enoungh money" )
    else:
        print("your bet is successful")
    result = get_slot_machine(ROWS,COLS,symbols)
    print_result = print_slot_machine(result)
    return None

display()