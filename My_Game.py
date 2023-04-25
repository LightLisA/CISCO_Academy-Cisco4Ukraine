from random import randrange
import math
#import cisco

print("The GUESSING game has begun")
print("----------------------------------")
print("I can guess number to 10 or to 100.")
bulleans = True


def try_to_guess_num(user_number):
    if system_number == user_number:
        print("*" * 52)
        print("**" + " " * 20 + "\(⌒ω⌒)/" + " " * 20 + "**")
        print("** Congratulations. You guessed the System number **")
        print("**" + " " * 48 + "**")
        print("*" * 52)
    else:
        find_digital_section(user_number, system_number)


def hot_cold_value(user_number):
    if abs(user_number - system_number) == 1:
        print("Very Hot! - You are very close to System number.")
    elif abs(user_number - system_number) == 2 or abs(user_number - system_number) == 3:
        print("Hot! - You are close to System number.")
    elif abs(user_number - system_number) == 4 or abs(user_number - system_number) == 5:
        print("Warm! - You almost guessed the System number.")
    elif abs(user_number - system_number) == 6 or abs(user_number - system_number) == 7:
        print("Cold! - You are too far from the System number.")
    elif abs(user_number - system_number) == 8 or abs(user_number - system_number) == 9:
        print(" Very Cold! - You are very far from the System number.")


def attempts(j):
    if 1 < j < 4:
        print("You have ", 4 - j, "attempts left.")
    else:
        last_attempt(j)


def last_attempt(k):
    if k == 4:
        print("-" * 41)
        print("--" + " " * 15 + "(︶︹︺)" + " " * 15 + "--")
        print("--  You lost :(. System number was ", system_number, "--")
        print("-" * 41)


def attempts_on_start_game(jj):
    if jj < 2:
        print("You have ", 2 - jj, "attempts left to start playing otherwise we say Goodbye")
    else:
        print("-" * 50)
        print("--" + " " * 20 + "(o_O)" + " " * 21 + "--")
        print("-- As I see, you don't want to play. Bye-e-e!!! --")
        print("-" * 50)


def inter_division(dig):
    return dig // 10


def find_digital_section(sv, uv):
    sv_1 = inter_division(sv)
    uv_1 = inter_division(uv)

    if sv_1 < uv_1:
        if uv_1 - sv_1 == 1:
            print("Sorry, but your value is on 10 less")
        elif sv_1 == 0:
            print("Sorry, but your value is in", uv_1-sv_1, "times more")
        else:
            if (uv_1/sv_1) <= 0.5:
                print("Sorry, but your value is in", math.ceil(uv_1/sv_1), "times less")
            else:
                print("Sorry, but your value is in", math.floor(uv_1/sv_1), "times less")
    elif sv_1 > uv_1:
        if sv_1 - uv_1 == 1:
            print("Sorry, but your value is on 10 more")
        elif uv_1 == 0:
            print("Sorry, but your value is in", sv_1-uv_1, "times more")
        else:
            if (uv_1/sv_1) <= 0.5:
                print("Sorry, but your value is in", math.ceil(uv_1/sv_1), "times more")
            else:
                print("Sorry, but your value is in", math.floor(uv_1/sv_1), "times more")
    else:
        hot_cold_value(sv)


for ii in range(3):
    try:
        ten_sto = int(input("Please enter 10 or 100: "))

        if ten_sto == 10 or ten_sto == 100:
            print("The system made a number. Guess it")
            if ten_sto ==10:
                system_number = randrange(1, 10)
            else:
                system_number = randrange(1, 100)

            # print("SYS NUM =", system_number)

            print("You have 5 attempts to guess the system number", end="\n")
            for i in range(5):
                try:
                    print("=====================================================")

                    if ten_sto == 10:
                        user_number = int(input("Please enter number from 1 to 10: "))
                        if user_number <= 10:
                            if system_number != user_number:
                                try_to_guess_num(user_number)
                                attempts(i)
                                bulleans = False
                            else:
                                try_to_guess_num(user_number)
                                bulleans = False
                                break
                        else:
                            print("Your number is ", user_number, ". It is out of the range. Please enter number from 1 to 10")
                            attempts(i)
                    else:
                        user_number = int(input("Please enter number from 1 to 100: "))
                        if user_number <= 100:
                            if system_number != user_number:
                                try_to_guess_num(user_number)
                                attempts(i)
                                bulleans = False
                            else:
                                try_to_guess_num(user_number)
                                bulleans = False
                                break
                        else:
                            print("Your number is ", user_number, ". It is out of the range. Please enter number from 1 to 100")
                            attempts(i)
                except ValueError:
                    print("Empty value. Your number should be between 1 and 10")
                    attempts(i)
        else:
            attempts_on_start_game(ii)

    except ValueError:
        print("Empty value.")
        attempts_on_start_game(ii)

    if bulleans:
        continue
    else:
        break
