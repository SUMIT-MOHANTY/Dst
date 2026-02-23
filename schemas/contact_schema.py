from marshmallow import Schema, fields, validate, ValidationError

class ContactSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    message = fields.Str(required=True, validate=validate.Length(min=1, max=2000))
