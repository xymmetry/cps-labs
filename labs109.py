#Marc David

def ryerson_letter_grade(pct):
  if pct >= 90:
    return 'A+'
  elif pct >= 85:
    return 'A'
  elif pct >= 80:
    return 'A-'
  elif pct >= 77:
    return 'B+'
  elif pct >= 73:
    return 'B'
  elif pct >= 70:
    return 'B-'
  elif pct >= 67:
    return 'C+'
  elif pct >= 63:
    return 'C'
  elif pct >= 60:
    return 'C-'
  elif pct >= 57:
    return 'D+'
  elif pct >= 53:
    return 'D'
  elif pct >= 50:
    return 'D-'
  else:
    return 'F'

def riffle(items, out = True):
  shuffled = []
  b = len(items)
  half = b//2
  first = items[:half]
  second = items[half:]
  i = 0
  while i < half:
    if out==True:
      shuffled.append(first[i])
      shuffled.append(second[i])
      i+=1
    else:
      shuffled.append(second[i])
      shuffled.append(first[i])
      i+=1
  return shuffled

def expand_intervals(interval):
  exp = []
  com = ','
  mns = '-'
  for n in interval.split(com):
    if mns not in n:
      exp.append(int(n))
    else:
      x, y = map(int, n.split(mns))
      exp+= range(x, y+1)
  else:
    return exp


def reverse_vowels(text):
  vowels = ('aeiouAEIOU')
  text = list(text)
  x = 0
  y = len(text) - 1
  while x < y:
    while (text[x] not in vowels and x < min(len(text) - 1, y)):
      x += 1
    while (text[y] not in vowels and y > max(0,x)):
      y -= 1
    if text[x].isupper() and text[y].islower():
      text[x] = text[x].lower()
      text[y] = text[y].upper()
    elif text[y].isupper() and text[x].islower():
      text[y] = text[y].lower()
      text[x] = text[x].upper()
    text[x], text[y] = text[y], text[x]
    x +=1
    y -=1
  return ''.join(text)


def only_odd_digits(n):
  if n % 2 == 0:
    return 'False'
  digits = [int(q) for q in str(n)]
  if any(n % 2 == 0 for n in digits):
    return 'False'
  else: 
    return 'True'

def first_preceded_by_smaller(items, k=1):
  for i in range(1, len(items)):
    count = 0
    for j in range(0,i):
      if items[j] < items[i]:
        count += 1
      if count == k:
        return items[i]
      else:
        pass
  return None

def is_ascending(items):
  if len(set(items)) < len(items):
    return 'False'
  x = 0
  i = 1
  while i < len(items):
    if items[i] < items[i-1]:
      x=1
    i+=1
  if not x:
    return 'True'
  else:
    return 'False'

def disemvowel(text):
  import re
  ne = re.sub('[y]+[aeiou]+[y]','',text)
  nex =  re.sub('[y]+[aeiou]','',ne)
  newtxt = re.sub('[aeiou]+[y]','',nex)
  vowel = set('AEIOU')
  final = [let for let in newtxt if let.upper() not in vowel]
  return ''.join(final)

def iterated_remove_pairs(items):
  listo = []
  for x in items:
    if listo and x == listo[-1]: 
      listo.pop()
    else:
      listo.append(x)
  return listo

def double_until_all_digits(n, count = 1000):
  checker = {0,1,2,3,4,5,6,7,8,9}
  while count > 0:
    checkthis = set([int(x) for x in str(n)])
    if checker.issubset(checkthis) == False:
      n = n*2
      count -=1
      continue
    if checker.issubset(checkthis) == True:
      return 1000 - count
  else:
    return -1


def count_distinct_sums_and_products(items):
  import itertools
  digits = set()
  sums = [sum(i) for i in itertools.combinations_with_replacement(items, 2)]
  products = [x*y for x, y in itertools.combinations_with_replacement(items,2)]
  soup = sums + products
  for num in soup:
    digits.add(num)
  return len(digits)


def count_and_say(digits):
  new = []
  x = 0
  while x < len(digits):
    cnt = 1
    while x + 1 < len(digits) and digits[x] == digits[x+1]:
      x +=1
      cnt +=1
    new.append(str(cnt) + digits[x])
    x +=1
  return ''.join(new)

def pancake_scramble(text):
  ttl = len(text)
  bagel = list(text)
  x = 0
  while x < ttl:
    if x == ttl:
      return ''.join(bagel)
    else:
      start = bagel[:x+1][::-1]
      moo = bagel[x+1:]
      bagel = start + moo
      x+=1
  else: 
    return ''.join(bagel)

def remove_after_kth(items, k = 1):
  seen = {}
  ret = []
  if k == 0:
    return []
  for x in items:
    if x not in seen:
      seen[x] = 1
      ret.append(x)
    else:
      if seen[x] < k:
        ret.append(x)
        seen[x] +=1
      else:
        pass
  return ret

def scrabble_value(word, multiplier = None):
  point = {'a':1, 'b':3, 'c':3, 'd':2, 'e':1, 'f':4, 'g':2, 'h':4, 'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10 }
  if multiplier == None:
    pts = 0
    for letter in word:
      pts += point[letter]
    return pts
  else:
    pts = 0
    for w, m in zip(word, multiplier):
      pts += point[w] * m
    return pts

def three_summers(items, goal):
  import itertools
  sumo = [tre for tre in itertools.combinations(items,3) if sum(tre) == goal]
  if sumo == []:
    return 'False'
  else:
      return 'True'

def group_equal(items):
  sub = []
  x = 0
  while x < len(items):
    temp = []
    while x + 1 < len(items) and items[x] == items[x+1]:
      temp.append(items[x])
      x +=1
    temp.append(items[x])
    sub.append(temp)
    x +=1
  return sub

def sum_of_two_squares(n):
  from itertools import combinations_with_replacement
  import math
  presum = [a*a for a in range(n) if a*a<n]
  j = []
  sol = sorted([pair for pair in combinations_with_replacement(presum, 2) if sum(pair) == n])
  if sol == []:
    return None
  else:
    b = sol[::-1]
    j.append(b[-1:][0][1])
    j.append(b[-1:][0][0])
    sol2 = [math.sqrt(x) for x in j]
    sol3 = [round(x) for x in sol2]
    return tuple(sol3)