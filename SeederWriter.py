HEADER = '\n<?php\n\nuse Illuminate\\Database\\Seeder; \nuse App\\{0};\n\nclass {1}Seeder extends Seeder\n.\n    /**\n     * Run the database seeds.\n     *\n     * @return void\n     */\n    public function run()\n    .\n'
FOOTER = '\n    }\n}\n'

class SeederWriter:
    
    def __init__(self, model, attributes, values):
        self.model = model
        self.attributes = attributes
        self.values = values

    
    def write(self):
        file = open(f'''seeders/{self.model}Seeder.php''', 'w')
        self._writeHeader(file)
        self._writeContent(file)
        self._writerFooter(file)

    
    def _writeHeader(self, file):
        file.write(HEADER.format(self.model[:-1], self.model).replace('.', '{'))

    
    def _writeContent(self, file):
        for values in self.values:
            file.write(f'''        {self.model[:-1]}::create([\n''')
            for index, value in enumerate(values):
                try:
                    file.write(f'''            "{self.attributes[index]}" => ''' + value.replace('\\', '') + ',\n')
                except:
                    print(f'''Error in file {self.model}Seeder''')
                    print(f'''id: {values[0]}''')
            file.write('        ]);\n')


    
    def _writerFooter(self, file):
        file.write(FOOTER)