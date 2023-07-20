import asyncio

"""async def count(API): #coroutine function                               
    print(f"Call API {API}")                                           
    await asyncio.sleep(API)
    print(f"API {API} Call Completed ")

async def main():
    await asyncio.gather(count(1), count(6), count(3))

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")"""

import aiohttp

async def call(url,t):
    async with aiohttp.ClientSession() as session:
        print(f"Calling Status for {t}")
        async with session.request("Get", url) as resp:
            await asyncio.sleep(t)
            c = await resp.read()
            if c != "":
                print(f"Status {t} is success")
                #return c
async def main():
    await asyncio.gather(call("https://www.python.org/dev/peps/pep-8010/",1),
                            call("https://www.python.org/dev/peps/pep-8011/",5),
                            call("https://www.python.org/dev/peps/pep-8012/",2))

asyncio.run(main())