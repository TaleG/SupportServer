#!/usr/bin/env python
#_*_ coding: utf-8 _*
from app import db

class Ip_Models(db.Model):
    """IP列表"""
    __tablename__ = "ip"

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(32), unique=True, nullable=False)
    Netmask= db.Column(db.String(32))
    gateway = db.Column(db.String(32))
    Desc = db.Column(db.String(128))