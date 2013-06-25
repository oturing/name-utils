import io, sys

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

from models import Base, Nome

def criar_tabelas(url_bd):
    engine = sa.create_engine(url_bd, echo=True)
    Base.metadata.create_all(engine)

def carregar(url_bd, nome_arq):
    engine = sa.create_engine(url_bd, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    with io.open(nome_arq, encoding='utf-8') as entrada:
        for n, lin in enumerate(entrada, 1):
            lin = lin.rstrip()
            print(n, lin)
            nome = Nome(lin)
            session.add(nome)
    session.commit()

if __name__=='__main__':
    url_bd = 'sqlite:///nomes.sqlite'
    #criar_tabelas(url_bd)
    carregar(url_bd, sys.argv[1])

