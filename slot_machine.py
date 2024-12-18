import random
import os
import time


def welcome():
    input('''          Hello welcome, this is a slot machine game
          you will start with $1000 dollars and can bet however much you want at a time
          run out of money and you lose, try and make the most money you can
          press enter to continue >> ''')
    time.sleep(0.5)
    os.system("cls")

def main_menu(account):
    options = ["b", "s", "e", "h"]
    select = input(f'''                      Main Menu
            You have ${account} in your account
                   _______________
b.) change you bet
s.) start the round
e.) exit the game early
h.) rules of the game
                   >> ''')
    if select not in options:
        raise ValueError
    else:
        return select

def exit_message(max_account):
    print("Thank you for playing!")
    print(f"Your high score was {max_account}")
    time.sleep(1)
    os.system("cls")

def select_b(account):
    invalid_bet = True
    while invalid_bet:
        try:
            bet = input("What would you like to set your bet to? $")
            bet = int(bet)
            if bet > account or bet <= 0:
                raise ValueError
        except ValueError:
            print("please make sure you have the funds in your account to bet this amount")
            pass
        try:
            if int(bet) <= account and int(bet) > 0:
                break
        except ValueError:
            print("please make sure what you inputed was a number")
    print(f"Your bet has been changed to ${bet}")
    time.sleep(1)
    os.system("cls")
    return bet

def select_s(account, bet):
    os.system("cls")
    if account - bet < 0:
        input('''                 You do not have enough money to start a game, please change your bet
                                    press enter to continue >> ''')
        time.sleep(0.4)
        os.system("cls")
        return account
    options = ["!", "@", "#", "$", "&", "*"]
    input('''You are about to start
          press enter to spin the wheel >> ''')
    spin1 = random.choice(options)
    spin2 = random.choice(options)
    spin3 = random.choice(options)
    print(f"{spin1}|{spin2}|{spin3}")
    if spin1 == spin2 and spin2 == spin3:
        if spin1 == "$":
            bet = bet * 100
            input('''                 You have won the jackpot, 100x your bet
                  press enter to continue >> ''')
        elif spin1 == "#":
            bet = bet * 10
            input('''                 You have won the medium jackpot, 10x your bet
                  press enter to continue >> ''')
        else:
            bet = bet * 2
            input('''                 You have won the small jackpot, 2x your money
                  press enter to continue >> ''')
        time.sleep(0.5)
        os.system("cls")
        return (account + bet)
    
    elif spin1 == spin2 or spin2 == spin3 or spin1 == spin2:
        input('''                 You got two in a row, you make your money back
              press enter to continue >> ''')
        time.sleep(0.5)
        os.system("cls")
        return account
    else:
        input('''                 You lost, your bet is being subtracted from your account
              press enter to continue >> ''')
        time.sleep(0.5)
        os.system("cls")
        return (account - bet)


def select_h():
    input(f'''
the rules are pretty simple:
You will pick how much money you want to gamble from your account on the spin
the payouts are as follows:
three $'s: 100x your bet
three #"s 10x your bet
three of anything else will double your bet
if you get two in a row of something you will get your money back
                  press enter to continue >>''')
    os.system("cls")

def record(account, max_account):
    if account > max_account:
        return account
    else:
        return max_account
    
def app():
    os.system("cls")
    account = 1000
    max_account = 1000
    welcome()
    play = True
    while play:
        max_account = record(account, max_account)
        if account == 0:
            print("You ran out of money and have lost, better luck next time")
            ans = input("Press enter to play again, enter any key and press enter to exit the game >> ")
            if ans == "":
                account = 1000
                pass
            else:
                break
        
        loop = True
        while loop:
            try:
                select = main_menu(account)
                loop = False
            except ValueError:
                print("please select one of the options given")
                time.sleep(0.7)
                os.system("cls")
                loop = True
        if select == "b":
            bet = select_b(account)
        try:
            if select == "s":
                account = select_s(account, bet)
        except UnboundLocalError:
            print("Please create a bet amount before you start a game")
            time.sleep(0.8)
            os.system("cls")
            pass
        if select == "e":
            time.sleep(0.5)
            os.system("cls")
            break
        elif select == "h":
            select_h()
    exit_message(max_account)


if __name__ == "__main__":
    app()
