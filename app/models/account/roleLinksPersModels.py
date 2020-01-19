#!/usr/bin/env python
#_*_ coding: utf-8 _*_
from app import db
from .permissionsModels import Permissions_Models
from .rolesModels import Roles_Models

class Role_Permissions_Models(db.Model):
    """组和用户关联"""
    __tablename__ = "role_permissions"

    id = db.Column(db.Integer, primary_key=True)
    permissionsId = db.Column(db.ForeignKey(Permissions_Models.id))
    roleId = db.Column(db.ForeignKey(Roles_Models.id))

    def to_json(self):
        json_data = {
            "id": self.id,
            "permissionsId": self.permissionsId,
            "roleId": self.roleId,
            "PermissionName": self.permissions.Name
        }
        return json_data

