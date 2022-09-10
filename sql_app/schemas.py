from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    age: int


class UserCreate(UserBase):
    password: str


class GameBase(BaseModel):
    name: str


class GameCreate(GameBase):
    pass


class Game(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
