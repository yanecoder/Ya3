from exceptions import unrecognizedVariable

class Executor:
    
    def __init__(self, s_tree):
        self.s_tree = s_tree
        self.variables = {}
        self.output = []
        
    def execute(self):
        line_number = 1
        try:
            for branch in self.s_tree[1:]:
                self.execute_rec(branch)
                line_number += 1
        except unrecognizedVariable as variable:
            return f"Unrecognized variable {variable.message} in line {line_number}"
        
        
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
                    if branch[0] == "$":
                        raise unrecognizedVariable(branch)
                    return branch

