#!/usr/bin/env python
#_*_ coding: utf-8 _*_

import uuid
from flask import current_app, request, jsonify
from flask_restful import Resource
from app.models import Users_Models
from app.utils import RET, DB_Console

class User_Views(Resource, DB_Console):
    """ 用户视图 """
    def __init__(self):
        """初始化数据库自定义类"""
        super(User_Views, self).__init__(Database=Users_Models)

    def get(self, id):
        """
        按ID查找每条数据
        :param id:
        :return:
        """
        return self.By_Id_Get(id)

    def post(self):
        """
        添加用户
        :return:
        """

        req_data = request.get_json()
        # 初始化uuid
        suid = str(uuid.uuid4())

        try:
            Data = Users_Models(
                username=req_data.get("username"),
                Phone=req_data.get("userPhone"),
                Email=req_data.get("userEmail"),
                uuid=''.join(suid.split("-")),
                LoginIp=request.remote_addr,  # 获取登录IP
                Desc=req_data.get("userDesc")
            )
            # 在用户model中配置了用户是否填有名字，如果没有系统会随机创建一个。
            Data.name_info = req_data.get("Name")
            # 在用户model中创建了hash加密，所有创建的密码都会做成加密。
            Data.password_hash = req_data.get("password")

        except Exception as e:
            current_app.logger.error(e)
            return jsonify(RET.DATAERR)
        # 调用集成方法提交数据
        return self.DB_Commit(Data)

class User_List_Views(Resource, DB_Console):
    """用户查询视图"""
    def __init__(self):
        """初始化数据库自定义类"""
        super(User_List_Views, self).__init__(Database=Users_Models)
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

