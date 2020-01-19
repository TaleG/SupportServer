#!/usr/bin/env python
#_*_ coding: utf-8 _*_

from app import db

class Groups_Models(db.Model):
    """用户组"""
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(32), unique=True, nullable=False)
    Desc = db.Column(db.String(128))
    LinkUser = db.relationship("Group_Users_Models", backref="groups", lazy="dynamic")

    def to_json(self):
        json_data = {
            "id": self.id,
            "groupName": self.groupName,
            "groupDesc": self.groupDesc
        }
        return json_data