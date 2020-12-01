from dataclasses import dataclass, field

from nova_api.entity import generate_id

from utils.entity.base import Base


@dataclass
class Telefone(Base):
    id_: str = field(default_factory=generate_id,
                     metadata={"primary_key": True})
    telefone: str = None
    usuario_id_: str = None
