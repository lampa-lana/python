from enum import Enum


class TagType(Enum):
    INPUT = 0,
    IMAGE = 1,
    TEXT = 2,
    LINK = 3


class Tag:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Input(Tag):
    def __init__(self):
        super().__init__('<input>'r'<\input>')


class Image(Tag):
    def __init__(self):
        super().__init__('<img>'r'<\img>')


class Text(Tag):
    def __init__(self):
        super().__init__('<p>'r'<\p>')


class Link(Tag):
    def __init__(self):
        super().__init__('<a>'r'<\a>')


def create_tag(tag_type: TagType):
    factory_dict = {
        TagType.INPUT: Input,
        TagType.IMAGE: Image,
        TagType.TEXT: Text,
        TagType.LINK: Link
    }
    return factory_dict[tag_type]()


for i in TagType:
    my_tag = create_tag(i)
    print(f'Tag : {i}, пишется как: {my_tag.get_name()}')
