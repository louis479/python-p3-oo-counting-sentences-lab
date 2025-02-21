#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=""):
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueError("Value must be a string")  # Fixed capitalization
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")
    
    def is_question(self):
        return self._value.endswith("?")
    
    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        """Counts the number of sentences based on '.', '?', and '!' endings."""
        normalized = re.sub(r"[.?!]+", ".", self._value)  # Fixed incorrect variable name
        sentences = normalized.split(".")
        return len([s for s in sentences if s.strip()])  # Removes empty strings before counting

