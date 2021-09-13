from html.parser import HTMLParser


class Tag(object):
    html = ''  # тег
    attrs = ''  # атрибуты
    decr = ''  # описание
    tag = ''

    def get_html(self):
        return self.html

    def get_attrs(self):
        return self.attrs

    def get_decr(self):
        return self.decr

    def get_tag(self):
        return Tag.get_html(self) + ' ' + Tag.get_attrs(self) + ' ' + Tag.get_decr(self)


class Input(Tag):
    html = '<input>'
    attrs = ' alt, checked -  атрибуты тега. '
    decr = 'Позволяет создавать разные части интерфейса и обеспечивать взаимодействие с пользователем. Закрывающий тег не требуется'


class Image(Tag):
    html = '<img>'
    attrs = ' src, alt - атрибуты тега. '
    decr = 'Предназначен для отображения на веб-странице изображений в графическом формате.Закрывающий тег не требуется'


class P(Tag):
    html = '<p></p>'
    attrs = 'align - атрибуты тега. '
    decr = 'Определяет текстовый абзац.Закрывающий тег не требуется'


class A(Tag):
    html = '<a></a>'
    attrs = ' href - атрибуты тега. '
    decr = 'Предназначен для создания ссылок'


class Form(Tag):
    html = '<form></form>'
    attrs = ' action - атрибуты тега. '
    decr = 'Устанавливает форму на веб-странице'


class TagFactory():
    def create_tag(self, type):
        targetclass = type.capitalize()
        return globals()[targetclass]()


factory = TagFactory()
tags = ['image', 'input', 'p', 'a', 'form']

# for i in tags:
#     print(f'Тег <{i}> пишется: ', factory.create_tag(i).get_html(), factory.create_tag(i).get_decr(),
#           ' имеет атрибуты:', factory.create_tag(i).get_attrs())
# print('-----------------------------------------------------------------------------------------------------')

# for i in tags:
#     print('Тег <{}> пишется: '.format(i), factory.create_tag(i).get_tag())
tag_objects = []
for i in tags:
    tag_objects.append(factory.create_tag(i))

for i in tag_objects:
    print('Тег <{}> пишется: '.format(
        str(type(i).__name__).lower()), i.get_tag())
