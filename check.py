def check(info_sent, info_required):
    for info in info_required:
        if (info_sent.get(info) == None):
            return f"This {info} is required!"
        else:
            return None