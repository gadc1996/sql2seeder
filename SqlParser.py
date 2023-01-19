import re
import shlex

class SqlParser:
    def __init__(self, filename):
        self._filename = filename
        
        self.model = self._getModel()
        self.attributes = self._getAttributes()
        self.values = self._getValues()

    def _getModel(self):
        with open(self._filename) as file:
            try:
                return file.readline().split()[2].replace('`', '').replace("_", " ").title().replace(" ", '')
            except:
                print(self._filename)
        
    def _getAttributes(self):   
        with open(self._filename) as file:
            return re.search('\(([^)]+)', file.readline()).group(1).replace('`', '').replace(',', '').split(' ')

    def _getValues(self):
        values = []
        with open(self._filename) as file:
            for line in file.readlines():
                if not line.startswith("INSERT") and line.startswith("("):
                    string = line.replace('(', '').replace(')', '').replace(',', '').replace(';', '').replace("'", '"')
                    values.append(shlex.split(string, posix=False))
        return values
        
