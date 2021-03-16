def find_function(s):
    if "(" and ")" in s:
        function_name = ''
        in_params = False
        params = []
        param = ""
        for item in s:
            if item != " ":
                if not in_params:
                    if item != "(":
                        function_name += item
                    else:
                        in_params = True
                else:
                    if item != ")":
                        if item != ",":
                            param += item
                        else:
                            params.append(param)
                            param = ""
        return ["do", function_name, params]
    else:
        return False


def from_python(file):
    """
    coverts to base lang from python
    """
    file = str(file).replace("    ", "\t")
    lines = file.split("\n")
    new_lines = []
    in_class = False
    class_list = []
    for item in lines:
        if (len(item) >= 4) and (item[0] + item[1] + item[2] + item[3] + item[4] == "class"):
            in_class = True
            class_list.append(item)
        elif in_class:
            if (len(item) >= 1) and (item[0] == "\t"):
                class_list.append(item[1:len(item)])
            else:
                new_lines.append(class_list)
                in_class = False
                class_list = []
        else:
            if " = " in item:
                varset = item.split(" = ")
                set_to = varset.pop()
                var_name = varset.pop()
                find_function_in_set = find_function(set_to)
                if not find_function_in_set:
                    new_lines.append(["set", var_name, set_to])
                else:
                    new_lines.append(["set", var_name, find_function_in_set])
            else:
                new_lines.append(item)
    lines = new_lines
    return lines
