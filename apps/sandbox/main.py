from nxorm import Model, Column, Relation, DB


class Main(Model):
    table_name = 'main'

    id: Column = Column(int, primary=True)
    name: Column = Column(str, default='No Name')


class Dep(Model):
    table_name = 'dep'

    id: Column = Column(int, primary=True)
    name: Column = Column(str, default='John Doe')
    main_id: Relation = Relation('main')


def main():
    main = Main()
    dep = Dep()
    db = DB('hello', [main, dep])

    dep.create({'name': 'Dep 1', 'main_id': 1})
    dep.create({'name': 'Dep 2', 'main_id': 1})
    print(dep.read_all())


if __name__ == "__main__":
    main()
