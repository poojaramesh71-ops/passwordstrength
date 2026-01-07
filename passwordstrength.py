def check_password_strength(password):
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    for ch in password:
        if ch.isdigit():
            has_digit = True
        if ch in special_characters:
            has_special = True

    if len(password) < 8:
        print("Weak Password: Less than 8 characters")
        return "Weak"
    elif not has_digit:
        print("Weak Password: No digit found")
        return "Weak"
    elif not has_special:
        print("Weak Password: No special character found")
        return "Weak"
    else:
        print("Strong Password: Meets all requirements")
        return "Strong"


password = input("Enter password: ")
result = check_password_strength(password)
print("Password Status:", result)