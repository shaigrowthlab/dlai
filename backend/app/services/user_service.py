from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_user(db: Session, user: UserCreate) -> User:
    existing = db.query(User).filter(User.email == user.email).first()

    if existing:
        raise ValueError("Email already exists")

    db_user = User(
        name=user.name,
        email=user.email,
        hashed_password=pwd_context.hash(user.password),
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user