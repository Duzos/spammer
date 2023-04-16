import re

class Splitter():
    def __init__(self, filepath: str):
        self.path = filepath

    def split(self, text: str):
        split_lines = re.split('(?<=[.!?]) +',text)
        lines = ""

        for line in split_lines:
            lines = lines + "\n" + line
        
        return lines
    
    def rewrite(self):
        file = open(self.path, "r")
        lines = self.split(file.read())
        
        file = open(self.path, "w")
        file.write(lines)
        