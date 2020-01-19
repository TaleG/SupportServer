#!/usr/bin/env python
#_*_ coding: utf-8 _*_
from app import db

class Permissions_Models(db.Model):
    """ 权限表 """
    __tablename__ = "permissions"

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(32), unique=True, nullable=False)
    Desc = db.Column(db.String(128))
    LinkRoles = db.relationship("Role_Permissions_Models", backref="permissions", lazy="dynamic")

    def to_json(self):
        json_data = {
            "id": self.id,
            "Name": self.Name,
            "Desc": self.Desc
        }
        return json_data