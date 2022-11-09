number = 1000

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

limit = 10

tag = ['mil', 'mil', 'milhão', 'milhões', 'bilhão', 'bilhões', 'trilhão', 'trilhões']


def abbreviator(element, limit=10):
  element = str(element)
  if element.isnumeric():
    for i in range(4, len(element) + 1, 3):
      if i != 4:
        if len(element) >= i and len(element) <= (i + 2):
          element = int(element)
          element /= (10 ** (i - 1))
          if element < 2:
            index = i - 5
          else:
            index = i - 4
          if i == 4:
            index += 1
          if not str(element).isdecimal():
            element = '{:.0f} {}'.format(element, tag[index])
          else:
            element = '{:.1f} {}'.format(element, tag[index])
  else:
    if limit > len(element) - 1:
      limit = len(element) - 1
    while element[limit] == ' ' or element[limit] == '.':
      limit -= 1
    while element[limit].isalnum() and element[limit + 1] != ' ' and element[limit + 1] != '.':
      limit += 1
    while len(element) - 1 > limit:
      element = element[:-1]
    while element[len(element) - 1] == '.':
      element = element[:-1]
    element += '...'
  return element


print(abbreviator(number))

print(abbreviator(text))
