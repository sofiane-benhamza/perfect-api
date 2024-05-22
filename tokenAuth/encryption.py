import base64
import hashlib
from cryptography.fernet import Fernet

def hash(input_string):
    """
    Hashes a given string using SHA-256 and returns the hexadecimal representation of the hash.

    Parameters:
    input_string (str): The string to be hashed.

    Returns:
    str: The hexadecimal representation of the hash.
    """
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

    
def generate_key(custom_string):
    # Hash the string using SHA256 to ensure it's 32 bytes
    hashed = hashlib.sha256(custom_string.encode()).digest()
    # Base64 encode the hashed result to make it URL-safe
    return base64.urlsafe_b64encode(hashed)

def encrypt(message, key):
    key = generate_key(key)
    fernet = Fernet(key)
    return fernet.encrypt(message.encode()).decode()

def decrypt(token, key):
    key = generate_key(key)
    fernet = Fernet(key)
    return fernet.decrypt(token.encode()).decode()