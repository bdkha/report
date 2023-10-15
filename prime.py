def is_prime(n):
  """
  Kiểm tra xem một số nguyên tố là số nguyên tố hay không.

  Args:
    n: Một số nguyên dương.

  Returns:
    True nếu n là số nguyên tố, False nếu không.
  """

  if n <= 1:
    return False

  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False

  return True

def find_prime(n_digits):
  """
  Tìm một số nguyên tố có n_digits chữ số.

  Args:
    n_digits: Số lượng chữ số của số nguyên tố cần tìm.

  Returns:
    Một số nguyên tố có n_digits chữ số.
  """

  n = 10**(n_digits - 1)
  while not is_prime(n):
    n += 1

  return n

print(find_prime(30))