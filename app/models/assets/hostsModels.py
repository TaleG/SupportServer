#!/usr/bin/env python
#_*_ coding: utf-8 _*_
from app import db

class Assets_Models(db.Model):
    """主机资产"""
    __tablename__ = "assets"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(32), unique=True, nullable=False)
    Localhost = db.Column(db.String(32))
    OS = db.Column(db.String(16))
    OS_Version = db.Column(db.String(8))
    Disk = db.Column(db.String(8))
    Memory = db.Column(db.String(8))
    Desc = db.Column(db.String(128))