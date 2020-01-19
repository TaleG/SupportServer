#!/usr/bin/env python
#_*_ coding: utf-8 _*_
from app import db

class Roles_Models(db.Model):
    """ 权限表 """
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(32), unique=True, nullable=False)
    Desc = db.Column(db.String(128))
    LinksUsers = db.relationship("Role_Users_Models", backref="roles", lazy="dynamic")
    LinkPermissions = db.relationship("Role_Permissions_Models", backref="roles", lazy="dynamic")

    
    def to_json(self):
        json_data = {
            "id": self.id,
            "roleName": self.Name,
            "roleDesc": self.Desc
        }
        return json_data