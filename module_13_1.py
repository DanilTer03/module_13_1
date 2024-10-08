import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(5):
        await asyncio.sleep(1 / power)
        print(f'{name} поднял {i + 1} шар')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
        challenger_1 = asyncio.create_task(start_strongman('Pasha', 3))
        challenger_2 = asyncio.create_task(start_strongman('Denis', 4))
        challenger_3 = asyncio.create_task(start_strongman('Apollon', 5))
        await challenger_1
        await challenger_2
        await challenger_3



asyncio.run(start_tournament())
