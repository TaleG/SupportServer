#!/usr/bin/env python
#_*_ coding: utf-8 _*_
from app import db

class Domains_Models(db.Model):
    """域名管理"""
    __tablename__ = "Domains"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(32), unique=True, nullable=False)
    Desc = db.Column(db.String(128))