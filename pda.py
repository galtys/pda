#API entry points for Android PDA application

def searh_picking(name):
    """
    @name is the barcode string (for example OUT04432) uniquely identifying a picking.
    
    return:
    picking_id  id value in sql database (integer)
    """

def read_picking(name):
    picking_id=search_picking(name)
    return read_picking(picking_id)

def read_picking(picking_id):
    """
    @picking_id   input
    """
    #return example:
    {
        'header':{'id':222,'customer_name':'Sue Roberts', 'carrier':'KINGS', 'carrier_ref':'4a34564','order':'SO4422'},
        #we may need to extend header info later
        'stock_moves':[ {'sku': 'AFI3',
                         'name': 'chair ....................',
                         'qty_to_deliver': 3,
                         'qty_loaded':2,
                         'qty_to_follow':1,
                         'pallet_no':1},
                        {'sku': 'UDS43',
                         'name': 'table ....................',
                         'qty_to_deliver': 1,
                         'qty_loaded':1,
                         'qty_to_follow':0,
                         'pallet_no':1},
                        {'sku': 'KACB',
                         'name': 'sofa ....................',
                         'qty_to_deliver': 2,
                         'qty_loaded':1,
                         'qty_to_follow':1,
                         'pallet_no':2} ],
        'pallets':[{'pallet_no':1,
                    'dimensions': (100,120,30)},
                   'photo': '', #base64 encode png or jpeg
                   {'pallet_no':2,
                    'dimensions': (80, 20,70),
                    'photo': '', #base64 encoded png or jpeg
                } ],
    }

def upload_picking(picking_id, data):
    pass
    #data has the same structure as in example above (for read_picking)

def save_picking(picking_id):
    pass
    #Save picking will save progress only. It will not affect stock levels

def confirm_picking(picking_id):
    pass
    #Confirm picking will save and confirm picking. It will validate picking in odoo (and move stock)

