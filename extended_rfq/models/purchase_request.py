from odoo import models, fields, api

class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase Request'

    # Char field for the request reference number
    name = fields.Char(string='Request Reference', required=True, copy=False, readonly=True, default='New',
                       help="Unique identifier for this purchase request")
    
    # Many2one field to link to the employee making the request
    requesting_employee = fields.Many2one('hr.employee', string='Requesting Employee', required=True,
                                          help="The employee who is making this purchase request")
    
    # Many2one field to store the department of the requesting employee
    department_id = fields.Many2one('hr.department', string='Department',
                                    help="The department of the requesting employee")
    
    # Date field for when the request was made
    date_request = fields.Date(string='Request Date', default=fields.Date.today,
                               help="The date when this purchase request was made")
    
    # Many2one field to link to the product being requested
    product_id = fields.Many2one('product.product', string='Product', required=True,
                                 help="The product being requested")
    
    # Float field for the quantity of the product being requested
    quantity = fields.Float(string='Quantity', required=True,
                            help="The quantity of the product being requested")
    
    # Text field for any additional description or notes about the request
    description = fields.Text(string='Description',
                              help="Additional details or notes about this purchase request")
    
    # Selection field to track the state of the purchase request
    state = fields.Selection([
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved'),
        ('rfq_created', 'RFQ Created'),
        ('done', 'Done'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft',
       help="Current status of the purchase request")

    @api.model
    def create(self, vals):
        # Override create method to generate a unique sequence for the name field
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.request') or 'New'
        return super(PurchaseRequest, self).create(vals)

    def action_create_rfq(self):
        # TODO: Implement logic to create RFQ from purchase request
        # This method should:
        # 1. Create a new purchase.order (RFQ) record
        # 2. Populate the RFQ with data from this purchase request
        # 3. Update the state of this purchase request to 'rfq_created'
        pass