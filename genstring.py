#
# Copyright (C) 2021-2022 by Toni880@Github, < https://github.com/Toni880 >.
#
# This file is part of < https://github.com/Toni880/PrimeMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Toni880/PrimeMusic/blob/master/LICENSE >
#
# All rights reserved.


import asyncio

from pyrogram import Client as c

API_ID = input("\n24707785:\n > ")
API_HASH = input("\n77d4d72c610c167806df6e01fab9561e:\n > ")

print("\n\n +6285931988098\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print("\n1BVtsOJgBu2dn83E4L3B9IcHp0lM3fjFJwcVAzusn8cBLMVXxXDMH1atZqNKkO21nrVIj6500vBnRMe4jAMdz3DCW-RkR2l8C_KLINEc-WDK24dk2AKDWr9L-c5VTNnSi8XUg5NIdQqpXOYnKYaq05dL0UciXV6nttXr6DTzRIBDRD5oSOvJ020T4uRGg3Wpgl1zCpXDD1xLs_W_S7N1ztHHEodQvDoMGcPLZ0Zrq1Wp1mfCV3lLOepSehi7K3G6b0IerjIn87kgvMzg1JlBTmJghVKwKk1oAKcm-mivUr7_jfll1fl6PWissgM1TOBj_azHkoavD9QN7kjVmMXaU3ZIi8rIO7kM=\n")
    print(f"\n{ss}\n")


asyncio.run(main())
