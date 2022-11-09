number = 1000

limit = 500


def abbreviator(element, limit):
  index = 4
  if element.isdigit():
    if len(element) >= index and len(element) <= (index + 2):
      element /= (10 ** (index - 1))
      element = "{:,2f} mil".format(element)
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
