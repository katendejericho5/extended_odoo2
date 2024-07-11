from odoo import models, fields, api
from odoo.exceptions import UserError

class NationalIDApplication(models.Model):
    _name = 'national.id.application'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Inherit for chatter functionality
    _description = 'National ID Application'

    name = fields.Char(string="Name", required=True)
    birth_date = fields.Date(string="Birth Date", required=True)
    address = fields.Text(string="Address", required=True)
    photo = fields.Binary(string="Photo")
    lc_reference_letter = fields.Binary(string="LC Reference Letter")
    stage = fields.Selection([
        ('draft', 'Draft'),
        ('stage1', 'Stage 1'),
        ('stage2', 'Stage 2'),
        ('done', 'Done'),
    ], default='draft', tracking=True)  # Enable tracking for chatter
    approver_ids = fields.Many2many('res.users', string="Approvers")

    def action_approve_stage1(self):
        if self.stage != 'draft':
            raise UserError("Can only approve from draft stage")
        self.stage = 'stage1'
        self.message_post(body="Approved Stage 1 by %s" % self.env.user.name)  # Log in chatter

    def action_approve_stage2(self):
        if self.stage != 'stage1':
            raise UserError("Can only approve from stage 1")
        self.stage = 'stage2'
        self.message_post(body="Approved Stage 2 by %s" % self.env.user.name)  # Log in chatter

    def action_done(self):
        if self.stage != 'stage2':
            raise UserError("Can only mark as done from stage 2")
        self.stage = 'done'
        self.message_post(body="Marked as Done by %s" % self.env.user.name)  # Log in chatter
