from flectra import models, fields

class LibraryBook(models.Model):
    _name = 'library_book.library_book'
    name = fields.Char('name', required=True)
    father_name=fields.Char('Father Name' )
    agee=fields.Date('age')
    description = fields.Char('desc')
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many(
        'res.partner',
        string='Authors'
    )