import datetime as dt
from marshmallow import Schema, fields


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()


user = User(name="Monty", email="monty@python.org")
schema = UserSchema()
result, errs = schema.dump(user)

print result

# dict_test = dict(result.data)
# dict_test.update(test="test add")
#
# print dict_test
