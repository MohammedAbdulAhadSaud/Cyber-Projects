import re

def password_strength_checker(password):
    # Initialize strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&]', password) is not None

    # Count the number of criteria met
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria,
                        number_criteria, special_char_criteria])

    # Determine password strength
    if criteria_met < 3:
        strength = "Weak"
        advice = get_advice(password)
    elif criteria_met == 3:
        strength = "Moderate"
        advice = "Consider adding more variety to your password for better security."
    else:
        strength = "Strong"
        advice = "Your password is strong! Keep it safe."

    return strength, advice

def get_advice(password):
    advice = []
    
    if len(password) < 8:
        advice.append("Increase the length of your password to at least 8 characters.")
    
    if not re.search(r'[A-Z]', password):
        advice.append("Include at least one uppercase letter (A-Z).")
    
    if not re.search(r'[a-z]', password):
        advice.append("Include at least one lowercase letter (a-z).")
    
    if not re.search(r'[0-9]', password):
        advice.append("Include at least one number (0-9).")
    
    if not re.search(r'[@$!%*?&]', password):
        advice.append("Include at least one special character (e.g., @$!%*?&).")
    
    if len(password) < 12:
        advice.append("Consider making your password longer (12+ characters) for better security.")
    
    return " ".join(advice)

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength, advice = password_strength_checker(password)
    print(f"Password strength: {strength}")
    print(f"Advice: {advice}")
