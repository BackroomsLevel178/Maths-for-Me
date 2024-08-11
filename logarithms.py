import sys
numbers = "0123456789"

def log(base, answer):
    power = 0
    while base ** power != answer:
        power += 1
    return power - 1

equation = "2x^7 - 3x^6 + 5x^3 - 2x^4 / 7x^8 + 5x^3"
symbols = "+-*/"

class Object:
    def __init__(self, number, pronumeral, exponent):
        self.number = number
        self.pronumeral = pronumeral
        self.exponent = exponent
        
    def __str__(self):
        return f"{self.number}{self.pronumeral}^{self.exponent}"    
    
    def derive(self):
        self.number = self.exponent * self.number
        self.exponent = self.exponent - 1
        return self

    @staticmethod
    def create_term(string):
        index = string.find("x")
        term = Object(int(string[:index]), string[index], int(string[index + 2:]))
        return term
    
    @staticmethod
    def identify_terms(string):
        all_terms = []
        current_term = ""
        for char in string:
            if char in symbols:
                if current_term:
                    all_terms.append(current_term.strip())
                    current_term = ""
                all_terms.append(char)
            else:
                current_term += char
        if current_term:
            all_terms.append(current_term.strip())
        return all_terms
    
    @staticmethod
    def simply_derive():
        equation = input("Enter your equation here: ")
        eq_list = Object.identify_terms(equation)
        for i, term in enumerate(eq_list):
            if i % 2 == 0:
                term_obj = Object.create_term(term)
                derived_term = term_obj.derive()
                eq_list[i] = str(derived_term)
        print(" ".join(eq_list))

Object.simply_derive()