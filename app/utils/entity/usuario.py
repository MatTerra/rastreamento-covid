from dataclasses import dataclass, field
from datetime import datetime, date
from secrets import token_bytes
from base64 import b64decode, b64encode

from cryptography.hazmat.primitives.hashes import SHA3_512, Hash

from nova_api.entity import generate_id


def generate_salt() -> str:
    """ Generate a 24 bytes salt for password hashing

    :return: str in base64 of the salt
    """
    return b64encode(token_bytes(24)).decode('ascii')


def hash_password(password: str, salt: str) -> str:
    """ Generates the password hash for the given user

    :param password: The password to hash
    :param salt: The salt(base64) to use in hash
    :return: The password hash
    """
    hash_ = Hash(SHA3_512())
    hash_.update(password.encode('ascii')+b64decode(salt.encode('ascii')))
    digest = hash_.finalize()
    hash_ = Hash(SHA3_512())
    hash_.update(digest)
    digest = hash_.finalize()
    hash_ = Hash(SHA3_512())
    hash_.update(digest+b64decode(salt.encode('ascii')))
    digest = hash_.finalize()
    return b64encode(digest).decode('ascii')


@dataclass
class Usuario:
    id_: str = field(default_factory=generate_id,
                     metadata={"primary_key": True})
    ord: int = field(default=None)
    salt: str = field(default_factory=generate_salt)
    password: str = field(default="")
    primeiro_nome: str = field(default="")
    ultimo_nome: str = field(default="")
    consentimento: bool = field(default=False)
    data_nascimento: date = field(default_factory=datetime.now)

    def __post_init__(self):
        if not isinstance(self.data_nascimento, datetime):
            self.data_nascimento = datetime.strptime(self.data_nascimento,
                                                     "%Y-%m-%d")
        if not self.password.endswith('=='):
            self.password = hash_password(password=self.password,
                                          salt=self.salt)
