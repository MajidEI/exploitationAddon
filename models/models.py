# -*- coding: utf-8 -*-

from odoo import models, fields, api


class explo(models.Model):
    _name = 'explo.explo'

    @api.multi
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s' % (rec.code)))
        return res

    # @api.model
    # def default_get(self,fields):
    #     print('im inside the function')
    #     res =  super(explo,self).default_get(fields)
    #     rubriques_rec = self.env['explo.explo'].search([])
    #     children = [ ] 
        
    #     for rub in rubriques_rec:
    #         line = (0,0,{
    #             'codec':rub.code,
    #             'rubriquesc':rub.rubriques,
    #             'montantc':rub.montant,
    #         })
    #         children.append(line)
    #         print(line)

    #     print(children)
    #     res.update({
    #         'children':children,
    #     })
    #     return res
    code = fields.Char()
    rubriques = fields.Char()
    montant = fields.Float()

    children = fields.One2many('explo.children','parent',string='children')
class explochildren(models.Model):
    _name = 'explo.children'

    codec = fields.Many2one('explo.explo',string='Code')
    rubriquesc = fields.Char()
    montantc = fields.Float()

    parent = fields.Many2one('explo.explo',string='Parent')

    