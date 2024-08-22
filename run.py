from src.quieres.orm import create_tables, add_worker, add_task
import datetime


create_tables()
add_worker()
add_task()
print(datetime.datetime.now(datetime.timezone.utc))