from dataclasses import dataclass, field

from nova_api.entity import generate_id

from utils.entity.base import Base

@dataclass
class Notificacao(Base):
    id_: str = field(default=None, metadata={"primary_key": True})
    recebida: bool = field(default=False)