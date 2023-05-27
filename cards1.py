def is_valid_credit_card_number(number):
  """
  Checks if the given credit card number is valid.

  Args:
    number: The credit card number as a string.

  Returns:
    True if the number is valid, False otherwise.
  """

  # Check the length of the number.
  if len(number) not in (13, 15, 16):
    return False

  # Check the first digit of the number.
  if number[0] not in ('4', '5', '37', '6'):
    return False

  # Check the Luhn algorithm.
  sum = 0
  for i in range(len(number)):
    if i % 2 == 0:
      digit = int(number[i]) * 2
      if digit > 9:
        digit -= 9
      sum += digit
    else:
      sum += int(number[i])

  return sum % 10 == 0


def get_card_type(number):
  """
  Gets the card type for the given credit card number.

  Args:
    number: The credit card number as a string.

  Returns:
    The card type, or None if the number is invalid.
  """

  if not is_valid_credit_card_number(number):
    return None

  if number.startswith('4'):
    return 'Visa'
  elif number.startswith('5'):
    return 'MasterCard'
  elif number.startswith('37'):
    return 'American Express'
  elif number.startswith('6'):
    return 'Discover'

  return None


def main():
  # Get the credit card number from the user.
  number = input("Enter your credit card number: ")

  # Validate the credit card number.
  if is_valid_credit_card_number(number):
    # Get the card type.
    card_type = get_card_type(number)

    # Display the results.
    print("The credit card number is valid and is a {}.".format(card_type))
  else:
    print("The credit card number is invalid.")


if __name__ == "__main__":
  main()
