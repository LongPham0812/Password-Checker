from django.db import models
import statistics

MAX_LENGTH = 30

def default_password_attributes():
    return {
        'length': 0,
        'uppercase': 0,
        'lowercase': 0,
        'numbers': 0,
        'special_characters': 0,
        'previous_password': 0,
        'contains_common_words': 0,
        'contains_personal_information': 0,
    }

class Password(models.Model):
    password_text = models.CharField(max_length=MAX_LENGTH)
    password_strength = models.IntegerField(default=50)
    password_attributes = models.JSONField(default=default_password_attributes)

    def get_password_text(self):
        return self.password_text

    def set_password_strength(self, password_strength):
        self.password_strength = password_strength

    def get_password_strength(self):
        return self.password_strength

    def calculate_password_strength(self):
        # 0 to 100
        self.password_strength += (self.password_attributes['length'] - 9) * 5
        self.password_strength = 100 if self.password_strength > 100 else 0 if self.password_strength < 0 else self.password_strength

        self.password_strength += (self.password_attributes['uppercase'] - 3) * 5
        self.password_strength = 100 if self.password_strength > 100 else 0 if self.password_strength < 0 else self.password_strength

        self.password_strength += (self.password_attributes['lowercase'] - 3) * 5
        self.password_strength = 100 if self.password_strength > 100 else 0 if self.password_strength < 0 else self.password_strength
        
        self.password_strength += (self.password_attributes['numbers'] - 3) * 5
        self.password_strength = 100 if self.password_strength > 100 else 0 if self.password_strength < 0 else self.password_strength
        
        self.password_strength += (self.password_attributes['special_characters'] - 3) * 5
        self.password_strength = 100 if self.password_strength > 100 else 0 if self.password_strength < 0 else self.password_strength

        upper_percent = (self.password_attributes['uppercase'] / self.password_attributes['length'])
        lower_percent = (self.password_attributes['lowercase'] / self.password_attributes['length'])
        number_percent = (self.password_attributes['numbers'] / self.password_attributes['length'])
        symbol_percent = (self.password_attributes['special_characters'] / self.password_attributes['length'])
        deviation = statistics.stdev([upper_percent, lower_percent, number_percent, symbol_percent])
        self.password_strength -= deviation * 10
        self.password_strength = 100 if self.password_strength > 100 else 0 if self.password_strength < 0 else self.password_strength

        if self.password_attributes['previous_password']:
            self.password_strength -= 10
            self.password_strength = 100 if self.password_strength > 100 else 0 if self.password_strength < 0 else self.password_strength
        
        if self.password_attributes['common_words']:
            self.password_strength -= 10
            self.password_strength = 100 if self.password_strength > 100 else 0 if self.password_strength < 0 else self.password_strength
        
        if self.password_attributes['personal_information']:
            self.password_strength -= 10
            self.password_strength = 100 if self.password_strength > 100 else 0 if self.password_strength < 0 else self.password_strength

        self.password_strength = round(self.password_strength)

    def set_password_attributes(self, password_attributes):
        self.password_attributes = password_attributes

    def get_password_attributes(self):
        return self.password_attributes

    def calculate_password_attributes(self, previous_password, common_words, personal_information):
        self.password_attributes['length'] = len(self.password_text)
        
        for char in self.password_text:
            if char.isupper():
                self.password_attributes['uppercase'] += 1
            elif char.islower():
                self.password_attributes['lowercase'] += 1
            elif char.isdigit():
                self.password_attributes['numbers'] += 1
            else:
                self.password_attributes['special_characters'] += 1

        self.password_attributes['previous_password'] = 1 if previous_password else 0
        self.password_attributes['common_words'] = 1 if common_words else 0
        self.password_attributes['personal_information'] = 1 if personal_information else 0

    def __str__(self):
        return f"{self.password_text} {self.password_strength} {self.password_attributes}"