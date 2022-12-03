import random
# Welcome to the casino of Lawrence, where you win nothing and lose everything.
# credit to tech with tim

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
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row])


def deposit():
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


def get_bet(balance):
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
    for line in range(3):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
                winnings += values[symbol] * bet

    return winnings

def main():
    balance = deposit()
    balance, bet = get_bet(balance)
    print(f"\nYour bet is: {bet} Your balance is: {balance}.")

    slots = play(ROWS, COLS, SYMBOL_COUNT)
    print_screen(slots)
    winnings = check_result(slots, bet, SYMBOLS_VALUES)
    balance += winnings
    print(f"You won ${winnings}. Your balance is now {balance}")
    

main()