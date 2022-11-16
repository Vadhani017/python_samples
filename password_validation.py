# password validation and storing
import re

password_dict = {}
while True:
    username = input("Enter the application name for which password is being stored: ")
    print("The password length must be greater than 8 and less than 15")
    print("The password must contain one digit, one upper case alphabet, one lower case letter and one special "
          "characters")
    password = input("Enter the password: ")
    total_char = len(password)
    if (total_char > 7) and (total_char < 16):
        num = re.search(r'\d', password)
        special_char = re.search(r'(#|\*|@|!|\$|%|^|&|\(|\))', password)
        capital_letter = re.search(r'[A-Z]', password)
        small_letter = re.search(r"[a-z]", password)
        if num:
            if special_char:
                if capital_letter:
                    if small_letter:
                        print("Your password is in correct format and it is saved in your dictionary")
                        password_dict[username] = password
                    else:
                        print("There is no lower case letter in your password. Do try with correction again")
                        continue
                else:
                    print("There is no upper case letter in your password. Do try with correction again")
                    continue
            else:
                print("There is no special character in your password. Do try with correction again")
                continue
        else:
            print("There is numerical character in your password. Do try with correction again")
            continue
    elif total_char < 7:
        print("The number of character in your password is less. Try to give at least 8 characters.")
        continue
    else:
        print("The number of character in your password is more. Try to give less than 15 characters. ")
        continue

    response1 = input("Do you want to continue storing passwords in dictionary, type s else type n: ")
    if response1.upper() == 'S':
        continue
    elif response1.upper() == 'N':
        print(password_dict)
        break
