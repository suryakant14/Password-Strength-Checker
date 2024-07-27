import hashlib
import time
import math

def check_length(password):
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters."
    else:
        return "Password length is sufficient."

def check_complexity(password):
    if not any(char.isupper() for char in password):
        return "Password should have at least one uppercase letter."
    elif not any(char.islower() for char in password):
        return "Password should have at least one lowercase letter."
    elif not any(char.isdigit() for char in password):
        return "Password should have at least one digit."
    elif not any(char in "!@#$%^&*()_+-=" for char in password):
        return "Password should have at least one special character."
    else:
        return "Password complexity is sufficient."

def check_uniqueness(password):
    common_passwords = ["password123", "qwerty", "letmein", "dragonball"]
    if password in common_passwords:
        return "Password is too common. Please choose a more unique password."
    else:
        return "Password uniqueness is sufficient."

def calculate_entropy(password):
    entropy = 0
    for char in password:
        entropy += -math.log(len(password), 2)
    return entropy

def estimate_cracking_time(password):
    cracking_speed = 100000
    cracking_time = len(password) / cracking_speed
    return cracking_time

def assess_password_strength(password):
    length_result = check_length(password)
    complexity_result = check_complexity(password)
    uniqueness_result = check_uniqueness(password)
    entropy_result = calculate_entropy(password)
    cracking_time_result = estimate_cracking_time(password)
    
    if length_result != "Password length is sufficient.":
        return length_result
    elif complexity_result != "Password complexity is sufficient.":
        return complexity_result
    elif uniqueness_result != "Password uniqueness is sufficient.":
        return uniqueness_result
    elif entropy_result < 128:
        return "Password entropy is too low. Please choose a more complex password."
    elif cracking_time_result < 60:
        return "Password cracking time is too short. Please choose a longer password."
    else:
        return "Password strength is sufficient."

while True:
    password = input("Enter a password: ")
    result = assess_password_strength(password)
    if result == "Password strength is sufficient.":
        print("Strong password accepted!")
        break
    else:
        print(result)
