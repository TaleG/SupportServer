#!/usr/bin/env python
#_*_ coding: utf-8 _*_
from app import db
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from .usersModels import Users_Models
from .rolesModels import Roles_Models

class Role_Users_Models(db.Model):
    """组和用户关联"""
    __tablename__ = "role_user"

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.ForeignKey(Users_Models.id))
    roleId = db.Column(db.ForeignKey(Roles_Models.id))


    def to_json(self):
        json_data = {
            "id": self.id,
            "userId": self.userId,
            "roleId": self.roleId,
            "userName": self.users.Name
        }
        return json_data
