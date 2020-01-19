#!/usr/bin/env python
#_*_ coding: utf-8 _*_
from app import Create_APP, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS

app = Create_APP("develop")
CORS(app)

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
