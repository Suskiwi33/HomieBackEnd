from vivienda import Vivienda
from usuario import Usuario
from db_conexion import coneccion_bd
from typing import List, Tuple

class viviendaDAO:
    def __init__(self):
        self.__db = None
        self._user = None
        self._password = None
        
    def login(self, user):
        """Connect to the database and store credentials for reconnection."""
        self._user = user.getUsername()
        self._password = user.getPassword()
        dbconnector = coneccion_bd(self._user, self._password)
        self.__db = dbconnector.connectToDB()
        
    def insertVievienda(self, vivienda: Vivienda):
        self.ensure_connection()
        with self.db.cursor() as dbCursor:
            sql =  """
        INSERT INTO vivienda (
        nombre, balcony, bath_num, `condition`, floor, garage, garden, 
        ground_size, house_type, lift, loc_city, loc_district, loc_neigh, 
        m2_real, price, room_numbers, swimming_pool, terrace, unfurnished, usuario_id
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
            values = (
    vivienda.getNombre(),
    vivienda.getBalcony(),
    vivienda.getBathNum(),
    vivienda.getCondition(),
    vivienda.getFloor(),
    vivienda.getGarage(),
    vivienda.getGarden(),
    vivienda.getGroundSize(),
    vivienda.getHouseType(),
    vivienda.getLift(),
    vivienda.getLocCity(),
    vivienda.getLocDistrict(),
    vivienda.getLocNeigh(),
    vivienda.getM2Real(),
    vivienda.getPrice(),
    vivienda.getRoomNumbers(),
    vivienda.getSwimmingPool(),
    vivienda.getTerrace(),
    vivienda.getUnfurnished(),
    vivienda.getIdUsuario()
    )
            dbCursor.execute(sql, values)
            self.db.commit()
            return self.checkRows(dbCursor.rowcount)