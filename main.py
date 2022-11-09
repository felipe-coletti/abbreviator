number = 1000

limit = 500

tag = ['mil', 'milhão', 'bilhão', 'trilhão']


def abbreviator(element, limit):
  if element.isdigit():
    for i in range(4, len(element), 3):
      if len(element) >= i and len(element) <= (i + 2):
        element /= (10 ** (i - 1))
        element = '{:,2f} mil'.format(element)
  else:
    while element(limit) == '':
      limit -= 1
    while element(limit).isalpha and element(limit + 1):
      limit += 1
    for i in range(limit + 1, limit + 4):
      element[i] = '.'
    for i in range(limit + 4, len(element)):
      element.remove[i]
  return element


print(abbreviator(number))
