#API entry points for Android PDA application
#
#
#

class stock_picking(osv.osv):
    _inherit = 'stock.picking'
    _columns = {'pda_finished':fields.boolean('PDA Finished',help='PDA confirms that all data to picking, stock moves and pallets has been written'),
                '
    def searh_picking(name):
        """
        @name is the barcode string (for example OUT04432) uniquely identifying a picking. Note that prefix OUT can be ommited.

        return:
        picking_id  id value in sql database (integer)
        """


def read_moves(picking_id):
    #return example
    ret = [ {'sku': 'AFI3',
             'name': 'chair ....................',
             'qty_to_deliver': 3,
             'qty_loaded':2,
             'pallet': '00000017'},
            {'sku': 'UDS43',
             'name': 'table ....................',
             'qty_to_deliver': 1,
             'qty_loaded':1,
             'pallet': '00000018'},
            {'sku': 'KACB',
             'name': 'sofa ....................',
             'qty_to_deliver': 2,
             'qty_loaded':1,
             'pallet': ''} ],
    return ret

def search_palletes(picking_id):
    ret = [4343, 1243]
    return ret

#class pallete (stock.packaging) has to be extended as follows:
class stock_packaging(osv.osv):
    _inherit = 'stock.packaging'
    _columns = {'number':fields.integer('Number'),
                'w':fields.integer('W'),
                'h':fields.integer('H'),
                'd':fields.integer('D'),
                'photo':fields.binary('Photo'),

                }

