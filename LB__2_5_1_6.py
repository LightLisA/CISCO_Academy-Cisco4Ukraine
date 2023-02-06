#  2.5.1.6 LAB: Improving the Caesar cipher

text = input("Enter a text for encrypt: ")
shift_value = int(input("Enter a shift value from 1 to 25: "))

while True:
    if shift_value < 1 or shift_value > 25:
        shift_value = int(input("Enter a shift value from 1 to 25: "))
    else:
        cipher = ''
        for char in text:
            if not char.isalpha():
                code = ord(char)
            else:
                code = ord(char) + shift_value
                if char.isupper():
                    if code > ord('Z'):
                        code = (code - ord('Z')) + ord('A') - 1
                else:
                    if code > ord('z'):
                        code = (code - ord('z')) + ord('a') - 1

            cipher += chr(code)
        print(cipher)

        break
