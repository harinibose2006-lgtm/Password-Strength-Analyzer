import re
import secrets
import string
def check_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[@#$!%&*]", password):
        score += 1
    print("\n----- PASSWORD ANALYSIS -----")
    if score <= 2:
        print("Password Strength: WEAK")
        print("Suggestion: Use a longer password with mixed characters.")
    elif score <= 4:
        print("Password Strength: MEDIUM")
        print("Suggestion: Add numbers and special characters.")
    else:
        print("Password Strength: STRONG")
        print("Your password meets all basic security checks!")
def generate_password():
    characters = string.ascii_letters + string.digits + "@#$!%&*"
    password = ''.join(secrets.choice(characters) for _ in range(14))
    return password
print("================================")
print("     PASSWORD STRENGTH ANALYZER")
print("================================")
password = input("Enter your password: ")
check_password(password)
print("\nSuggested Strong Password:")
print(generate_password())
print("\nAnalysis Completed!")