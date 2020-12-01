from nova_api.dao.generic_sql_dao import GenericSQLDAO
from nova_api.persistence.postgresql_helper import PostgreSQLHelper

from utils.entity.telefone import Telefone

class TelefoneDAO(GenericSQLDAO):
    def __init__(self, database_instance=None):
        super().__init__(database_instance=database_instance,
                         table='telefone',
                         database_type=PostgreSQLHelper,
                         return_class=Telefone)
