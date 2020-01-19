#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask_restful import Resource
from app.models import *
class Begins(Resource):
    def get(self):
        """
        测试页
        :return:
        """
        return "Hello Begine Flask."