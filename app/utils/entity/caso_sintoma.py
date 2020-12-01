from datetime import date
from dataclasses import dataclass, field

from nova_api.entity import generate_id

from utils.entity.base import Base

@dataclass
class CasoSintoma(Base):
    id_: str = field(default_factory=generate_id,
                     metadata={"primary_key": True})
    usuario_id_: str = field(default="")
    sintoma_id_: int = field(default=0)
    inicio: date = field(default_factory=date.today)
    final: date = field(default=None)
