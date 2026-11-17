from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Configurar la conexión a la base de datos SQLite
engine = create_engine("sqlite:///zapatos.db", echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# 3. Construir el modelo Zapato que representará la tabla zapatos
class Zapato(Base):
    __tablename__ = 'zapatos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    modelo = Column(String, nullable=False)
    talla = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)

# 2. Función que el main.py está llamando obligatoriamente
def inicializar_bd():
    Base.metadata.create_all(engine)

# ==========================================
# ACTIVIDAD 2: Implementar el CRUD
# ==========================================p

def crear_zapato(modelo, talla, precio):
    """Registra un zapato en la base de datos."""
    session = Session()
    try:
        nuevo_zapato = Zapato(modelo=modelo, talla=talla, precio=precio)
        session.add(nuevo_zapato)
        session.commit()
        print(f"¡Zapato '{modelo}' registrado con éxito!")
        return True  # <--- ¡Añade esto para que el main.py sepa que salió bien!
    except Exception as e:
        session.rollback()
        print(f"Error al registrar el zapato: {e}")
        return False
    finally:
        session.close()
        
def listar_zapatos():
    """Consulta todos los zapatos."""
    session = Session()
    zapatos = session.query(Zapato).all()
    session.close()
    return zapatos

def buscar_zapato(zapato_id):
    """Busca un zapato mediante su ID."""
    session = Session()
    zapato = session.query(Zapato).filter_by(id=zapato_id).first()
    session.close()
    return zapato

def actualizar_precio(zapato_id, nuevo_precio):
    """Modifica el precio de un zapato."""
    session = Session()
    try:
        zapato = session.query(Zapato).filter_by(id=zapato_id).first()
        if zapato:
            zapato.precio = nuevo_precio
            session.commit()
            print(f"¡Precio actualizado con éxito para el ID {zapato_id}!")
            return True
        else:
            print(f"No se encontró ningún zapato con el ID {zapato_id}.")
            return False
    except Exception as e:
        session.rollback()
        print(f"Error al actualizar el precio: {e}")
        return False
    finally:
        session.close()

def eliminar_zapato(zapato_id):
    """Eliminar un zapato mediante su ID."""
    session = Session()
    try:
        zapato = session.query(Zapato).filter_by(id=zapato_id).first()
        if zapato:
            session.delete(zapato)
            session.commit()
            print(f"¡Zapato con ID {zapato_id} eliminado con éxito!")
            return True
        else:
            print(f"No se encontró ningún zapato con el ID {zapato_id}.")
            return False
    except Exception as e:
        session.rollback()
        print(f"Error al eliminar el zapato: {e}")
        return False
    finally:
        session.close()