def from_python(file):
    """

    """
    file = str(file).replace("    ", "\t")
    lines = file.split("\n")
    new_lines = []
    in_class = False
    class_list = []
    for item in lines:
        if item[0] + item[1] + item[2] + item[3] == "class":
            in_class = True
            class_list.append(item)
        elif in_class:
            if item[0] == "\t":
                class_list.append(item)
            else:
                new_lines.append(class_list)
                class_list = []
        else:
            new_lines.append(item)
