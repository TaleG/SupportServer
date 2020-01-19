#!/usr/bin/env python
#_*_ coding: utf-8 _*_
from flask import current_app, request, jsonify
from flask_restful import Resource
from app.models import Role_Users_Models
from app.utils import RET, DB_Console
from app import db

class Role_User_Views(Resource, DB_Console):
    def __init__(self):
        super(Role_User_Views, self).__init__(Database=Role_Users_Models)

    def get(self, id):
        """
        按groupId查询所有组内用户
        :return:
        """

        DataList = []
        try:
            Data = db.session.query(self.Database).filter_by(roleId=id).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Databaes Error.")
        for DataInfo in Data:
            DataList.append(DataInfo.to_json())

        return jsonify(code=RET.OK, codemsg="Succeed.", data=DataList)