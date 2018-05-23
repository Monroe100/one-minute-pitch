from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import Category
from flas_login import LoginManager
#creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User)

if __name__ == '__main__':
    manager.run()