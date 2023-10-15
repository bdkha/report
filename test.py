import math

def gcd(a, b):
  """
  Calculates the greatest common divisor of two numbers.

  Args:
    a: An integer.
    b: An integer.

  Returns:
    The greatest common divisor of a and b.
  """

  while b > 0:
    a, b = b, a % b
  return a

def calculate_modular_inverse(a, m):
  """
  Calculates the modular inverse of a modulo m.

  Args:
    a: An integer.
    m: An integer.

  Returns:
    The modular inverse of a modulo m, or None if no such inverse exists.
  """

  for i in range(1, m):
    if (a * i) % m == 1:
      return i
  return None

def calculate_rsa_public_key(p, q, e):
  """
  Calculates the RSA public key from the large numbers p, q, and e.

  Args:
    p: A large prime number.
    q: A large prime number.
    e: A positive integer greater than 1 and relatively prime to (p-1)(q-1).

  Returns:
    A tuple containing the RSA public key (n, e), where n = p * q.
  """

  n = p * q
  return (n, e)

def calculate_rsa_private_key(p, q, e):
  """
  Calculates the RSA private key from the large numbers p, q, and e.

  Args:
    p: A large prime number.
    q: A large prime number.
    e: A positive integer greater than 1 and relatively prime to (p-1)(q-1).

  Returns:
    The RSA private key, which is an integer d such that (d * e) % (p-1)(q-1) == 1.
  """

  r = (p - 1) * (q - 1)
  d = calculate_modular_inverse(e, r)
  if d is None:
    raise ValueError("No modular inverse exists for e modulo (p-1)(q-1)")
  return d

def main():
  # Get the large numbers p, q, and e from the user.
  p = int(input("Enter the large prime number p: "))
  q = int(input("Enter the large prime number q: "))
  e = int(input("Enter the public exponent e: "))

  # Calculate the RSA public key.
  public_key = calculate_rsa_public_key(p, q, e)

  # Calculate the RSA private key.
  private_key = calculate_rsa_private_key(p, q, e)

  # Print the RSA public key and private key.
  print("RSA public key:", public_key)
  print("RSA private key:", private_key)

if __name__ == "__main__":
  main()