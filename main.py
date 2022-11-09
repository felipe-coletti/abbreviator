number = 1500

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

tag = ['mil', 'milhão', 'bilhão', 'trilhão']

def abbreviator(element, limit=10):
  element = str(element)
  if element.isnumeric():
    for i in range(4, len(element) + 1, 3):
      if i != 4:
        if len(element) >= i and len(element) <= (i + 2):
          element = float(element)
          element /= (10 ** (i - 1))
          index = (i - 1) / 3 - 1
          tag = tag[index]
          if element > 1:
            tag = tag.replace('ão', 'ões')
          if i == 4:
            index += 1
          if not str(element).isdecimal():
            element = '{:.0f} {}'.format(element, tag)
          else:
            element = '{:.1f} {}'.format(element, tag)
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
