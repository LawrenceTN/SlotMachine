# Welcome to the casino, where you win nothing and lose everything.
# Credit to tech with tim

import random

#GLOBAL VARIABLES/DICTS
MIN_BET = 5
MAX_BET = 20
ROWS = 3
COLS = 3

SYMBOL_COUNT = { # how much they occur in our machine
    "@": 2,
    "#": 4,
    "%": 6,
    "&": 8
}

SYMBOLS_VALUES = { # how much they're worth 
    "@": 5, 
    "#": 4,
    "%": 3,
    "&": 2
}

def repeat(balance): # loop
    balance, bet = get_bet(balance)
    if bet == 0:
        return balance
    print(f"\nBet: {bet}\nBalance: {balance}")
    slots = play(ROWS, COLS, SYMBOL_COUNT)
    print_screen(slots)
    winnings = check_result(slots, bet, SYMBOLS_VALUES)
    balance += winnings
    print(f"You won ${winnings}. Your balance is now ${balance}")
    return balance

def play(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #key=symbol / value=symbol_count
        for _ in range(symbol_count): 
            all_symbols.append(symbol) # adding each symbol 'count' amount of times into all_symbols list

    # pick a random value for each row 
    columns = []
    for _ in range(cols): # 3 times
        column = []
        current_symbols = all_symbols[:] # we don't reference, we want a copy of all symbols
        for _ in range(rows): # 3 times
            value = random.choice(current_symbols)
            current_symbols.remove(value) 
            column.append(value) # results in 3 values to column

        columns.append(column)
    
    return columns

def print_screen(columns):
    for row in range(3):
        for i, column in enumerate(columns): # retrieve element in the row of each column
            if i != len(columns) - 1: # if not at the end, print the element of the column followed by '|' to divide columns
                print(column[row], end=" | ")
            else: # no divider, because at the end
                print(column[row])


def deposit(): # how many chips you want to buy
    while True:
        amount = input("How many chips you like to buy? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    
    return amount


def get_bet(balance): # get the bet from user
    while True:
        bet = input("Place your bets: \nA) [MIN]\nB) [10]\nC) [MAX]\nQ) [QUIT]\n")
        
        if bet.isalpha():
            bet = bet.lower()
            match bet:
                case 'a':
                    if balance >= MIN_BET:
                        balance -= MIN_BET
                        bet = MIN_BET
                        break
                    else:
                        print("Not enough coins!")
                case 'b':
                        if balance >= 10:
                            balance -= 10
                            bet = 10
                            break
                        else:
                            print("Not enough coins!")
                case 'c': 
                    if balance >= MAX_BET:
                        balance -= MAX_BET
                        bet = MAX_BET
                        break
                    else:
                        print("Not enough coins!")
                case 'q':
                        bet = 0
                        break
                case _:
                    print("Invalid entry")
        
        else:
            print("Invalid choice, try again.")
    
    return balance, bet   

def check_result(columns, bet, values):
    winnings = 0
    for row in range(3):
        symbol = columns[0][row] # obtain the first symbol of each row of the first column
        for column in columns:
            symbol_to_check = column[row] #obtain symbol to check
            if symbol != symbol_to_check: # compare first symbol in row to the rest of the symbols in the row
                break
        else: #for-else = if no break occurs in the for loop, else executes after for loop completes
                winnings += values[symbol] * bet # winnings += symbol value from dict * bet made

    return winnings

def main():
    balance = deposit()
    while True:
        balance = repeat(balance)
        if balance == 0:
            print("Game over! Better luck next time")
            break
        answer = input("Press enter to play again or 'q' to quit ")
        if (answer == 'q'):
            break
    print("Thank you for playing!")

main()