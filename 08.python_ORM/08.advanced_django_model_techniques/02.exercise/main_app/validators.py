from django.core.exceptions import ValidationError


class ValidateName:
    def __init__(self, message: str):
        self.message = message
    
    def __call__(self, value: str):
        for char in value:
            if not (char.isalpha() or char.isspace()):
                raise ValidationError(self.message)
    
    def deconstruct(self):
        return (
            'main_app.validators.ValidateName', # path
            (self.message, ), # args
            {} # kwargs
        )
