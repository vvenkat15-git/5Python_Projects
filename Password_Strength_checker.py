"Password Strength checker using Python"
def check_password_strength(password):
    #define criteria
    length = len(password) >= 8
    contain_upper = any(char.isupper() for char in password)
    contain_lower = any(char.islower() for char in password)
    contain_digit = any(char.isdigit() for char in password)
    contain_spec_char = any(char in '!@#$%^&*?><(),//' for char in password)

    if length and contain_upper and contain_lower and contain_digit and contain_spec_char:
        return "Strong Password"
    elif length and(contain_upper or contain_lower) and contain_digit:
        return "Moderate Password"
    else:
        return "Weak Password, Please change it immediately"

password = input("Enter your passowrd here = ")

strength = check_password_strength(password)
print("")
print("Password Strength = ", strength)

'_________________________________________________________________________________________________________________________________'

#updated code:
import string
import getpass

def check_pwd():
    password = getpass.getpass("Enter Password: ")
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count =0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1
    
    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        stregth += 1
    
    if strength == 1:
        remarks = "Very Bad Password !!! Change ASAP"
    elif strength == 2:
        remarks = "Not a Good Password !!! Change ASAP"
    elif strength == 3:
        remarks = "It's a Weak Password, Consider Changing"
    elif strength == 4:
        remarks  = "It's a Hard Password, But can be better"
    elif strength == 5:
        remarks = "A very strong password"
        
    print("Your password has : ")
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")

    print(f"Password Strength: {strength}")
    print(f"Hint:{remarks}")

def ask_pwd(another_pwd = False):
    valid = False
    if another_pwd:
        choice = input("Do you want to enter another Pwd (y/n):")
    else:
        choice = input("Do you want to check pwd (y/n):")
    
    while not valid:
        if choice.lower() == 'y':
            return True
        elif choice.lower == 'n':
            return False
        else:
            print("Invalid, Try Again")
            
if __name__ == "__main__":
    print('+++ Welcome to Password Strength Checker +++')
    ask_pw = ask_pwd()
    while check_pwd:
        check_pwd()
        ask_pw = ask_pwd(True)


