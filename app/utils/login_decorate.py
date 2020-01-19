#!/usr/bin/env python
#_*_ coding: utf-8 _*_

from functools import wraps
import inspect
from flask import jsonify, request, current_app
from app.utils import RET
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature
from app.models import Role_Users_Models, Role_Permissions_Models
from app import db

def login_required(view_func):
    """
    用户登录检测装饰器
    :param view_func:
    :return:
    """
    @wraps(view_func)
    def wrapper(*args, **kwargs):

        # 判断用户是否有登录
        try:
            tokens = request.headers["X-CSRFToken"]
        except Exception:
            return jsonify(code=RET.SESSIONERR, codemsg="Http RespError")
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            # g.data = s.loads(tokens)
            data = s.loads(tokens)
            user_id = data.get("id")

            # 判断此用户是否有权限操作
            inspect_res = inspect.getcallargs(view_func, *args, **kwargs)
            # 获取到当前方法的method类型，为了和用户的所属权限相匹配。
            method_type = inspect_res.get("method")
            try:
                # 以该ID查出该用户的角色
                UserData = db.session.query(Role_Users_Models).filter_by(userId=user_id).first()
            except Exception as e:
                current_app.logger.error(e)
                return jsonify(code=RET.DBERR, codemsg="Database Error.")
            # 从用户数据中拿到该用户的角色ID
            roleId = UserData.to_json().get("roleId")

            try:
                # 通过角色ID获取该角色的所有权限
                PermissionData = db.session.query(Role_Permissions_Models).filter_by(roleId=roleId).all()
            except Exception as e:
                current_app.logger.error(e)
                return jsonify(code=RET.DBERR, codemsg="Database Error.")

            DataList = []
            for DataInfo in PermissionData:
                # 获取该角色的所有权限，在字典中找出permissionName字段。
                DataList.append(DataInfo.to_json().get("PermissionName"))

            # 判断该用户权限中是否有对该方法有操作权限。
            if method_type not in DataList:
                return jsonify(code=RET.PERMISSIONSERR, codemsg="Permissions Error")

            return view_func(*args, **kwargs)

        except SignatureExpired:
            return jsonify(code=RET.SESSIONERR, codemsg="Token Signature Error")
        except BadSignature:
            return jsonify(code=RET.SESSIONERR, codemsg="Token BadSignatury Error.")

    return wrapper
