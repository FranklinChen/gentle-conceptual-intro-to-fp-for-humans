def cons(head, tail):
    return (head, tail)

def append(list1, list2):
    if list1 is None:
        return list2
    else:
        head1, tail1 = list1
        return cons(head1, append(tail1, list2))

first = cons("1", cons("2", None))
second = cons("3", cons("4", None))
third = append(first, second)
