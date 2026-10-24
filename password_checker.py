
import re
import getpass

COMMON_PASSWORDS = {
    "password", "password123", "123456", "12345678",
    "qwerty", "admin", "letmein", "welcome"
}


def check_password(password):
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Prefer 12 or more characters.")

    # Check character variety
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Consider special characters.")

    # Check common passwords
    if password.lower() in COMMON_PASSWORDS:
        score = 0
        suggestions.append("Avoid common passwords.")

    # Identify simple repeated or sequential patterns
    if re.search(r"(.)\1{3,}", password):
        score = max(0, score - 2)
        suggestions.append("Avoid repeating the same character.")

    if re.search(
        r"1234|2345|3456|4567|5678|6789|abcd|qwerty",
        password.lower()
    ):
        score = max(0, score - 2)
        suggestions.append("Avoid predictable sequences.")

    # Assign a basic rating
    if password.lower() in COMMON_PASSWORDS or len(password) < 8:
        rating = "Weak"
    elif score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Medium"
    elif score == 5:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return rating, suggestions


def main():
    print("=" * 40)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 40)
    print("Your password is checked locally.")
    print("It will not be saved by this program.\n")

    password = getpass.getpass("Enter a test password: ")

    if not password:
        print("Error: Password cannot be empty.")
        return

    rating, suggestions = check_password(password)

    print(f"\nStrength rating: {rating}")

    if suggestions:
        print("\nSuggestions:")
        for item in suggestions:
            print(f"- {item}")
    else:
        print("Good character variety and length!")

    print("\nNote: This is an educational checker,")
    print("not a guarantee against password attacks.")


if __name__ == "__main__":
    main()
