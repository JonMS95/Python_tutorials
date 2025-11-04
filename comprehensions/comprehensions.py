'''
A comprehension is a compact syntax for creating new lists, sets, or dictionaries from existing iterables.
They’re faster, cleaner, and idiomatic.

Comprehensions are not just syntactic sugar: they’re slightly faster than loops because the iteration
happens in C-level code internally. Use them as much as possible, preferably when initializing data collection
types (lists, sets dicts and tuples).

Take a look at the examples scattered across this module to have a better idea about how to use them properly.
'''

from list_comprehensions    import callListCompFns
from dict_comprehensions    import callDictCompFns
from set_comprehensions     import callSetCompFns
from generator_expressions  import callGenExpFns

def main():
    callListCompFns()
    callDictCompFns()
    callSetCompFns()
    callGenExpFns()

if __name__ == "__main__":
    main()
