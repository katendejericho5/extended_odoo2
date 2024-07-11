from odoo import models, fields, api, exceptions

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.Many2many('res.partner', string='Vendors', domain=[('supplier_rank', '>', 0)],
                                  help="Select multiple vendors for this RFQ")
    
    bid_ids = fields.One2many('purchase.bid', 'rfq_id', string='Bids',
                              help="Bids received from vendors for this RFQ")
    
    winning_bid_id = fields.Many2one('purchase.bid', string='Winning Bid',
                                     help="The selected winning bid for this RFQ")

    def action_select_winning_bid(self):
        for order in self:
            if not order.bid_ids:
                raise exceptions.UserError("No bids to select from.")
            
            # Select the best bid based on the lowest price
            winning_bid = min(order.bid_ids, key=lambda bid: bid.amount)
            
            # Set the winning bid
            order.winning_bid_id = winning_bid
            
            # Create a Purchase Order based on the winning bid
            po_vals = {
                'partner_id': winning_bid.vendor_id.id,
                'order_line': [(0, 0, {
                    'product_id': product_id,
                    'name': product_name,
                    'product_qty': product_qty,
                    'product_uom': product_uom,
                    'price_unit': winning_bid.amount,
                    'date_planned': date_planned,
                }) for product_id, product_name, product_qty, product_uom, date_planned in order.order_line.mapped(lambda line: (line.product_id.id, line.name, line.product_qty, line.product_uom.id, line.date_planned))],
            }
            new_po = self.env['purchase.order'].create(po_vals)
            # Additional logic to confirm the PO if needed
            # new_po.button_confirm()
        return True

class PurchaseBid(models.Model):
    _name = 'purchase.bid'
    _description = 'Purchase Bid'

    rfq_id = fields.Many2one('purchase.order', string='RFQ', required=True,
                             help="The RFQ this bid is associated with")
    
    vendor_id = fields.Many2one('res.partner', string='Vendor', required=True,
                                help="The vendor who submitted this bid")
    
    amount = fields.Float(string='Bid Amount', required=True,
                          help="The total amount of this bid")
    
    notes = fields.Text(string='Notes',
                        help="Any additional notes or comments about this bid")
