from app import create_app,db
from flask_script import Manager,Server
<<<<<<< HEAD
from app.models import User,Category,Peptalk,Comments
from  flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager



# Creating app instances

app = create_app('production')

manager = Manager(app)
manager.add_command('server',Server)

#Migration
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
=======

# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
    """Run the unit tests.
    """
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

# from app import create_app,db
# from flask_script import Manager,Server
from app.models import Category,User,Peptalk,Comments
# from  flask_migrate import Migrate, MigrateCommand
# from flask_login import LoginManager



# # Creating app instances
# # app = create_app('development')
# app = create_app('production')

# manager = Manager(app)
# manager.add_command('server',Server)

# #Migration
# migrate = Migrate(app,db)
# manager.add_command('db',MigrateCommand)
>>>>>>> c74fb1c5c010f7302e5447fd11140ed96877d666

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, Category = Category, User = User, Peptalk = Peptalk, Comments = Comments)


if __name__ == '__main__':
<<<<<<< HEAD
    manager.run()
=======
    manager.run()


>>>>>>> c74fb1c5c010f7302e5447fd11140ed96877d666
