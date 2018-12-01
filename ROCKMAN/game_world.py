
# layer 0: Background Objects
# layer 1: Foreground Objects
# layer 2: bullets
# layer 3: player, ui
objects = [[],[],[],[]]


def add_object(o, layer):
    objects[layer].append(o)

def add_objects(l, layer):
    for o in l:
        add_object(o, layer)

def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break


def clear():
    for l in objects:
        l.clear()
    objects.clear()


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

