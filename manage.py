#coding:utf-8
from flask_script import Manager
from SparkIdeaMain import app
from flask_migrate import Migrate,MigrateCommand
from extensions import db

manager = Manager(app)

migrate = Migrate(app,db)

#add without @!!!!!!
manager.add_command('db',MigrateCommand)
#init once
#migrate when model change
#upgrade when model change

#create with @!!!!!!
@manager.command
def test():
    print "flask_script test is working!"




if __name__ == '__main__':
    manager.run()