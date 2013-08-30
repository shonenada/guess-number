from tornado.options import options
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class Database(object):

    app = None
    base = None
    engine = None
    session = None

    def __init__(self, app=None):
        self.base = declarative_base()
        if app:
            self.bind_app(app)

    def bind_app(self, app):
        self.app = app
        self.engine = self.create_db_engine()
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_tables(self):
        if self.base and self.engine:
            from rseader.account.model import Account
            self.base.metadata.create_all(self.engine)

    def drop_tables(self):
        if self.base and self.engine:
            self.base.metadata.drop_all(self.engine)

    def create_db_engine(self):
        """Create a sqlalchemy engine"""
        if hasattr(options, "db_params"):
            params = dict(options.db_params)
        else:
            params = {}
        info = self._get_db_config()
        url = self._generate_db_url(info)
        if url:
            return create_engine(url, **params)
        else:
            return None

    def _get_db_config(self):
        """Just get database configs from toronda.options"""
        db_type = self.get_option("db_type")
        host = self.get_option("db_host")
        port = self.get_option("db_port")
        user = self.get_option("db_user")
        passwd = self.get_option("db_passwd")
        name = self.get_option("db_name")
        return {"type": db_type, "host": host, "port": port, "user": user,
                "passwd": passwd, "name": name}

    def _generate_db_url(self, info):
        '''Generate a db url based on tornado.options'''
        if 'type' in info:
            db_type = info['type']
        else:
            db_type = None
        if db_type == 'sqlite':
            url = Sqlite(info).generate_url()
        elif db_type == 'mysql':
            url = Mysql(info).generate_url()
        elif db_type == 'pgsql':
            url = Pgsql(info).generate_url()
        else:
            url = None
        return url

    def get_option(self, attr):
        if hasattr(options, attr):
            return getattr(options, attr)
        else:
            return None


class Sqlite(object):

    def __init__(self, info):
        self.name = info['name']

    def generate_url(self):
        if self.name:
            url = 'sqlite:///%s' % self.name
        else:
            url = 'sqlite://'  # Using memory
        return url


class Mysql(object):

    def __init__(self, info):
        self.name = info['name']
        self.user = info['user']
        self.host = info['host']
        if 'port' in info:
            self.port = str(info['port'])
        else:
            self.port = '3306'
        if 'passwd' in info:
            self.passwd = info['passwd']
        else:
            self.passwd = ''

    def generate_url(self):
        if not self.passwd is None:
            url = 'mysql://%s:%s' % (self.user, self.passwd)
        else:
            url = 'mysql://%s' % self.user
        url = url + ('@%s:%s/%s' % (self.host, self.port, self.name))
        return url


class Pgsql(object):

    def __init__(self, info):
        self.name = info['name']
        self.user = info['user']
        self.host = info['host']
        if 'port' in info:
            self.port = str(info['port'])
        else:
            self.port = '5432'
        if 'passwd' in info:
            self.passwd = info['passwd']
        else:
            self.passwd = ''

    def generate_url(self):
        if not self.passwd is None:
            url = 'postgresql://%s:%s' % (self.user, self.passwd)
        else:
            url = 'postgresql://%s' % self.user
        url = url + ("@%s:%s/%s" % (self.host, self.port, self.name))
        return url