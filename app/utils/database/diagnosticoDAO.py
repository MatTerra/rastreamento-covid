from typing import List

from nova_api.dao.generic_sql_dao import GenericSQLDAO
from nova_api.exceptions import NoRowsAffectedException
from nova_api.persistence.postgresql_helper import PostgreSQLHelper

from utils.database.emissorDAO import EmissorDAO
from utils.database.usuarioDAO import UsuarioDAO
from utils.entity.diagnostico import Diagnostico
from utils.entity.emissor import Emissor
from utils.entity.usuario import Usuario


class DiagnosticoDAO(GenericSQLDAO):
    SELECT_QUERY = "SELECT {fields} FROM `{table}` " \
                   "LEFT JOIN usuario " \
                   "ON diagnostico_usuario_id_ = usuario_id_ " \
                   "LEFT JOIN emissor " \
                   "ON diagnostico_emissor_id_ = emissor_id_" \
                   " {filters} " \
                   "LIMIT %s OFFSET %s;"

    def __init__(self, database_instance=None):
        super().__init__(database_instance=database_instance,
                         table='diagnostico',
                         database_type=PostgreSQLHelper,
                         return_class=Diagnostico)
        self.fields['usuario'] = self.prefix + 'usuario_id_'
        self.fields['emissor'] = self.prefix + 'emissor_id_'

    def get_all(self, length: int = 20, offset: int = 0,
                filters: dict = None) -> (int, List[Diagnostico]):
        self.logger.debug("Getting all with filters %s limit %s and offset %s",
                          filters, length, offset)
        usuario_dao = UsuarioDAO(database_instance=self.database)
        emissor_dao = EmissorDAO(database_instance=self.database)

        filters_, query_params = ('', list()) \
            if not filters \
            else self.generate_filters(filters)

        fields = list(self.fields.values())
        fields.remove(self.fields['usuario'])
        fields.remove(self.fields['emissor'])

        query = self.database.SELECT_QUERY.format(
            fields=', '.join(self.fields.values() +
                             usuario_dao.fields.values() +
                             emissor_dao.fields.values()),
            table=self.table,
            filters=filters_
        )

        self.logger.debug("Running query in database %s with params %s",
                          query,
                          [*query_params, length, offset])
        self.database.query(query, [*query_params, length, offset])
        results = self.database.get_results()

        if results is None:
            self.logger.info("No results found for query %s, %s in get_all. "
                             "Returning none", query, [*query_params,
                                                       length, offset])
            return 0, []

        return_list = []
        for result in results:
            values = {field: value
                      for field, value in zip(fields,
                                              result[:len(fields) + 1])}
            values['usuario'] = Usuario(
                *result[len(fields):len(fields)+len(usuario_dao.fields)+1])
            values['emissor'] = Emissor(
                *result[len(fields) + len(usuario_dao.fields):])
            return_list.append(Diagnostico(**values))

        query_total = self.database.QUERY_TOTAL_COLUMN.format(
            table=self.table,
            column=self.fields['id_'])

        self.database.query(query_total)
        total = self.database.get_results()[0][0]
        self.logger.debug("Results are %s and the total in the database is %s",
                          results,
                          total)

        return total, results

    def get(self, id_: str) -> List[Diagnostico]:
        _, results = self.get_all(filters={"usuario": id_})
        return results

    def create(self, entity: Diagnostico) -> str:
        """
        Creates a new row in the databse with data from `entity`.

        :param entity: The instance to save in the database.
        :return: The entity uuid.
        """
        if not isinstance(entity, Diagnostico):
            self.logger.error("Entity was not passed as an instance to create."
                              " Value received: %s", entity)
            raise TypeError(
                "Entity must be a {entity} object!".format(
                    entity=self.return_class.__name__
                )
            )

        ent_values = entity.get_db_values()

        query = self.database.INSERT_QUERY.format(
            table=self.table,
            fields=', '.join(self.fields.values()),
            values=', '.join(['%s'] * len(ent_values)))

        self.logger.debug("Running query in database: %s and params %s",
                          query,
                          ent_values)
        row_count, _ = self.database.query(query, ent_values)

        if row_count == 0:
            self.logger.error("No rows were affected in database during "
                              "create!")
            raise NoRowsAffectedException()

        self.logger.info("Entity created as %s", entity)

        return entity.id_
