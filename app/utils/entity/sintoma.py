from dataclasses import dataclass, field

from nova_api.entity import generate_id

from utils.entity.base import Base

@dataclass
class Sintoma(Base):
    id_: str = field(default_factory=generate_id,
                     metadata={"primary_key": True})
    descricao: str = field(default="")
    risco: int = field(default=0)
