import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or ""
    port = dbinfo.get("PORT") or ""
    name = dbinfo.get("NAME") or ""

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    DEBUGE = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "Kenevy"

    SESSION_TYPE = 'redis'      # 将 session存在redis中
    # SESSION_REDIS = '127.0.0.1:6379'  # 可以连接远程redis库
    SESSION_COOKIE_SECURE = True
    SESSION_USE_SIGNER = True   # 将 key 加密


class DevelopConfig(Config):
    DEBUGE = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "db_user",
        "PASSWORD": "eSD2mmrj6kHGRA8Y",
        "HOST": "122.51.240.250",
        "PORT": "3306",
        "NAME": "db_user",

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestConfig(Config):
    TESTING = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "db_user",
        "PASSWORD": "eSD2mmrj6kHGRA8Y",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "db_user",

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "db_user",
        "PASSWORD": "eSD2mmrj6kHGRA8Y",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "db_user",

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "db_user",
        "PASSWORD": "eSD2mmrj6kHGRA8Y",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "db_user",

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)



envs = {
    "develop": DevelopConfig,
    "testing": TestConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}