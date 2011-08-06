def insert_helper(index, item):
    d = {'type' : 'insert', 'index' : index, 'item' : item}
    return d

def delete_helper(index):
    d = {'type' : 'delete', 'index' : index}
    return d

def insert_insert(a, b):
    if a == b:
        return None 

    if a['index'] < b['index']:
        return a
    else:
        return insert_helper(a['index'] + 1, a['item'])

def delete_insert(a, b):
    if a['index'] < b['index']:
        return a
    else:
        return delete_helper(a['index'] + 1) 

def insert_delete(a, b):
    if a['index'] < b['index']:
        return a
    else:
        return insert_helper(a['index'] - 1, a['item'])

def delete_delete(a, b):
    if a == b:
        return None 

    if a['index'] > b['index']:
        return delete_helper(a['index'] - 1)
    else:
        return a

def transform(a, b):
    # insert insert
    if (a['type'] == 'insert') and (b['type'] == 'insert'):
        return insert_insert(a, b)

    # delete insert
    if (a['type'] == 'delete') and (b['type'] == 'insert'):
        return delete_insert(a, b)

    # insert delete
    if (a['type'] == 'insert') and (b['type'] == 'delete'):
        return insert_delete(a, b)

    # delete delete
    if (a['type'] == 'delete') and (b['type'] == 'delete'):
        return delete_delete(a, b)

def transform_many(a, l, i = 0):
    if len(l) == 0:
        return a

    if i == len(l) - 1:
        a = transform(a, l[i])
        if not a:
            return None
        else:
            return a
    else:
        current = l[i]
        a = transform(a, current)
        if not a:
            return None
        return transform_many(a, l, i + 1)

def transform_many_to_many(a, b):
    if b:
        transformed = [] 
        for i, op in enumerate(a):
            op = transform_many(op, b[i:])
            if op:
                transformed.append(op)
    else:
        transformed = a

    return transformed

def render(operations, state = None):
    state = state or []
    for op in operations:
        if op['type'] == 'insert':
            state.insert(op['index'], op['item'])
        else:
            state.pop(op['index'])
    return state
