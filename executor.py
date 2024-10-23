from lexer import Lexer
from parser import Parser
from exceptions import unrecognizedVariable

class Executor:
    
    def __init__(self, s_tree):
        self.s_tree = s_tree
        self.variables = {}
        self.output = []
        
    def execute(self):
        for branch in self.s_tree[1:]:
            self.execute_rec(branch)
        
    def execute_rec(self, branch):
        if isinstance(branch, list):
            if branch[0] == "ASSIGNMENT":
                self.variables[branch[1]] = self.execute_rec(branch[2])
            elif branch[0] == "PRINT":
                self.output.append(self.execute_rec(branch[1]))
            elif "ALG_" in branch[0]:
                if branch[0] == "ALG_ADD":
                    return self.execute_rec(branch[1]) + self.execute_rec(branch[2])
                elif branch[0] == "ALG_SUB":
                    return int(self.execute_rec(branch[1])) - int(self.execute_rec(branch[2]))
                elif branch[0] == "ALG_MUL":
                    return int(self.execute_rec(branch[1])) * int(self.execute_rec(branch[2]))
                elif branch[0] == "ALG_DIV":
                    return int(self.execute_rec(branch[1])) / int(self.execute_rec(branch[2]))
        else:
            if branch in self.variables:
                return self.variables[branch]
            else:
                if isinstance(branch, int):
                    return branch
                else:
                    # raise unrecognizedVariable
                    return branch

                
                
    
# code = Lexer(["a = 12;\nprint a;\nb = 13 + 21 - 32;"])
code = Lexer(["a = \"Hello, \" + \"world\";\nprint a + \"!\";"])
lexed = code.splitTokens() 
parser = Parser(lexed)
s_tree = parser.parseLexed()
executor = Executor(s_tree)
output = executor.execute()
print(1)

# TODO:
# 1. Разобраться с string (сложение строк и просто как переменные, вывод)  ✅
# 1.1 Сделать нормальную работу unrecognizedVariable
# 2. Доделать все
# 3. Сделать свое расширение .ya3 для языка
# Extra4. Добавить условные операторы, умножение строки на число