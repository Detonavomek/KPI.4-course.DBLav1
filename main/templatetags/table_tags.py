from django import template

from main import models

register = template.Library()


# def get_foreign_key_name(k, v):
#     k = k.replace('_id', '').title()
#     table = getattr(models, k)
#     print table.__name__
#     trows = table.get_all()
#     for trow in trows:
#         if trow.id == v:
#             return '<td>%s</td>' % getattr(trow, 'to_string')()
#     return '<td></td>'


@register.simple_tag
def table_row(row):
    result = '<td>%s</td>' % row.id
    for k, v in row.params.items():
        result += '<td>%s</td>' % v
        # if '_id' in k:
        # result += get_foreign_key_name(k, v)
        # else:
        # result += '<td>%s</td>' % v
    return result
