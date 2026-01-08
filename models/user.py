from database import db, Mapped, mapped_column

# UserClass = user_class


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(50), nullable=False, unique=False)


def seedData(db):
    if db.session.query(User).first() == None:
        user = User()
        user.name = "Kimmo"
        db.session.add(user)
        db.session.commit()
