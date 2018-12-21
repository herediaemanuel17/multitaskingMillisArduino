from models import Medidas
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import mysql.connector
#from mysql.connector.constants import ClientFlag cnx = mysql.connector.connect(user='[example]', password='[example]', host='[localhost]', client_flags=[ClientFlag.LOCAL_FILES]) cursor = cnx.cursor()

import os
import json

class Database(object):
    session = None
    db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "example"
    db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "example"
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "localhost"
    db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "db"
    db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"
    Base = declarative_base()


    def get_last(self):
        session = self.get_session()
        ultima = session.query(Medidas).order_by(Medidas.id.desc()).first()
        session.close()
        return ultima

    def get_session(self):
        """Singleton of db connection

        Returns:
            [db connection] -- [Singleton of db connection]
        """
        if self.session == None:
            connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
            engine = create_engine(connection,echo=True)
            connection = engine.connect()
            Session = sessionmaker(bind=engine)
            self.session = Session()
            self.Base.metadata.create_all(engine)
        return self.session
