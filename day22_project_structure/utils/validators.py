import re

def is_valid_email(email):
    pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
    return re.fullmatch(pattern, email) is not None
