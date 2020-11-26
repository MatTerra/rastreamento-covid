from dataclasses import dataclass, field

from nova_api.entity import generate_id

from utils.entity.base import Base


@dataclass
class Local(Base):
    id_: str = field(default_factory=generate_id,
                     metadata={"primary_key": True})
    nome: str = field(default="")
    latitude: str = field(default="")
    longitude: str = field(default="")
    ord: int = field(default=None, metadata={"database": False})
