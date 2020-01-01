from i3ipc import Connection, Event
from operator import itemgetter, attrgetter
i3 = Connection()

def swap(a, b):
    i3.command("[con_id=%s] swap container with con_id %s" % (a, b))

tree = i3.get_tree()
leaves = list(tree.find_focused().workspace().leaves())
sorted_leaves = sorted(leaves, key=attrgetter('rect.x', 'rect.y'))
windows = list(str(leaf.id) for leaf in sorted_leaves)

for i in range(len(windows) - 1):
    a = windows[0]
    b = windows[i + 1]
    swap(a, b)
