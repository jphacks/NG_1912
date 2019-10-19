import os
import environ

# ENV = ".production"
ENV = ".local"

ROOT_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DOTENVS_DIR_PATH = os.path.join(ROOT_DIR_PATH, ".envs", ENV)
DOTENV_FILE_PATH = os.path.join(ROOT_DIR_PATH, ".env")


with open(DOTENV_FILE_PATH, "w") as output_file:
    # Django
    # ----------------------------------------------------------------
    DJANGO_FILE_PATH = os.path.join(DOTENVS_DIR_PATH, ".django")
    with open(DJANGO_FILE_PATH, "r") as django_file:
        django_file_content = django_file.read()
        output_file.write(django_file_content)
        output_file.write(os.linesep)

    # MySQL
    # ----------------------------------------------------------------
    pref = """
# MySQL
# ------------------------------------------------------------------------------
"""
    output_file.write(pref)

    POSTGRES_FILE_PATH = os.path.join(DOTENVS_DIR_PATH, ".mysql")
    env = environ.Env()
    env.read_env(POSTGRES_FILE_PATH)
    POSTGRES_USER = env('MYSQL_USER')
    POSTGRES_PASSWORD = env('MYSQL_PASSWORD')
    POSTGRES_HOST = env('MYSQL_HOST')
    POSTGRES_PORT = env('MYSQL_PORT')
    POSTGRES_DB = env('MYSQL_DB')

    db_url = "DATABASE_URL=mysql://" + POSTGRES_USER + ":" + POSTGRES_PASSWORD + "@" + \
             POSTGRES_HOST + ":" + POSTGRES_PORT + "/" + POSTGRES_DB

    output_file.write(db_url)
    output_file.write(os.linesep)
