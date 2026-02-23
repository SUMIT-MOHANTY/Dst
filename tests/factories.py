import factory
from app.models import User

class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session_persistence = "commit"

    id = factory.Sequence(lambda n: n)
    username = factory.Faker('user_name')
    email = factory.Faker('email')
