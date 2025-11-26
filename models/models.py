from odoo import models, fields

# ============================================================
# MODELO CUIDADOR
# ============================================================
class Cuidador(models.Model):
    _name = 'refugio_animales.cuidador'
    _description = 'Persona responsable de los animalitos en el refugio'
    _rec_name = 'nombre_cuidador'
    nombre_cuidador = fields.Char(string='Nombre completo', required=True)

    animal_ids = fields.One2many('refugio_animales.animal', 'cuidador_id', string='Animales cuidados')
    #1 cuidador -> varios animales: en la tabla animal se creará un campo con el id del cuidador responsable

    instalacion_id = fields.Many2one('refugio_animales.instalacion', string='Instalación donde trabaja')


# ============================================================
# MODELO ANIMAL
# ============================================================
class Animal(models.Model):
    _name = 'refugio_animales.animal'
    _description = 'Ser vivo indefenso al que se cuida en el refugio'
    _rec_name = 'nombre_animal'

    nombre_animal = fields.Char(string='Nombre del animalito', required=True)
    especie = fields.Char(string='Especie del animalito', required=True)
    edad = fields.Float(string='Edad del animalito', required=True)
    estado = fields.Text(string='Estado frl animalito')

    cuidador_id = fields.Many2one('refugio_animales.cuidador', string='Cuidador responsable')
    instalacion_id = fields.Many2one('refugio_animales.instalacion', string='Ubicacion')

    



# ============================================================
# MODELO INSTALACION
# ============================================================
class Instalacion(models.Model):
    _name = 'refugio_animales.instalacion'
    _description = 'Edificio que contiene a los animales'

    _rec_name = 'nombre_instalacion'
    nombre_instalacion = fields.Char(string='Nombre de la instalación', required=True)
    capacidad = fields.Float(string='Capacidad')
    tipo = fields.Selection([
        ('general', 'General'),
        ('roedores', 'Roedores'),
        ('aves', 'Aves'),
        ('exoticos', 'Exoticos')
    ], string='tipo', default='general')

    animal_ids = fields.One2many('refugio_animales.animal', 'instalacion_id', string='Animales refugiados')
    #1 instalacion -> varios animales: en la tabla animal se creará un campo con el id de la instalacion a la que pertenecen
    cuidador_ids = fields.One2many('refugio_animales.cuidador', 'instalacion_id', string='cuidadores que trabajan en la instalacion')
    #1 instalacion -> varios cuidadores: en la tabla cuidador se creará un campo con el id de la instalacion en la que trabajan

# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class refugio_animales(models.Model):
#     _name = 'refugio_animales.refugio_animales'
#     _description = 'refugio_animales.refugio_animales'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

