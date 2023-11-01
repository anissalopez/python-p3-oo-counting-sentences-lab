#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value = ""):
    self._value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self._value[-1] == "."
 
  def is_question(self):
    return self._value[-1] == "?"
  
  def is_exclamation(self):
    return self._value[-1] == "!"
  
  def count_sentences(self):
    if len(self.value):
      sentences = re.split('[?!.]\s', self.value)
      return len(sentences)
    return 0
    
