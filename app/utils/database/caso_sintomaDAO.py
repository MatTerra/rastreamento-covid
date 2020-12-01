from nova_api.dao.generic_sql_dao import GenericSQLDAO
from nova_api.persistence.postgresql_helper import PostgreSQLHelper

from utils.entity.caso_sintoma import CasoSintoma

class CasoSintomaDAO(GenericSQLDAO):
    def __init__(self, database_instance=None):
        super().__init__(database_instance=database_instance,
                         table='caso_sintoma',
                         database_type=PostgreSQLHelper,
                         return_class=CasoSintoma)
