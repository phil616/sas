import asyncio

async def say_hi_after(delay, name):
    await asyncio.sleep(delay)
    print(f"Hi, {name}")

async def main():
    print("a")
    await say_hi_after(2, "Bob")
    print("b")
    await say_hi_after(1, "Alice")
    print("c")

asyncio.run(main())
