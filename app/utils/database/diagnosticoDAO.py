from datetime import datetime
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
    SELECT_QUERY = "SELECT {fields} FROM {table} " \
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

        query = self.SELECT_QUERY.format(
            fields=', '.join(fields +
                             list(usuario_dao.fields.values()) +
                             list(emissor_dao.fields.values())),
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
            field_names = list(self.fields.keys())
            field_names.remove('usuario')
            field_names.remove('emissor')
            values = {field: value
                      for field, value in zip(field_names,
                                              result[:len(fields) + 1])}
            values['usuario'] = Usuario(
                *result[len(field_names):len(field_names)+len(usuario_dao.fields)+1])
            values['emissor'] = Emissor(
                *result[len(field_names) + len(usuario_dao.fields):])
            return_list.append(Diagnostico(**values))

        query_total = self.database.QUERY_TOTAL_COLUMN.format(
            table=self.table,
            column=self.fields['usuario'])

        self.database.query(query_total)
        total = self.database.get_results()[0][0]
        self.logger.debug("Results are %s and the total in the database is %s",
                          results,
                          total)

        return total, return_list

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

    def update(self, entity: Diagnostico) -> str:
        """
        Updates an entity on the database.

        :param entity: The entity with updated values to update on \
        the database.
        :return: The id_ of the updated entity.
        """
        if not isinstance(entity, self.return_class):
            self.logger.error("Entity was not passed as an instance to update."
                              " Value received: %s", entity)
            raise TypeError(
                "Entity must be a {return_class} object!".format(
                    return_class=self.return_class
                )
            )

        if self.get_all(length=1, offset=0,
                        filters={"usuario": entity.usuario.id_,
                                 "emissor": entity.emissor.id_})[1][0] is None:
            self.logger.error("Entity was not found in database to update."
                              " Value received: %s", entity)
            raise AssertionError("Entity doesn't exists in database!")

        ent_values = entity.get_db_values()

        query = self.database.UPDATE_QUERY.format(
            table=self.table,
            fields=', '.join(
                [field + '=%s' for field in
                 self.fields.values()]),
            column=f"diagnostico_usuario_id_ = %s AND diagnostico_emissor_id_"
        )

        self.logger.debug("Running query in database: %s and params %s",
                          query,
                          ent_values + [entity.usuario.id_,
                                        entity.emissor.id_])
        row_count, _ = self.database.query(query,
                                           ent_values + [entity.usuario.id_,
                                                         entity.emissor.id_])

        if row_count == 0:
            self.logger.error("No rows were affected in database during "
                              "update!")
            raise NoRowsAffectedException()

        self.logger.info("Entity updated to %s", entity)
        return entity.id_
