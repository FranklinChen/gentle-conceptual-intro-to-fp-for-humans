mutableArray = ["my", "world"]
mutableArrayAlias = mutableArray # alias mutableArray

mutableArray.insert(0, "hello")

def cons(head, tail):
    return (head, tail)

immutableList = cons("my", cons("world", None))
immutableListAlias = immutableList

newImmutableList = cons("hello", immutableList)
