# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class Lab2(models.Model):
#     _name = 'lab2.lab2'
#     _description = 'lab2.lab2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100