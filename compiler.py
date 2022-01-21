
class Operator:
    def __init__(self, python_name, symbol, target):
        self.name = python_name
        self.symbol = symbol
        self.target = target
        self.cond_target = {}

    def get_target(self):
        return self.target

    def get_name(self):
        return self.name

    def prev_cond(self, prev_operator, target):
        self.cond_target[prev_operator] = target

    def next_cond(self, next_operator, target):
        self.cond_target[next_operator] = target

    def need_next_operator(self, operator):
        self.need_next_operator = operator
        self.nno_error = self.nno_error()

    def need_prev_operator(self, operator):
        self.need_prev_operator = operator
        self.npo_error = self.npo_error()

    def nno_error(self, operator):
        try:
            self.get_next_cond(operator)
        except:
            return ' '

    def npo_error(self, operator):
        try:
            self.get_prev_cond(operator)
        except:
            return ' '

    def get_next_cond(self, operator):
        return self.cond_target[operator]

    def get_prev_cond(self, operator):
        return self.cond_target[operator]


class StrOperator:
    def __init__(self, name, target):
        self.name = name
        self.target = target
        self.cond_target = {}

    def cond_next_stroperator(self, strstroperator, target):
        self.cond_target[strstroperator] = target

    def cond_prev_stroperator(self, strstroperator, target):
        self.cond_target[strstroperator] = target

    def need_next_stroperator(self, stroperator):
        self.need_next_stroperator = stroperator
        self.nno_error = self.nno_error()

    def need_prev_stroperator(self, stroperator):
        self.need_prev_stroperator = stroperator
        self.npo_error = self.npo_error()

    def nno_error(self, stroperator):
        try:
            self.get_next_cond(stroperator)
        except:
            return ' '

    def npo_error(self, stroperator):
        try:
            self.get_prev_cond(stroperator)
        except:
            return ' '

    def get_next_cond(self, stroperator):
        return self.cond_target[stroperator]

    def get_prev_cond(self, stroperator):
        return self.cond_target[stroperator]

def read_input_file(file_name):
    file = open(file_name, "rt")
    raw_code = file.read()
    return raw_code if len(raw_code) > 0 else "empty file"


def template_asm(ind):
    if ind == 0:
        head_asm = ".386 " \
                   ".model flat, stdcall" \
                   "option casemap:none " \
                   "include \masm32\include\kernel32.inc " \
                   "include \masm32\include\windows.inc " \
                   "include \masm32\include\kernel32.inc " \
                   "include \masm32\include\masm32.inc " \
                   "include \masm32\include\user32.inc " \
                   "includelib \masm32\lib\kernel32.lib " \
                   "includelib \masm32\lib\masm32.lib " \
                   "includelib \masm32\lib\user32.lib "

        file = open("templates/head_asm.txt", "rt")
        head_template = file.read()
    elif ind == 1:
        file = open()

def parse_code(code):
    code_lines = code.split('\n')
    string_in_code = []
    symbol_in_code = []
    for line in range(len(code_lines)):
        string_in_code.append('')
    for str in code_lines:
        try:
            string_in_code.append(str)
        except:
            string_in_code.append('\n')
        for symbol in str:
            try:
                symbol_in_code.append(symbol)
            except:
                symbol_in_code.append(' ')
    lexim(string_in_code, symbol_in_code)

def lexim(string_code, symbol_code):


def main():
    file_name = "factorial.py"
    raw_code = read_input_file(file_name)
    parse_code(raw_code)
