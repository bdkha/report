import math

def encrypt_rsa(message, public_key, private_key):
  """
  Encrypts a message using RSA.

  Args:
    message: The message to encrypt.
    public_key: The RSA public key, which is a tuple (n, e).
    private_key: The RSA private key, which is an integer d.

  Returns:
    The encrypted message.
  """

  n, e = public_key
  d = private_key

  # Convert the message to a number.
  message_number = int.from_bytes(message, 'big')

  # Encrypt the message number using the public key.
  encrypted_message_number = (message_number ** e) % n

  # Convert the encrypted message number back to a byte string.
  encrypted_message = encrypted_message_number.to_bytes((encrypted_message_number.bit_length() + 7) // 8, 'big')

  return encrypted_message

def main():
  # Get the large numbers p, q, e, and d from the user.
  p = int(input("Enter the large prime number p: "))
  q = int(input("Enter the large prime number q: "))
  e = int(input("Enter the public exponent e: "))
  d = int(input("Enter the private key d: "))

  # Get the message to encrypt.
  message = input("Enter the message to encrypt: ")

  # Encrypt the message.
  encrypted_message = encrypt_rsa(message, (p * q, e), d)

  # Print the encrypted message.
  print("Encrypted message:", encrypted_message)

if __name__ == "__main__":
  main()