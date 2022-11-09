number = 1000

limit = 500


def abbreviator(element, limit):
  if element.isdigit():
    if len(element) >= 4 and len(element) <= 6:
      element /= 1000
      element = "{:,2f} mil".format(element)
  else:
    while element(limit) == '':
      limit -= 1
    while element(limit).isalpha and element(limit + 1):
      limit += 1
    for i in range(limit, limit + 4):
      element[i] = '.'
    for i in range(limit + 4, len(element)):
      element.remove[i]
  return element


print(abbreviator(number))
