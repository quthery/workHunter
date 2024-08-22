from src.database import async_engine, sync_engine, fabric_session
from src.models import meta, WorkersOrm, TasksOrm
from src.database import Base
from sqlalchemy.exc import IntegrityError





def create_tables():
	sync_engine.echo = False
	meta.drop_all(sync_engine)
	meta.create_all(sync_engine)
	sync_engine.echo = True


def add_worker():
	with fabric_session() as session:
		worker = WorkersOrm(username="krutoi bobr")
		worker1 = WorkersOrm(username="krutoi wolk")
		session.add_all([worker, worker1])
		session.commit()

def add_task():
    with fabric_session() as session:
        try:
            task = TasksOrm(title="amazon parser", desc="create an amazon parser with python and requests", price=50.00, currency="usdt", worker_id=1)
            session.add(task)
            session.commit()
        except IntegrityError:
            session.rollback() 
            print("Ошибка: внешний ключ не совпадает.")