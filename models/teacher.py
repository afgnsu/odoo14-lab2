# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teacher(models.Model):
    _name = 'lab2.teacher'
    _description = '老師'

    name = fields.Char('姓名', required=True)
    age = fields.Integer('年紀')
    #一對多(One2many，參數: ['對方資料表','對方欄位名稱','說明'])
    class_student = fields.One2many('lab2.student', 'class_teacher', '班上學生')  #一個導師有很多學生
    note = fields.Text('備註')

