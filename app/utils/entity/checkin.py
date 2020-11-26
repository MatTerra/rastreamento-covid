from datetime import datetime
from dataclasses import dataclass, field

from nova_api.entity import generate_id

from utils.entity.base import Base

@dataclass
class Checkin(Base):
    id_: str = field(default_factory=generate_id,
                     metadata={"primary_key": True})
    risco: int = field(default=0)

    inicio: datetime = field(default_factory=datetime.now)
    final: datetime = field(default_factory=datetime.now)

    usuario_id_: str = None
    local_id_: str = None