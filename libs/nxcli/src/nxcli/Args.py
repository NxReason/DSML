class Args:
    inputs: list[str]
    errors: list[str]

    def __init__(self):
        self.inputs = []
        self.errors = []

    def __str__(self):
        s = 'Inputs:\n'
        for i in self.inputs:
            s += f'\t{i}\n'

        s += 'Args:\n'
        for key, value in self.__dict__.items():
            if (key in ['inputs', 'errors']):
                continue
            s += f'\t{key}: {value}\n'

        s += 'Errors:\n'
        for e in self.errors:
            s += f'\t{e}\n'
        return s[:-1]

    def __getattr__(self, name):
        if name == 'input' and len(self.inputs) > 0:
            return self.inputs[0]
        try:
            return self.__dict__[name]
        except:
            return None

    def valid(self):
        return len(self.errors) == 0

    def show_errors(self):
        print('argument parsing errors:')
        for e in self.errors:
            print(f'  {e}')
