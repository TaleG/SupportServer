#!/usr/bin/env python
#_*_ coding: utf-8 _*_
import random
from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from app import db

class Users_Models(db.Model):
    """ 用户表 """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(128))
    Name = db.Column(db.String(32), unique=True, nullable=False)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(128), unique=True, nullable=False)
    Email = db.Column(db.String(64))
    Phone = db.Column(db.String(11))
    LoginIp = db.Column(db.String(32))
    Desc = db.Column(db.String(128))
    LinkGroup = db.relationship("Group_Users_Models", backref="users", lazy="dynamic")
    LinkRole = db.relationship("Role_Users_Models", backref="users", lazy="dynamic")

    def to_json(self):
        json_data = {
            "id": self.id,
            "uuid": self.uuid,
            "name": self.Name,
            "username": self.username,
            "userEmail": self.Email,
            "userPhone": self.Phone,
            "userLoginIp": self.LoginIp,
            "userDesc": self.Desc
        }
        return json_data

    @property
    def name_info(self):
        """
        设置只读属性
        Python内置的@property装饰器就是负责把一个方法变成属性调用
        :return:
        """
        raise AttributeError("This property can only be set.not read.")


    @name_info.setter
    def name_info(self, value):
        """
        设置名字是否为空，如果是空会随机创建创建一个用户名。
        :param value:
        :return:
        """
        if value is None:
            ret = ''
            # 随机创建6位数
            for i in range(6):
                num = random.randint(0, 9)
                # 小写字母
                letter = chr(random.randint(97, 122))
                # 大写字母
                Letter = chr(random.randint(65, 90))
                s = str(random.choice([num, letter, Letter]))
                ret += s
            self.Name = ret
        else:
            self.Name = value


    @property
    def password_hash(self):
        """
        设置只读属性
        Python内置的@property装饰器就是负责把一个方法变成属性调用
        :return:
        """
        raise AttributeError("This property can only be set.not read.")

    @password_hash.setter
    def password_hash(self, value):
        """
        设置属性    account.password = 'XXX'
        :return: 设置属性时的数据  value就是"XXX"    源始明文密码
        """
        self.password = generate_password_hash(value)

    def check_password(self, passwd):
        """
        检验密码的正确证
        :param passwd: 用户登录时填写的原始密码
        :return: 如果正确返回True，否则返回False
        """
        return check_password_hash(self.password, passwd)

    # 为token串设置有效期设置expiration单位为秒，1小时=3600秒
    def generate_auth_token(self, expiration=3600 * 2):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        token = s.dumps({'id': self.id, "name": self.Name, "uuid": self.uuid}).decode('ascii')
        return token