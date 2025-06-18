
import re

def check_strength(password):
    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        print("❌ Password must be at least 8 characters.")

    # Check for lowercase letters
    if re.search("[a-z]", password):
        score += 1
    else:
        print("❌ Add lowercase letters.")

    # Check for uppercase letters
    if re.search("[A-Z]", password):
        score += 1
    else:
        print("❌ Add uppercase letters.")

    # Check for digits
    if re.search("[0-9]", password):
        score += 1
    else:
        print("❌ Add numbers.")

    # Check for special characters
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        print("❌ Add special characters.")

    # Final result
    if score == 5:
        print("✅ Your password is Strong!")
    elif score >= 3:
        print("🟡 Your password is Medium.")
    else:
        print("🔴 Your password is Weak.")

# Run the checker
print("🔐 Welcome to the Password Strength Checker!")
user_password = input("Enter your password: ")
check_strength(user_password)
