#!/usr/bin/env python
#_*_ coding: utf-8 _*_
from app import db
from .usersModels import Users_Models
from .groupsModels import Groups_Models

class Group_Users_Models(db.Model):
    """组和用户关联"""
    __tablename__ = "group_user"

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.ForeignKey(Users_Models.id))
    groupId = db.Column(db.ForeignKey(Groups_Models.id))

    def to_json(self):
        json_data = {
            "id": self.id,
            "userId": self.userId,
            "groupId": self.groupId,
            "userName": self.users.Name
        }
        return json_data
