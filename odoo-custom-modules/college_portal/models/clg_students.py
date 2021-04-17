import datetime
import math
import random
import string

from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Clg_Student(models.Model):
    _name = 'clg.student.detail'
    _description = 'college student detail'

    user_name = fields.Char(string='User Name')
    name = fields.Char(string='Student Name',
                       default="your name")
    mobile_no = fields.Char(string='Student Mo No.')
    email_id = fields.Char(string='Student email id.')
    address = fields.Text(string='Student Address')
    dob = fields.Date(string='Student Date of Birth')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ], 'Gender', default='male')
    id_no = fields.Integer(compute='compute_id_no', store=True)
    todos = fields.Many2one(
        'todos.detail', string="Todo")
    age = fields.Integer()
    courses = fields.Many2one('courses.detail', string="Course")
    spend_amt = fields.Float(string='Amount to spend', compute='compute_amt')
    res = fields.Char()

    # def name_get(self):
    #     name = []
    #     for rec in self:
    #         name = f"{rec.name} ({rec.user_name})"
    #     return name

    # @api.onchange('dob')
    # def calc_age(self):
    #     for rec in self:
    #         if rec.dob:
    #             your_date = rec.dob
    #             today_date = datetime.date.today()
    #             rec.age = abs(((today_date - your_date) // 365).days)

    # @api.model
    # def create(self, vals):
    #     print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     # clg_student = super(Clg_Student, self).create(vals)
    #     task_dt = self.env['todos.detail'].create(
    #         {'title': 'new to dfdod'})
    #     # # vals['todos'] = task_dt[0]
    #     # # clg_student.write(vals)
    #     print(f"\n\n\n\n {task_dt.id} \n\n\n")
    #     vals['name'] = 'xyzw'
    #     vals['todos'] = task_dt.id
    #     return super(Clg_Student, self).create(vals)

    # @api.model
    # def create(self, vals):
    #     print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     clg_student = super(Clg_Student, self).create(vals)
    #     # task_dt = self.env['todos.detail'].create(
    #     #     {'title': 'make a programming language'})
    #     # vals['todos'] = task_dt[0]
    #     # clg_student.write(vals)
    #     return clg_student

    @api.model
    def create(self, vals):
        print(f"student vals {vals}")
        clg_student = super(Clg_Student, self).create(vals)
        course_dt = self.env['courses.detail'].create(
            {'name': 'DsManthan course '})

        vals['courses'] = course_dt[0]
        clg_student.write(vals)
        print(course_dt)
        return clg_student

    def write(self, vals):
        vals['mobile_no'] = 8945631274
        clg_up_student = super(Clg_Student, self).write(vals)
        print(f"n\n\n{type(clg_up_student)}\n\n\n")
        return clg_up_student

    # def write(self, vals):
    #     vals['email_id'] = 'aktiv@gmail.com'
    #     clg_up_student = super(Clg_Student, self).write(vals)
    #     print(f"n\n\n{type(clg_up_student)}\n\n\n")
    #     return clg_up_student

    # def unlink(self):
    #     print("\n\n\nlink done sucessfully\n\n\n")
    #     print(f"\n\n\n {super(Clg_Student, self).unlink()} \n\n\n")
    #     return super(Clg_Student, self).unlink()

    def search_read_func(self):
        # read
        read_res = self.env['clg.student.detail'].search(
            [('name', '=', "fdefd")]).read(['name'])
        print(f"\n\n\nread() res : {read_res}\n\n\n")
        self.res = "read res : " + str(read_res)
        # read
        search_read_res = self.env['clg.student.detail'].search_read(
            [('gender', '=', "male")], ['name'])
        self.res += "<br>" + "search_read res : " + str(search_read_res)
        print(f"\n\n\nsearch_read() res : {search_read_res}\n\n\n")

    def search_func(self):
        # search
        search_res = self.env['clg.student.detail'].search(
            [('gender', '=', 'female')])
        print(f"\n\n\n search() res : {search_res} \n\n\n")
        # search_count
        search_cnt = self.env['clg.student.detail'].search_count(
            [('gender', '=', 'male')])
        print(f"\n\n\nsearch_count() res : {search_cnt}\n\n\n")
        # #browse
        browse_res = self.env['clg.student.detail'].browse([5])
        print(f"\n\n\nbrowse() res : {browse_res}\n\n\n")

# @api.model
# def create(self, vals):
#     print(f"values that we get  before: {vals}")
#     vals['mobile_no'] = str(8945128910)
#     print(f"values that we get  after: {vals}")
#     clg_student = super(Clg_Student, self).create(vals)
#     print(f"return vals : {clg_student}")
#     print(type(clg_student))
#     return clg_student
# else:
# raise ValidationError("user name is required.")

    @api.depends('courses')
    def compute_amt(self):
        discount_per = 15
        for rec in self:
            if rec.courses.rate > 500:
                # print(f"\n\n\n{rec.courses.rate * (discount_per //
                # 100)}\n\n\n")
                rec.spend_amt = rec.courses.rate - \
                    (rec.courses.rate * (discount_per / 100))
            else:
                discount_per = 5
                rec.spend_amt = rec.courses.rate - \
                    (rec.courses.rate * (discount_per / 100))

    @api.depends('todos')
    def compute_id_no(self):
        for rec in self:
            rec.id_no = 0
            if rec.todos.is_done == True:
                rec.id_no = 5
            else:
                rec.id_no = 15

    # @api.depends('name')
    # def compute_id_no(self):
    #     for rec in self:
    #         self.id_no = 0
    #         if rec.name == 'manthan':
    #             rec.id_no = 5
    #         else:
    #             rec.id_no = 15
    # @api.model
    # def name_create(self, name):
    #     for i in self:
    #         rec = i.name + i.user_name
    #     return rec

    # def generate_user_name(self):

    #     self.user_name = ''.join(random.choice(
    # string.ascii_uppercase + string.ascii_lowercase + string.digits) for _
    # in range(random.randint(9, 15)))

        # for rec in self:
        #     rec.write({'user_name': ''.join(random.choice(
        # string.ascii_uppercase + string.ascii_lowercase + string.digits) for
        # _ in range(random.randint(9, 15)))})

        # @api.constrains("mobile_no")
        # def check_mobile_no(self):
        #     if str(self.mobile_no).strip() != 'False':
        #         print("\n\n\n True \n\n\n")
        #         if not str(self.mobile_no).isdigit():
        #             raise ValidationError("Please enter valid mobile no.")
        #         else:
        #             if len(str(self.mobile_no).strip()) != 10:
        #                 raise ValidationError("mobile no. size must be 10.")
        # def write(self, vals):
        #     vals['email_id'] = 'sdrgfahrueiw@dsfabhj.com'
        #     return super(Clg_Student, self).write(vals)
