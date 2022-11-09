number = 1000

limit = 500


def abbreviator(element, limit):
  if element.isdigit():
    if len(element) >= 4 and len(element) < 7:
      element /= 1000
      element = "{:,2f} mil".format(element)
  else:
    for i in range(limit, limit + 4):
      element[i] = '.'
    for i in range(limit + 4, len(element)):
      element.remove[i]

