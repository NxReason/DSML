from data_store import read_translations

id_expr = {}
expr_id = {}
id_read = {}
id_defs = {}
id_exmp = {}


def gen_dict():
    exp, read, defs, exmp = read_translations()
    for id, e in exp:
        id_expr[id] = e
        expr_id[e] = id

    for _, r, id in read:
        if id not in id_read:
            id_read[id] = []
        id_read[id].append(r)

    for _, d, id in defs:
        if id not in id_defs:
            id_defs[id] = []
        id_defs[id].append(d)

    for _, e, id in exmp:
        if id not in id_exmp:
            id_exmp[id] = []
        id_exmp[id].append(e)


def lookup(word):
    if len(id_expr) == 0:
        gen_dict()

    id = expr_id.get(word)
    readings = id_read.get(id)
    definitions = id_defs.get(id)
    examples = id_exmp.get(id)

    return {'id': id, 'word': word, 'readings': readings, 'definitions': definitions, 'examples': examples}
