from tokenizer import Token


class Lexer:
    
    def __init__(self, code):
        self.code = code
        self.tokenized = []
        
    def splitTokens(self):    
        for string in self.code:
            tokenStart = 0
            tokenPos = 0
            readingChars = False
            readingDigits = False
            readingString = False
            
            for char in string:
                if char == "\"":
                    if not readingString:
                        tokenStart = tokenPos
                        readingString = True
                    else:
                        string_ = string[tokenStart:tokenPos]
                        self.tokenized.append([string_[1:], "STRING"])
                        readingString = False
                    
                if not readingString:
                
                    if char.isalpha():
                        if not readingChars:
                            tokenStart = tokenPos
                        readingChars = True
                    else:
                        if readingChars:
                            string_ = string[tokenStart:tokenPos]
                            if string_ in Token.resTokensString:
                                self.tokenized.append([string_, "RES_STRING", Token.resTokensString[string_]])
                            else:                        
                                self.tokenized.append([string_, "VARIABLE"])
                            readingChars = False
                    
                    if char.isdigit():
                        if not readingDigits:
                            tokenStart = tokenPos
                        readingDigits = True
                    else:
                        if readingDigits:
                            self.tokenized.append([int(string[tokenStart:tokenPos]), "NUMBER"])
                            readingDigits = False
                
                    if char in Token.resTokensChar["algebraic"]:
                        self.tokenized.append([char, "ALGEBRAIC", Token.resTokensChar["algebraic"][char]])
                    elif char in Token.resTokensChar["assignment"]:
                        self.tokenized.append([char, "ASSIGNMENT"])
                    elif char in Token.resTokensChar["EoS"]:
                        self.tokenized.append([char, "EoS"])
                    
                        
                
                tokenPos += 1
            if readingChars:
                string_ = string[tokenStart:tokenPos]
                if string_ in Token.resTokensString:
                    self.tokenized.append([string_, "RES_STRING", Token.resTokensString[string_]])
                else:                        
                    self.tokenized.append([string_, "VARIABLE"])
                readingChars = False
            if readingDigits:
                self.tokenized.append([int(string[tokenStart:tokenPos]), "NUMBER"])
                readingDigits = False
        if readingString:
            return "__misq__" # передача MissingQuote ошибки в parser
        return self.tokenized
    
code = Lexer(["a = \"Hello, world + a;"])
lexed = code.splitTokens()
print(1)