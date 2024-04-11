import os
from types import ModuleType

from dotenv import load_dotenv

load_dotenv()


class MetaEnv(type):
    @classmethod
    def _get_env_vars(mcs, var_name):  # type: ignore
        value = os.getenv(var_name)
        if value is None:
            raise ValueError(f"{var_name} is not defined in .env")
        return value

    @property
    def DATABASE_URL(cls):
        return cls._get_env_vars("DATABASE_URL")

    @property
    def SECRET_KEY(cls):
        return cls._get_env_vars("SECRET_KEY")

    @property
    def ALGORITHM(cls):
        return cls._get_env_vars("ALGORITHM")

    @property
    def FAKE_PASSWORD(cls):
        return cls._get_env_vars("FAKE_PASSWORD")

    @property
    def CLOUDINARY_CLOUD_NAME(cls):
        return cls._get_env_vars("CLOUDINARY_CLOUD_NAME")

    @property
    def CLOUDINARY_API_KEY(cls):
        return cls._get_env_vars("CLOUDINARY_API_KEY")

    @property
    def CLOUDINARY_API_SECRET(cls):
        return cls._get_env_vars("CLOUDINARY_API_SECRET")

    @property
    def ORIGINS(cls):
        return cls._get_env_vars("ORIGINS").split(",")


class Env(ModuleType, metaclass=MetaEnv):
    pass


__all__ = ["Env"]
