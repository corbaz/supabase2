from app.models.user import User


class UserViewModel:
    def __init__(self, user=None):
        self.id = user.id if user else None
        self.name = user.name if user else ''
        self.email = user.email if user else ''

    def create(self):
        user = User.create(self.name, self.email)
        self.id = user.id

    def update(self):
        user = User.find(self.id)
        if user:
            user.update(self.name, self.email)

    def delete(self):
        user = User.find(self.id)
        if user:
            user.delete()

    @classmethod
    def all(cls):
        return [cls(user) for user in User.all()]

    @classmethod
    def find(cls, user_id):
        user = User.find(user_id)
        if user:
            return cls(user)
        else:
            return None
