import hashlib
import requests
import getpass

# asks for the user to enter their password
def password_input():
    user_password = getpass.getpass("Enter your password: ") #getpass.getpass hides the password, to prevent shoulder-surfing
    return user_password

#checks if the password is compromised
def breach_check(response_text: str, target_suffix: str) -> int:
    lines = response_text.splitlines()
    for line in lines:
        returned_suffix, count_str = line.split(":")
        if returned_suffix == target_suffix:
            return int(count_str)
    return 0    

# hashes password
def password_hash(password: str):
    password_bytes = password.encode('utf-8') # encodes password into a utf-8 string
    hashed_password = hashlib.sha1(password_bytes).hexdigest().upper() # full hash is 40 characters
    prefix = hashed_password[:5] # first 5 characters
    suffix = hashed_password[5:] # remainining 35 characters
    return prefix, suffix

def fetch_breach_data(prefix: str):
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    # get url from the API
    response = requests.get(url)

    # raise an error if request fails

    if response.status_code != 200:
        raise RuntimeError(f"API request failed with status code{response}")

        # returns raw text with count of suffix
    return response.text

# -- Main Program --

# saves the password given into a global variable
password = password_input()

# returns the prefix and suffix for the hashed password
prefix, suffix = password_hash(password)

# Query API with 5-char prefix
print("Checking breach registry...")
data = fetch_breach_data(prefix)

# Returns amount of times password has been found in known breaches
count = breach_check(data, suffix)

if count > 0:
    print(f"WARNING: This password was found {count} times in known breaches.")
else:
    print("Good news: This password was not found in any known breaches!")    

