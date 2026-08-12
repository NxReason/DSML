class DataFrame:
    def __init__(self, headers: list[str] = []):
        self.headers = headers
        self.data = []

    def filter_by(self, col: str, value):
        if col not in self.headers:
            raise ValueError(f'{col} header not in DataFrame')

        idx = self.headers.index(col)
        df = DataFrame(self.headers)
        for row in self.data:
            if row[idx] == value:
                df.data.append(row)
        return df

    def __getitem__(self, key):
        if key not in self.headers:
            return []
        idx = self.headers.index(key)

        return [row[idx] for row in self.data]
