import sys, os
sys.path.append('/root/dev/app')
from consts import consts
from tools import log


def ExceptionLine():
    import linecache
    import sys
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return f"{filename}:{lineno} => {line.strip()}"


def set_db(name):
    global db_name
    db_name = name


def db():
    try:
        from pymongo import MongoClient
        MONGO_CONNECTION = os.getenv('MONGO')
        log.info(f'MONGO_CONNECTION: {MONGO_CONNECTION}')
        if MONGO_CONNECTION is None:
            con = MongoClient(f'mongodb://localhost:{consts.MONGODB_PORT}')
        else:
            con = MongoClient('mongodb://' + MONGO_CONNECTION)
        return con[consts.DB_NAME]
    except:
        log.error(f'Error connecting database: {ExceptionLine()}')
    return None

