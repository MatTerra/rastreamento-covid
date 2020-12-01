from dataclasses import dataclass, Field, fields
from datetime import date, datetime

from nova_api.entity import Entity


@dataclass
class Base:
    id_: str = None

    @staticmethod
    def _serialize_field(field_: Field):
        """

        :param field_:
        :return:
        """
        if isinstance(field_, Base):
            return field_.id_
        if isinstance(field_, datetime):
            return field_.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(field_, date):
            return field_.strftime("%Y-%m-%d")
        return field_

    def get_db_values(self) -> list:
        """Returns all attributes to save in database with formatted values.

        Goes through the fields in the entity and converts them to the
        expected value to save in the database. For example: datetime
        values are converted to string with the specific sql format.

        Also verifies if a field contains in metadata `database=False` and
        excludes it from the list if so. Default for `database` is True.

        :return: Serialized values to save in database
        """
        return [Base._serialize_field(self.__getattribute__(field_.name))
                for field_ in fields(self)
                if field_.metadata.get("database", True)]
