from html.parser import HTMLParser


class Tag(object):
    html = ''  # тег
    attrs = ''  # атрибуты
    decr = ''  # описание

    def get_html(self):
        return self.html

    def get_attrs(self):
        return self.attrs

    def get_decr(self):
        return self.decr


class Input(Tag):
    html = '<input>'
    attrs = 'alt, checked'
    decr = 'Позволяет создавать разные части интерфейса и обеспечивать взаимодействие с пользователем. Закрывающий тег не требуется'


class Image(Tag):
    html = '<img>'
    attrs = 'src, alt'
    decr = 'Предназначен для отображения на веб-странице изображений в графическом формате.Закрывающий тег не требуется'


class P(Tag):
    html = '<p></p>'
    attrs = 'align - атрибут устарел'
    decr = 'Определяет текстовый абзац.Закрывающий тег не требуется'


class A(Tag):
    html = '<a></a>'
    attrs = 'href'
    decr = 'Предназначен для создания ссылок'


class Form(Tag):
    html = '<form></form>'
    attrs = 'action'
    decr = 'Устанавливает форму на веб-странице'


class TagFactory():
    def create_tag(self, type):
        targetclass = type.capitalize()
        return globals()[targetclass]()


factory = TagFactory()
tags = ['image', 'input', 'p', 'a', 'form']
for i in tags:
    print(f'Тег {i} пишется: ', factory.create_tag(i).get_html(), factory.create_tag(i).get_decr(),
          ' имеет атрибуты:', factory.create_tag(i).get_attrs())
