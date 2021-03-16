
def get_lang(file_extention):
    """
    :param file:
    """
    lang_map = {".c": "c", "c++": "c++", "c#": "c#", ".py": "python", ".java": "java", ".ruby": "ruby", ".r": "r"}
    return lang_map.get(file_extention)
