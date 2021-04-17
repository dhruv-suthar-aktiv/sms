from odoo import api, fields, models
from random import randint


class Courses(models.Model):  # task
    _name = "courses.detail"
    _description = "course detail"
    _rec_name = "name"
    _order = "name"
    # _inherit = 'school.student.detail'

    def _get_default_color(self):
        return randint(1, 11)

    name = fields.Char(string="Course Name")
    thumbnail = fields.Image(string="Course Thumbnail",
                             max_width=150, max_height=75)
    short_desc = fields.Char(string="Short Desc.")
    created_by = fields.Char(string="Created By")
    rate = fields.Float(string="Rate")
    requirements = fields.Text(string="Requirements")
    long_desc = fields.Text(string="Long Desc.")
    is_discounted = fields.Boolean(string="Is Discounted")
    # student_id = fields.Many2one('school.student.detail', string='Student')
    # st_id = fields.Many2one(
    # comodel_name='school.student.detail', string='Student', ondelete="set
    # default")
    color = fields.Integer(default=_get_default_color)
    # courses_many = fields.Many2one(
    # comodel_name='courses.detail', string='Course')


# class ABC(models.Model):
#     _name = "abc.abc"
#     course_id = fields.Many2one('courses.detail', string='Course')
#     student_id = fields.Many2one('school.student.detail', string='Student')
