from exceptions import missingEoS

class Parser:
    
    def __init__(self, lexed):
        self.lexed = lexed
        self.s_tree = [["main"]]

    def parseLexed(self):
        line_number = 1
        string = []
        if self.lexed == "__misq__": # missingQoute at string
            return "Missing quote"
        for token in self.lexed:
            if token[1] == "EoS":
                string.append(token)
                try:
                    self.s_tree.append(self.parseString(string, line_number))
                except missingEoS:
                    return f"Missing \";\" at the end of a line {line_number}"
                string = []
                line_number += 1
            else:
                string.append(token)
        if len(string) > 0:
            try:
                self.s_tree.append(self.parseString(string, line_number))
            except missingEoS:
                return f"Missing \";\" at the end of a line {line_number}"
            string = []
            line_number += 1
        return self.s_tree
            
    def parseString(self, string, line_number):
        if string[0][1] in ["VARIABLE", "NUMBER", "STRING"]:
            if len(string) > 1:
                if string[1][1] == "ALGEBRAIC":
                    return [string[1][2], string[0][0], self.parseString(string[2:], line_number)]
                elif string[1][1] == "ASSIGNMENT":
                    return [string[1][1], string[0][0], self.parseString(string[2:], line_number)]
                elif string[1][1] == "EoS":
                    return string[0][0]
                else:
                    raise missingEoS
            else:
                raise missingEoS # возможно не ошибка
        elif string [0][1] == "RES_STRING":
            if string[0][2] == "PRINT":
                return ["PRINT", self.parseString(string[1:], line_number)]
            else:
                return f"Unrecognised command at the end of a line {line_number}"
            

    