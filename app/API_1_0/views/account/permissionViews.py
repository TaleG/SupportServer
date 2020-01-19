#!/usr/bin/env python
#_*_ coding: utf-8 _*_

from flask import request, jsonify, current_app
from flask_restful import Resource
from app.models import Permissions_Models
from app.utils import RET, DB_Console

class Permission_Views(Resource, DB_Console):
    """权限视图"""
    def __init__(self):
        """初始化数据库自定义类"""
        super(Permission_Views, self).__init__(Database=Permissions_Models)

    def post(self):
        req_data = request.get_json()

        try:
            Data = Permissions_Models(
                Name=req_data.get("Name"),
                Desc=req_data.get("Desc")
            )
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DATAERR, codemsg='Data Error.')
        return self.DB_Commit(Data)