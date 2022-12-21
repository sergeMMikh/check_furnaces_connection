from classes.furnace_io import FurnaceIO
from models.furnace_models import Base
from models.session import engine, Session
from sqlalchemy.sql import select


def main():
    Base.metadata.create_all(engine)

    furnace = FurnaceIO(ip='192.168.1.250',
                        port='9003')

    # conn = engine.connect()
    #
    # s = select(furnace)
    #
    # print(Session.query(FurnaceIO).all())

    if furnace.check_ping():
        print(furnace.get_current_data())


if __name__ == '__main__':
    main()
