from odoo import models, fields, api


class Students(models.Model):
    _name = "school.student.detail"
    _description = "student detail"
    _order = "email_id DESC"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    # _inherit = ["todos.detail"]

    name = fields.Char(string='Name', required=True)
    email_id = fields.Char(string='Email', default='manthan@gmail.com')
    todo_name = fields.Many2one(
        'todos.detail', string="Todo", ondelete="cascade")
    is_completed = fields.Boolean(
        related='todo_name.is_done', string="Is Completed")
    address_line1 = fields.Char(string='Address Line1')
    address_line2 = fields.Char(string='Address Line2')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ], 'Gender', default='male')
    fees = fields.Float(string='Fees', digits=(12, 6))
    # course_li_ids = fields.One2many(
    #     'courses.detail', 'st_id', string='Course Lines')
    skill_per = fields.Integer(string="Skill Per.")
    max_skill_per = fields.Integer(default=70)
    course_tags = fields.Many2many(
        'courses.detail', 'student_course_rel', 'student_id', 'course_id', string='Courses')
    course_payment_status = fields.Selection(
        [('ordered', 'Ordered'), ('pending', 'Pending'), ('delivered', 'Delivered')])
    course_cnt = fields.Integer('Courses', compute='get_course_doc_cnt')
    course_ids = fields.One2many(
        'course.data.lines', 'st_id', string='Course Lines')

    def get_course_doc_cnt(self):
        print(f"\n\n\n courses search count : {self.env['course.data.lines'].search_count([('st_id', '=', self.id)])} \n\n\n")
        self.course_cnt = self.env['course.data.lines'].search_count(
            [('st_id', '=', self.id)])

    _sql_constraints = [

        ('skill_per_check', 'CHECK((skill_per >= 65 ))',
         'Skill Per. must be >= 65.'),
        ('max_skill_per_check', 'CHECK((max_skill_per >= 55 ))',
         'Max Skill Per. must be >= 55.'),
    ]

    @api.model
    def create(self, vals):
        # set default val if email_id ""
        if not vals["email_id"]:
            print("\n\n\n email id is '' \n\n\n")
            default_email_id = super(Students, self).default_get(['email_id'])
            vals.update({'email_id': default_email_id['email_id']})
        return super(Students, self).create(vals)

    # #(4,ID) - for one2many,many2many
    # @api.model
    # def create(self, vals):
    #     print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     print(f"\n\n\n\n xml record id {self.env.ref('new_app.course_data_3').id} \n\n\n")
    #     vals.update({'course_li_ids': [(4, self.env.ref('new_app.course_data_3').id)],
    #                  'course_tags': [(4, self.env.ref('new_app.course_data_2').id)]})
    #     # student_obj = super(Students, self).create({
    #     #     # 'name': vals['name'],
    #     #     # 'email_id': vals['email_id'],
    #     #     'address_line1': vals['address_line1'],
    #     #     'course_li_ids': [(4, self.env.ref('new_app.course_data_3').id)],
    #     #     'course_tags': [(4, self.env.ref('new_app.course_data_2').id)]

    #     # })
    #     # print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     res = super(Students, self).create(vals)
    #     return res
    #     # return student_obj

    # #(4,ID) - for one2many
    # def write(self, vals):
    #     vals['name'] = 'GKT'
    #     # professor_obj = super(Professors, self).search([])
    #     print(f"\n\n\n before : {vals['email_id']} \n\n\n")
    #     vals["email_id"] = (super(Students, self).default_get(["email_id"]))[
    #         "email_id"]
    #     print(f"\n\n\n before : {vals['email_id']} \n\n\n")
    #     student_obj = super(Students, self).write({
    #         'name': vals['name'],
    #         'email_id': vals['email_id'],
    #         'course_li_ids': [(4, self.env.ref('new_app.course_data_3').id)]
    #     })
    #     print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     return student_obj

    # (6,0,ID) - for many2many
    # def write(self, vals):
    #     vals['name'] = 'AKA'
    #     # professor_obj = super(Professors, self).search([])
    #     student_obj = super(Students, self).write({
    #         'name': vals['name'],
    #         'course_tags': [(6, 0, [self.env.ref('new_app.course_data_1').id, self.env.ref('new_app.course_data_2').id])]
    #     })
    #     print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     return student_obj

    #  #(5,0,0) - for one2many
    # def write(self, vals):
    #     vals['name'] = 'JKT'
    #     # professor_obj = super(Professors, self).search([])
    #     student_obj = super(Students, self).write({
    #         'name': vals['name'],
    #         'course_li_ids': [(5, 0, 0)]
    #     })
    #     print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     return student_obj

    # #(5,0,0) - for many2many
    # def write(self, vals):
    #     vals['name'] = 'SKT'
    #     # professor_obj = super(Professors, self).search([])
    #     student_obj = super(Students, self).write({
    #         'name': vals['name'],
    #         'course_tags': [(5, 0, 0)]
    #     })
    #     print(f"\n\n\n student input dt : {vals}\n\n\n")
    #     return student_obj

    # @api.onchange('email_id')
    # def change_email(self):
    #     for rec in self:
    #         record = super(Students, self).default_get(['email_id'])
    #         rec.email_id = record['email_id']

    def action_ordered(self):
        for rec in self:
            if rec.course_li_ids.id:
                print("staus changed to 'ordered'.")
                rec.write({'course_payment_status': 'ordered'})

    def action_pending(self):
        for rec in self:
            if rec.course_li_ids.id:
                print("staus changed to 'pending'.")
                if rec.course_payment_status == 'ordered':
                    rec.write({'course_payment_status': 'pending'})

    def action_delivered(self):
        for rec in self:
            if rec.course_li_ids.id:
                print("staus changed to 'delivered'.")
                if rec.course_payment_status == 'pending':
                    rec.write({'course_payment_status': 'delivered'})

    def action_course(self):
        # self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Courses',
            'view_mode': 'tree,form',
            'res_model': 'course.data.lines',
            'domain': [('st_id', '=', self.id)],
        }

    # def open_wizard(self):

    #     return {
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'school.student.fees.wizard',
    #         'target': 'new'
    #     }


class CourseStudentline(models.Model):  # task.lines
    _name = 'course.data.lines'

    course_id = fields.Many2one('courses.detail', ondelete="set default")
    st_id = fields.Many2one('school.student.detail')
    short_desc = fields.Char(string="Short Desc.",
                             related='course_id.short_desc')
    created_by = fields.Char(
        string="Created By", related='course_id.created_by')

    def name_get(self):
        label = []
        for rec in self:
            title = f"{rec.course_id.name} ({rec.st_id.name})"
            label.append((rec.id, title))
        return label
