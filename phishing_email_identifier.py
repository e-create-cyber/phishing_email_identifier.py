# List of known phishing email keywords
phishing_keywords = [
    "password", "login", "secure", "urgent",
    "click here", "view", "confirm",
    "verify email", "view order status"
]

# Prompt the user to paste the email content
email = input("Paste the email content: ")

# Check if any phishing keyword is in the email content
if any(keyword.lower() in email.lower() for keyword in phishing_keywords):
    print("Beware! This is a phishing email.")
else:
    print("This email does not appear to be from a known phisher.")
