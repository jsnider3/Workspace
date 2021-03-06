''' A library for solving coding challenges
    involving strings.
    @author: Josh Snider'''
import math
import re
import string

def british_number_string(num):
  ''' Convert a number to a string
      in the british way. '''
  strn = str(num)
  words = []
  tens = {"1" : "ten", "2" : "twenty", "3" : "thirty", "4" : "forty",
          "5" : "fifty", "6" : "sixty", "7" : "seventy", "8" : "eighty",
          "9" : "ninety", "11" : "eleven", "12" : "twelve", "13" : "thirteen",
          "14" : "fourteen", "15" : "fifteen", "16" : "sixteen",
          "17" : "seventeen", "18" : "eighteen", "19" : "nineteen"}
  ones = {"1" : "one", "2" : "two", "3" : "three", "4" : "four",
          "5" : "five", "6" : "six", "7" : "seven", "8" : "eight",
          "9" : "nine"}
  if len(strn) == 4:
    words.append(ones[strn[0]])
    words.append("thousand")
    strn = strn[1:]
  if len(strn) == 3:
    if strn[0] in ones:
      words.append(ones[strn[0]])
      words.append("hundred")
    if strn[1:] != "00":
      words.append("and")
    strn = strn[1:]
  if len(strn) == 2:
    if strn in tens:
      words.append(tens[strn])
      strn = strn[2:]
    else:
      if strn[0] in tens:
        words.append(tens[strn[0]])
      strn = strn[1:]
  if len(strn) == 1:
    if strn[0] in ones:
      words.append(ones[strn[0]])
    strn = strn[1:]
  strn = " ".join(words)
  return strn

def caesar(phrase, shift):
  ''' Caesar shift a phrase.'''
  shift %= 26
  res = []
  for char in phrase:
    if char.isupper():
      res.append(chr((ord(char)-ord('A')+shift)%26+ord('A')))
    elif char.islower():
      res.append(chr((ord(char)-ord('a')+shift)%26+ord('a')))
    else:
      res.append(char)
  return ''.join(res)

def case_insensitive_contains(phrase, pattern):
  ''' Determine if phrase has pattern (case insensitive).'''
  return re.search(pattern, phrase, re.IGNORECASE) != None

def changes_for_anagram(first, second):
  ''' How many letters in first would need to be changed
      to make it an anagram of second.'''
  if len(first) == len(second):
    return dels_for_anagram(first, second) // 2

def chars_used(word):
  ''' Get the number of unique characters in a string. '''
  return len(set(word))

def common_substring(first, second):
  ''' Do first and second have a substring in common? '''
  return len(set(first).intersection(second)) > 1

def dels_for_anagram(first, second):
  ''' Return the minimal number of characters that would
      need to be deleted from first and second to make them
      anagrams.'''
  dels = set(first).symmetric_difference(set(second))
  shared = set(first).intersection(set(second))
  rm = 0
  for d in dels:
    rm += first.count(d)
    rm += second.count(d)
  for sh in shared:
    rm += abs(first.count(sh) - second.count(sh))
  return rm

def is_anagram(first, second):
  ''' return if first and second are anagrams
      of each other. '''
  first = str(first)
  second = str(second)
  for char in first + second:
    if first.count(char) != second.count(char):
      return False
  return True

def is_funny(word):
  ''' As per https://www.hackerrank.com/challenges/funny-string.'''
  assert len(word) > 1
  rev = word[::-1]
  for ind in range(len(word) - 1):
    if (abs(ord(word[ind + 1]) - ord(word[ind])) !=
        abs(ord(rev[ind + 1]) - ord(rev[ind]))):
      return False
  return True

def is_pan(word):
  ''' Check if a word is a valid PAN.
      Which is basically an Indian SSN.'''
  pattern = re.compile("([A-Z]{5}[0-9]{4}[A-Z])")
  return pattern.match(word)

def is_pangram(phrase):
  ''' Determine if phrase contains each of [a-z] once.'''
  phrase = set(phrase.lower())
  for c in string.ascii_lowercase:
    if c not in phrase:
      return False
  return True

def is_pi_phrase(phrase):
  ''' Check if the word lengths of phrase
      correspond to the digits of pi.'''
  pi_str = "31415926535897932384626433833"
  lens = "".join(list(str(len(s)) for s in phrase.split()))
  return lens == pi_str[:len(lens)]

def shared_prefix(first, second):
  '''Get the longest prefix shared by two strings.'''
  end = min(len(first), len(second))
  for leng in range(0, end):
    if first[leng] != second[leng]:
      return first[:leng]
  return first[:end]

def swap_case(phrase):
  ''' Return a string with all the lower case letters made
      upper case and all the upper case letters made lower case. '''
  swapd = []
  for char in phrase:
    if char.isupper():
      swapd.append(char.lower())
    elif char.islower():
      swapd.append(char.upper())
    else:
      swapd.append(char)
  return ''.join(swapd)

def unique_str(words):
  ''' Determine if a string is composed entirely
      of unique characters. '''
  return len(words) == chars_used(words)

def welcome_mat(rows, cols):
  ''' Print a welcome mat. '''
  assert rows % 2 and cols == rows * 3
  for i in range(1, rows, 2):
    print ('-' * ((cols - i*3)//2) + '.|.'*i + '-' * ((cols - i*3)//2))
  print ('-' * ((cols - 7)//2) + 'WELCOME' + '-' * ((cols - 7)//2))
  for i in range(rows-2, -1, -2):
    print ('-' * ((cols - i*3)//2) + '.|.'*i + '-' * ((cols - i*3)//2))

