class Token:

    resTokensString = {
            "print": "PRINT",
                    
        }
        
    resTokensChar = {
        "algebraic": {
            "+": "ALG_ADD",
            "-": "ALG_SUB",
            "*": "ALG_MUL",
            "/": "ALG_DIV",
        },
        "assignment": {
            "=": "ASSIGNMENT",
        },
        "EoS": {
            ";": "EoS" 
        }
        }
    
    def __init__(self, type, text, pos):
        self.type = type
        self.text = text
        self.pos = pos