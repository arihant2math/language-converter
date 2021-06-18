def from_python(file):
    """
    coverts to base lang from python
    """
    file = str(file).replace("    ", "\t")
    lines = file.split("\n")
    lines = from_python_r(lines)
    return lines
