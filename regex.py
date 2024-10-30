import re

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+(\.\w+)?$"
    return re.match(pattern, email) is not None

# Test
print(is_valid_email("example@domain.com"))  # Output: True
print(is_valid_email("invalid-email")) 