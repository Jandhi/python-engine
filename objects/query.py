class Query():
    def __init__(self, query_type) -> None:
        self.query_type = query_type

    def with_field(self, name, value):
        return self