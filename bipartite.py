# Bipartite Algorithm

def is_bipartite(graph):
    """ Returns True if given graph is bipartite and False if not
    
    For example:

        >>> is_bipartite({
        ... 'A': set(['B', 'C']),
        ... 'B': set(['A', 'D', 'E']),
        ... 'C': set(['A', 'F']),
        ... 'D': set(['B']),
        ... 'E': set(['B', 'F']),
        ... 'F': set(['C', 'E'])
        ... })
        False

        >>> is_bipartite({
        ... 'A': set(['B', 'C']),
        ... 'B': set(['A', 'D', 'E']),
        ... 'C': set(['A']),
        ... 'D': set(['B']),
        ... 'E': set(['B'])
        ... })
        True
    """
    red = set([])
    blue = set([])
    source = graph.keys()[0]
    red.add(source)

    if two_color(graph, source, red, blue) == True:
        return True
    else:
        return False

def two_color(graph, source, red, blue):
    """ Returns True if graph is bipartite and False if not """
    if source in red:
        for i in graph[source]:
            if i in red:
                return False
            elif i in blue:
                continue
            else:
                blue.add(i)
                new_source = i
                two_color(graph, new_source, red, blue)

    elif source in blue:
        for i in graph[source]:
            if i in blue:
                return False
            elif i in red:
                continue
            else:
                red.add(i)
                new_source = i
                two_color(graph, new_source, red, blue)

    return True


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print

