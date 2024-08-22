import datetime
from typing import Annotated
from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base, str_256

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.now(datetime.timezone.utc))]
meta = Base.metadata

class WorkersOrm(Base):
	__tablename__ = "workers"

	id: Mapped[intpk]
	username: Mapped[str] = mapped_column()

class TasksOrm(Base):
	__tablename__ = "tasks"

	id: Mapped[intpk]
	title: Mapped[str]
	desc: Mapped[str_256]
	price: Mapped[float]
	currency: Mapped[str]
	worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
	created_at: Mapped[created_at]
	updated_at: Mapped[updated_at]


























