from data_validator.validator import Validator


class OneOf(Validator):
    def __init__(self, *options):
        self.options = options

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f'Expected {value!r} to be one of {self.options!r}')
