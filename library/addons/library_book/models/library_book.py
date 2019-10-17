from flectra import models, fields
from flectra.addons import decimal_precision as dp

class LibraryBook(models.Model):
    _name = 'library_book.library_book'
    _description = 'records'

    short_name = fields.Char('Short Title')
    name = fields.Char('name')
    father_name=fields.Char('Father Name' )
    agee=fields.Date('age')
    description = fields.Char('desc')
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many(
        'res.partner',
        string='Authors'
    )
    cost_price = fields.Float(
        'Book Cost', dp.get_precision('Book Price'))