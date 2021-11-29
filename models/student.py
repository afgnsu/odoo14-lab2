# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Student(models.Model):
    _name = 'lab2.student'
    _description = '學生'

    name = fields.Char('姓名', required=True)
    age = fields.Integer('年紀')
    sex = fields.Selection([('M', '男'), ('F', '女')], '性別', default='M')
    #多對一(Many2one，參數: ['對方資料表','說明','刪除是否關聯'])
    class_teacher = fields.Many2one('lab2.teacher', '班導', ondelete='cascade') #學生只有一個導師
    note = fields.Text('備註')

