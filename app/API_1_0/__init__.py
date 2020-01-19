#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Blueprint
from flask_restful import Api
from . import begins
from .views import User_Views, User_List_Views, Group_Views, Group_List_Views, Roles_Views, Roles_List_Views,\
    Login_Auth_Views, Permission_Views, User_Group_Views, Role_User_Views, Role_Permissions_Views

# 创建蓝图对象
api_bp = Blueprint("api_1_0", __name__)
api = Api(api_bp)

api.add_resource(begins.Begins, '/begin', endpoint='begin')

# 用户验证
api.add_resource(Login_Auth_Views, '/loginauth', endpoint='loginauth')

# 用户
api.add_resource(User_Views, '/account', '/account/<int:id>', endpoint='account')
api.add_resource(User_List_Views, '/userslist', endpoint='userslist')

# 用户组
api.add_resource(Group_Views, '/group', '/group/<int:id>', endpoint="group")
api.add_resource(Group_List_Views, "/groupslist", endpoint="groupslist")

# 用户和用户组关联
api.add_resource(User_Group_Views, '/usergroup/<int:id>', endpoint='usergroup')

# 用户和角色关联
api.add_resource(Role_User_Views, '/roleuser/<int:id>', endpoint='roleuser')

# 角色和权限关联
api.add_resource(Role_Permissions_Views, '/rolepermissions/<int:id>', endpoint='rolepermissions')

# 角色
api.add_resource(Roles_Views, '/role', '/role/<int:id>', endpoint="role")
api.add_resource(Roles_List_Views, '/roleslist', endpoint="roleslist")

# 权限
api.add_resource(Permission_Views, '/permissions', '/permissions/<int:id>', endpoint='permissions')