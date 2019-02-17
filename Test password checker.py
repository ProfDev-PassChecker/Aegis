import re
def password_check(password):

    #Checks length of input
    lengthCheck = len(password) < 8

    #Checks if it includes a numeric value
    digitCheck = re.search(r"\d", password) is None

    #Checks for an uppercase letter
    uppercaseCheck = re.search(r"[A-Z]", password) is None

    #Checks for a lowercasse letter
    lowercaseCheck = re.search(r"[a-z]", password) is None

    #Checks if a symbol is used
    symbolCheck = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password) is None

    #Final check for if the password is strong
    passwordCheck = not ( lengthCheck or digitCheck or uppercaseCheck or lowercaseCheck or symbolCheck )

    return {
        'Strong password: ' : passwordCheck,
        'Suitable length: ' : lengthCheck,
        'Includes a number: ' : digitCheck,
        'Includes an uppercase letter: ' : uppercaseCheck,
        'Includes a lowercase letter: ' : lowercaseCheck,
        'Includes a symbol: ' : symbolCheck,
    }
def main(password):
    password = input("Enter your password: ")
    result =password_check(password)
    print (result)

    
    
main(main)