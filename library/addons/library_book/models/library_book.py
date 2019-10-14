from flectra import models, fields

class LibraryBook(models.Model):
    _name = 'library_book.library_book'
    name = fields.Char('Title', required=True)
    date_release = fields.Date('Release Date')
    author_ids = fields.Many2many(
        'res.partner',
        string='Authors'
    )