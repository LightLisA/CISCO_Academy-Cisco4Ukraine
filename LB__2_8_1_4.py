def read_int(prompt, min, max):
    print(prompt)

    while True:
        try:
            user_num = int(input())
            if -10 <= int(user_num) <= 10:
                return user_num
            else:
                print("Error: the value is not within permitted range (", str(min), "..", str(max), ")")
                continue
        except ValueError:
            print("Error: wrong input")
            continue


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
