def process_data_and_type(data_string):
    # if not and if it's a string, convert it to lower case
    if isinstance(data_string, str):
        data_string = data_string.lower()
        # remove any padded spaces
        data_string = data_string.strip()
        if data_string == "reorder" or data_string == "yes":
            return True
        elif data_string == "no":
            return False
        # if string starts with $, remove it and convert it ot float
        elif data_string.startswith("$"):
            data_string = data_string[1:]
            data_string = float(data_string)
            return data_string
        elif data_string.isnumeric():
            return int(data_string)
        else:
            return data_string
    else:
        return data_string
