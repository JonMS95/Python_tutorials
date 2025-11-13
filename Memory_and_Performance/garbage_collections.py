'''
Reference counting alone fails with circular references (when two ormore objects
point at each other cyclically).

That's why Python also has a garbage collector which does also solve this kind
of issues.
'''

import gc

def main():
    print("Is GC enabled? ", gc.isenabled())

    # Garbage collection can be forced manually.
    gc.collect()

    # Garbage colletor can be explicitly disabled (although it's strongly discouraged).
    # gc.disable()

if __name__ == "__main__":
    main()