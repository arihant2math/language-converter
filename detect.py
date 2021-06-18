"""Finds the language by file extention"""


def get_lang(file_extention):
    """
    :param file:
    """
    lang_map = {".c": "c", "c++": "c++", "c#": "c#", ".py": "python", ".java": "java", ".ruby": "ruby", ".r": "r", ".go", "go"}
    return lang_map[file_extention]
