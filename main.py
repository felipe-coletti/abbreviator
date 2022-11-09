number = 1000

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

limit = 500

tag = ['mil', 'mil', 'milhão', 'milhões', 'bilhão', 'bilhões', 'trilhão', 'trilhões']


def abbreviator(element, limit):
  if element.isdigit():
    for i in range(4, len(element), 3):
      if len(element) != 4:
        if len(element) >= i and len(element) <= (i + 2):
          element /= (10 ** (i - 1))
          if element < 2:
            index = i - 5
          else:
            index = i - 4
          if not element.isdecimal():
            element = '{:.0f} {}'.format(element, tag[index])
          else:
            element = '{:.1f} {}'.format(element, tag[index])
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

print(abbreviator(text))
