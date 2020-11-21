from dataclasses import dataclass, field


@dataclass
class Email:
    id_: int = field(default=None)
    email: str = None
    usuario_id_: str = None
    primario: bool = False
