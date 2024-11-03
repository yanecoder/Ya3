from interpreter.lexer import Lexer
from interpreter.parser import Parser
from interpreter.executor import Executor
import os, sys

PATH = os.getcwd() + "\\" + sys.argv[-1]
f = open(PATH)
readings = f.read()

def launch():
    try:
        code = Lexer([readings])
        lexed = code.splitTokens() 
        parser = Parser(lexed)
        s_tree = parser.parseLexed()
        executor = Executor(s_tree)
        error_output = executor.execute()
    
        if error_output:
            print(error_output) # ошибки компилятора
        elif not isinstance(s_tree, list):
            print(s_tree)
        else:
            print(*executor.output, sep="\n") # если все верно
    except Exception:
        print("Something went wrong. Check syntax")

if __name__ == "__main__":
    launch()

