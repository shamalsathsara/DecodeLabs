import random
import string

print("=" * 50)
print("        RANDOM PASSWORD GENERATOR")
print("=" * 50)

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password must be at least 8 characters long.\n")
            continue
        break

    except ValueError:
        print("Please enter a valid number.\n")

# Character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special = "!@#$%^&*()_-+=<>?"

# Ensure password contains at least one character from each category
password = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits),
    random.choice(special)
]

# Fill remaining characters
all_characters = lowercase + uppercase + digits + special

for _ in range(length - 4):
    password.append(random.choice(all_characters))

# Shuffle for randomness
random.shuffle(password)

# Convert list to string
final_password = "".join(password)

print("\nGenerated Password:")
print(final_password)
print("\nPassword generated successfully!")