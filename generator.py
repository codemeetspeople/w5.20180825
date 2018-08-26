import yaml

class Generator:
    def __init__(self, schema_path):
        self.schema_path = schema_path
        self.tables = []
        self.relations = []
        self.data = None

    def read_schema(self):
        with open(self.schema_path, 'r') as f:
            self.data = yaml.load(f.read())

    def create_table(self, name, data):
        table = (
            'DROP TABLE IF EXISTS "{table_name}" CASCADE;\n'
            'CREATE TABLE "{table_name}" (\n'
            '  id SERIAL NOT NULL PRIMARY KEY,\n'
            '  {fields}\n'
            ');\n'
        ).format(
            table_name=name.lower(),
            fields=',\n  '.join(
                [f'{k} {v.upper()}' for k, v in data['fields'].items()]
            )
        )
        self.tables.append(table)

    def generate(self):
        self.read_schema()

        for table, data in self.data.items():
            self.create_table(table, data)

        with open('db.sql', 'w') as f:
            f.write('\n'.join(self.tables))

if __name__ == '__main__':
    g = Generator('schema.yaml')
    g.generate()
