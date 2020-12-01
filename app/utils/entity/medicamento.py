from dataclasses import dataclass, field

from nova_api.entity import generate_id

from utils.entity.base import Base

@dataclass
class Medicamento(Base):
    id_: str = field(default_factory=generate_id,
                     metadata={"primary_key": True})
    nome: str = field(default="")
