#!/usr/bin/env python
#_*_ coding: utf-8 _*_

from flask import jsonify, current_app
from sqlalchemy.exc import IntegrityError
from app import db
from app.utils import RET

class DB_Console(object):
    """ 数据库操作 """
    def __init__(self, Database):
        self.Database = Database

    def Count_Data(self):
        """
        计算数据总数量
        :return:
        """
        try:
            Count = db.session.query(self.Database).count()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Database Error.")
        return Count

    def By_Id_Get(self, id):
        """
        按ID操作数据库（单条）查询
        :param id:
        :return:
        """
        try:
            Data = db.session.query(self.Database).filter_by(id=id).first()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Databaes Error.")
        try:
            Data_Info = Data.to_json()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.NODATA, codemsg="Select is None.")
        return jsonify(code=RET.OK, codemsg="Succeed.", data=Data_Info)

    def By_Id_All_Get(self, id):
        """
        按ID操作数据库(所有)查询
        :param id:
        :return:
        """
        DataList = []
        try:
            Data = db.session.query(self.Database).filter_by(groupId=id).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Databaes Error.")
        for DataInfo in Data:
            DataList.append(DataInfo.to_json())

        return jsonify(code=RET.OK, codemsg="Succeed.", data=DataList)

    # def Get_All_Data(self):
    #     """
    #     查看数据库所有数据
    #     :return:
    #     """
    #     try:
    #         Data = db.session.query(self.Database).all()
    #     except Exception as e:
    #         current_app.logger.error(e)
    #         return jsonify(code=RET.DBERR, codemsg="Database Error.")
    #     return Data

    def DB_Commit(self, Data):
        """
        添加数据到数据库
        :param Data:
        :return:
        """
        try:
            db.session.add(Data)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(code=RET.DATAEXIST, codemsg="Data Exist or Parameter Error.")
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Database Error.")
        return jsonify(code=RET.OK, codemsg="Succeed.")

    def Page_Data(self, pageSize, currentPage):
        """
        按分页查询数据
        :param pageSize:
        :param currentPage:
        :return:
        """
        PageList = []
        try:
            Data = db.session.query(self.Database).limit(pageSize).offset((currentPage - 1) * pageSize)
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Select Page Error")

        for DataInfo in Data:
            PageList.append(DataInfo.to_json())

        return jsonify(code=RET.OK, codemsg="Succeed.", data=PageList, total=self.Count_Data())

    def Get_Data(self, DataName):
        """

        :param DataName:
        :return:
        """
        DataList = []
        try:
            Data = db.session.query(self.Database).filter(self.Database.Name.like(DataName + "%")).all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Database Error.")

        for DataInfo in Data:
            DataList.append(DataInfo.to_json())
        return jsonify(code=RET.OK, codemsg="Succeed.", data=DataList, total=len(DataList))
