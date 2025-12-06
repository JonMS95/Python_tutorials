'''
AsyncIO works by switching between tasks whenever one is waiting, instead
of blocking the whole program. It is not real parallelism and does not use
multiple CPU cores. Instead, it is a single thread that rapidly swaps
between tasks using await.
'''

import asyncio

async def say(name: str, delay: float) -> None:
    await asyncio.sleep(delay)
    print(name)

async def main():
    await asyncio.gather(
        say("A", 1)     ,
        say("B", 2.5)   ,
        say("C", 0.3)
    )

if __name__ =="__main__":
    asyncio.run(main())