#!/usr/bin/env python
#_*_ coding: utf-8 _*_
from flask import request, jsonify, current_app
from flask_restful import Resource
from app.models import Groups_Models
from app.utils import RET, DB_Console

class Group_Views(Resource, DB_Console):
    """组视图"""
    def __init__(self):
        """初始化数据库自定义类"""
        super(Group_Views, self).__init__(Database=Groups_Models)

    def get(self, id):
        """
        按数据ID查询信息
        :param id:
        :return:
        """
        return self.By_Id_Get(id=id)

    def post(self):
        """
        添加组数据
        :return:
        """
        req_data = request.get_json()
        try:
            Data = Groups_Models(
                Name=req_data.get("Name"),
                Desc=req_data.get("Desc")
            )
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DATAERR, codemsg="Data Error.")

        return self.DB_Commit(Data)

class Group_List_Views(Resource, DB_Console):
    """组数据查询视图"""
    def __init__(self):
        """初始化数据库自定义类"""
        super(Group_List_Views, self).__init__(Database=Groups_Models)

    def get(self):
        """
        按ID查找每条数据
        :param id:
        :return:
        """
        req_data = request.get_json()
        Name = req_data.get("Name")
        return self.Get_Data(Name)

    def post(self):
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
