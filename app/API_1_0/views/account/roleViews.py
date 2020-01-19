#!/usr/bin/env python
#_*_ coding: utf-8 _*_

from flask import request, jsonify, current_app
from flask_restful import Resource
from app.models import Roles_Models
from app.utils import RET, DB_Console
from app.utils import login_required

class Roles_Views(Resource, DB_Console):
    """权限视图"""
    def __init__(self):
        """初始化数据库自定义类"""
        super(Roles_Views, self).__init__(Database=Roles_Models)

    @login_required
    def get(self, id, method="get"):
        """
        查询所有数据
        :return:
        """
        return self.By_Id_Get(id=id)

    def post(self, method="post"):
        req_data = request.get_json()

        try:
            Data = Roles_Models(
                Name=req_data.get("Name"),
                Desc=req_data.get("Desc")
            )
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DATAERR, codemsg='Data Error.')
        return self.DB_Commit(Data)

class Roles_List_Views(Resource, DB_Console):
    """数据查询视图"""
    def __init__(self):
        """初始化数据库自定义类"""
        super(Roles_List_Views, self).__init__(Database=Roles_Models)

    def get(self, method="get"):
        """
        按ID查找每条数据
        :param id:
        :return:
        """
        req_data = request.get_json()
        Name = req_data.get("Name")
        return self.Get_Data(Name)

    def post(self, method="post"):
        """
        分页显示数据
        :param pageSize:
        :param currentPage:
        :return:
        """
        req_data = request.get_json()
        pageSize = req_data.get("pageSize")
        currentPage = req_data.get("currentPage")
        return self.Page_Data(pageSize=pageSize, currentPage=currentPage)


