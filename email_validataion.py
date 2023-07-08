email = input("Enter your Email: ")
k, j, d = 0, 0, 0

# Check if the email length is greater than or equal to 6
if len(email) >= 6:
    # Check if the first character of the email is an alphabet
    if email[0].isalpha():
        # Check if the email contains exactly one "@" symbol
        if email.count('@') == 1:
            # Check if the email ends with a dot (.) at index -4 or -3
            if email[-4] == '.' or email[-3] == '.':
                for i in email:
                    # Check if the email contains any spaces
                    if i.isspace():
                        k = 1
                    # Check if the character is an uppercase alphabet
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    # Check if the character is a digit
                    elif i.isdigit():
                        continue
                    # Check if the character is one of underscore, dot, or at symbol
                    elif i in ['_', '.', '@']:
                        continue
                    # If none of the above conditions are met, it's an invalid character
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print('Invalid email: contains spaces, uppercase letters, or other symbols')
                else:
                    print('Valid email')
            else:
                print('Invalid email: must contain at least one dot (.)')
        else:
            print('Invalid email: must contain exactly one @ symbol')
    else:
        print('Invalid email: must start with a letter')
else:
    print('Invalid email: too short')
