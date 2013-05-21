def to_tag(k, v):
    """Create a new tag for the given key k and value v"""
    return '<{key}>{value}</{key}>'.format(key=k, value=get_content(k, v))

def get_content(k, v):
    """Create the content of a tag by deciding what to do depending on the content of the value"""
    if isinstance(v, str):
        # it's a string, so just return the value
        return v
    elif isinstance(v, dict):
        # it's a dict, so create a new tag for each element
        # and join them with newlines
        print '\n%s\n' % '\n'.join(to_tag(*e) for e in v.items())
        return '\n%s\n' % '\n'.join(to_tag(*e) for e in v.items())
    elif isinstance(v, list):
        # it's a list, so create a new key for each element
        # by using the enumerate method and create new tags
        return '\n%s\n' % '\n'.join(to_tag('{key}-{value}'.format(key=k, value=i+1), e) for i, e in enumerate(v))

def to_xml(d):
    xml = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    xml += "<Images>\n"
    for k, v in d.items():
        xml += to_tag("Image", v) + "\n"
    xml += "</Images>"
    return xml