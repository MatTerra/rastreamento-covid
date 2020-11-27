from dataclasses import dataclass, field
from datetime import date

from dateutil.utils import today

from utils.entity.base import Base
from utils.entity.emissor import Emissor
from utils.entity.usuario import Usuario


@dataclass
class Diagnostico(Base):
    id_: None = field(default=None, compare=False,
                      metadata={"database": False})
    usuario: Usuario = field(default=None, metadata={"primary_key": True})
    emissor: Emissor = field(default=None, metadata={"primary_key": True})
    data_exame: date = field(default_factory=today)
    data_inicio_sintomas: date = field(default_factory=today)
    data_fim_sintomas: date = None
    data_recuperacao: date = None