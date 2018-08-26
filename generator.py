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

    def create_foreign_key(self, src_table, src_field, dst_table):
        self.relations.append(
            (
                f'ALTER TABLE {src_table} ' 
                f'ADD CONSTRAINT {src_table}_{src_field}_fkey_{dst_table} '
                f'FOREIGN KEY ({src_field}) REFERENCES {dst_table} (id);'
            )
        )

    def create_additional_field(self, table, field):
        self.relations.append(f'ALTER TABLE {table} ADD COLUMN {field} INTEGER NOT NULL;\n')

    def make_many_to_many(self, table1, table2):
        table1 = table1.lower()
        table2 = table2.lower()

        inter_table = '_'.join((table1, table2))
        first_id = f'{table1}_id'
        second_id = f'{table2}_id'

        self.create_table(
            inter_table,
            {
                'fields': {
                    first_id: 'INTEGER NOT NULL',
                    second_id: 'INTEGER NOT NULL',
                }
            }
        )

        self.create_foreign_key(inter_table, first_id, table1)
        self.create_foreign_key(inter_table, second_id, table2)

    def make_one_to_many(self, one_table, many_table):
        many_table = many_table.lower()
        one_table = one_table.lower()
        many_field = f'{one_table}_id'

        self.create_additional_field(many_table, many_field)
        self.create_foreign_key(many_table, many_field, one_table)

    def parse_relations(self, table, data):
        for relation, relation_type in data['relations'].items():
            if relation_type == 'many' and self.data[relation]['relations'][table] == 'many':
                self.make_many_to_many(table, relation)
                self.data[relation]['relations'].pop(table, None)

            if relation_type == 'one' and self.data[relation]['relations'][table] == 'many':
                self.make_one_to_many(table, relation)
                self.data[relation]['relations'].pop(table, None)

    def generate(self):
        self.read_schema()

        for table, data in self.data.items():
            self.create_table(table, data)
            self.parse_relations(table, data)

        with open('db.sql', 'w') as f:
            f.write('\n'.join(self.tables))
            f.write('\n\n')
            f.write('\n'.join(self.relations))


if __name__ == '__main__':
    g = Generator('schema.yaml')
    g.generate()
`