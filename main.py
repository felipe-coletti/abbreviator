number = 1000

limit = 500


def abbreviator(element, limit):
  if element.isdigit():
    if len(element) >= 1000 and len(element) < 1000000:
      element /= 1000
  else:
    for i in range(limit, limit + 4):
      element[i] = "."
    for i in range(limit + 4, len(element)):
      element.remove[i]

