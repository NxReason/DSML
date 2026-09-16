import builtins


class Column:
    def __init__(self, t: type, primary: bool = False, required: bool = False, unique: bool = False, default=None):
        self.t = t
        self.primary = primary
        self.required = required
        self.unique = unique
        self.default = default

    def __str__(self):
        return f'Column(t={self.t}, primary={self.primary}, required={self.required}, unique={self.unique}, default={self.default})'

    def props_str(self) -> str:
        out = ''
        if self.primary:
            out += " PRIMARY KEY AUTOINCREMENT,"
            return out

        if self.required:
            out += " NOT NULL"

        if self.unique:
            out += " UNIQUE"

        out += ",\n"

        return out


class Model:
    table_name = ''

    def __init__(self):
        self._name = self.table_name \
            if self.table_name != '' \
            else self.__class__.__name__

        self.columns = {}
        for n, t in self.__annotations__.items():
            if t != Column:
                continue
            self.columns[n] = self.__getattribute__(n)

    def set_conn(self, conn):
        self.conn = conn

    def create_table(self):
        cursor = self.conn.cursor()
        query = f"CREATE TABLE IF NOT EXISTS {self._name} (\n"

        for name, col in self.columns.items():
            query += f"\t{name} {map_sql_type(col.t)}"
            query += col.props_str()

        query = query[:-2]
        query += ")"
        self._create_table_query = query

        cursor.execute(query)
        self.conn.commit()

    def create(self, data):
        cursor = self.conn.cursor()
        query = f'INSERT INTO {self._name} ({self._get_columns_str()}) VALUES ({self._get_values_placeholder()})'

        values = []
        for c, props in self.columns.items():
            if props.primary:
                continue

            if c not in data:
                if props.required and props.default == None:
                    print(
                        f'[ERROR:MODEL:CREATE] {c} not provided and no default value')
                    return
                data[c] = props.default

            values.append(data[c])

        cursor.execute(query, values)
        self.conn.commit()

    def read_all(self):
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM {self._name}")
        return cursor.fetchall()

    def read_by_id(self, id):
        cursor = self.conn.cursor()
        cursor.execute(f'SELECT * FROM {self._name} WHERE id = ?', [id])
        return cursor.fetchone()

    def update(self, id, data):
        cursor = self.conn.cursor()
        query = f'UPDATE {self._name} SET\n'
        values = []
        for name, val in data.items():
            query += f'{name} = ?,'
            values.append(val)

        query = query[:-1]
        query += 'WHERE id = ?;'
        values.append(id)

        cursor.execute(query, values)

    def delete(self, id):
        cursor = self.conn.cursor()
        query = f'DELETE FROM {self._name} WHERE id = ?'
        cursor.execute(query, [id])

    def _get_columns_str(self):
        out = ', '.join(
            [name for name, props in self.columns.items() if not props.primary])
        return out

    def _get_values_placeholder(self):
        return ', '.join(
            ['?' for name, props in self.columns.items() if not props.primary]
        )


def map_sql_type(t: type) -> str:
    match t:
        case builtins.str:
            return 'TEXT'
        case builtins.int:
            return 'INTEGER'
        case builtins.float:
            return 'REAL'
        case _:
            return 'TEXT'
