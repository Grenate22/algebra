import re

class MathOperationChecker:
    def __init__(self, text):
        self.text = text

    def check_math_operations(self):
        operations = []
        operations.extend(self._find_sum())
        operations.extend(self._find_product())
        operations.extend(self._find_subtract())

        return operations

    def _find_sum(self):
        pattern = re.compile(r'\bSUM\b', re.IGNORECASE)
        return pattern.findall(self.text)

    def _find_product(self):
        pattern = re.compile(r'\bPRODUCT\b', re.IGNORECASE)
        return pattern.findall(self.text)

    def _find_subtract(self):
        pattern = re.compile(r'\bSUBTRACT\b', re.IGNORECASE)
        return pattern.findall(self.text)

class Algebra :

    def _extract_integers_from_text(self,text):
    # Use a regular expression to find all integers in the text
        integers = re.findall(r'\b\d+\b', text)
        return list(map(int, integers))
    
    def _extract_func_from_text(self,text):
           pattern = re.compile(r'\bSUM\b', re.IGNORECASE)
           match = pattern.search(text)
           return match

    def calc(self, word):
                operator = MathOperationChecker(word)
                oper = operator.check_math_operations()
                result = []
                for op in oper:
                    print(op)
                    digit = self._extract_integers_from_text(word)
                    if op == "sum":
                        sum = digit[0] + digit [1]
                        result.append(sum)
                    if op == "product":
                         product = digit[0] * digit[1]
                         result.append(product)
                return result 

text1 = Algebra()
print(text1.calc("Find the sum and product  10 and 7"))


        