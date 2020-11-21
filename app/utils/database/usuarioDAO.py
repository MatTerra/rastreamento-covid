from nova_api.dao.generic_sql_dao import GenericSQLDAO
from nova_api.persistence.postgresql_helper import PostgreSQLHelper

from utils.database.emailDAO import EmailDAO
from utils.entity.usuario import Usuario


class UsuarioDAO(GenericSQLDAO):
    def __init__(self, database_instance=None):
        super().__init__(database_instance=database_instance,
                         table="usuario",
                         prefix="usuario_",
                         database_type=PostgreSQLHelper,
                         return_class=Usuario)

    def create(self, entity: Usuario) -> str:
        super(UsuarioDAO, self).create(entity)
        email_dao = EmailDAO(database_instance=self.database)
        try:
            for email in entity.emails:
                email_dao.create(email)
        except:
            self.remove(entity)
            raise IOError("Not able to insert user")

    def select_from_email(self, email: str) -> Usuario:
        query = "select {fields} from {table} LEFT JOIN email " \
                "ON email_usuario_id_=usuario_id_ WHERE email_email={filter};"
        query_to_run = query.format(
            fields=', '.join(self.fields.values()),
            table=self.table,
            filter='%s'
        )
        self.database.query(query_to_run, [email])

        results = self.database.get_results()

        if results is None:
            self.logger.info("No results found for query %s, %s in get_all. "
                             "Returning none", query_to_run, [email])
            return None

        return_list = [self.return_class(*result) for result in results]

        return return_list[0]