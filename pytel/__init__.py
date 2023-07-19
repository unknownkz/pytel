"""
# pytel < https://t.me/kastaid >
# Copyright (C) 2023-present kastaid

# This file is a part of < https://github.com/kastaid/pytel/ >
# Please read the GNU Affero General Public License in
# < https://github.com/kastaid/pytel/blob/main/LICENSE/ >.
"""
from asyncio import (
    get_event_loop,
    set_event_loop_policy,)
from uvloop import EventLoopPolicy
from .logger import pylog as send_log

set_event_loop_policy(EventLoopPolicy())

loopers = get_event_loop()

try:
    from pathlib import Path
    from shutil import rmtree
    from sys import exit
    from time import time
    from .client import PytelClient
    from .config import (
        API_HASH, API_ID, SESSION1,
        SESSION2, SESSION3, SESSION4,
        SESSION5, TGB_TOKEN,)
except Exception as excp:
    send_log.exception(excp)

__license__ = "GNU Affero General Public License v3.0"
__copyright__ = "PYTEL Copyright (C) 2023-present kastaid"

start_time = time()

Rooters: Path = Path(
    __file__
).parent.parent

dirs = "cache/"
if not (Rooters / dirs).exists():
    (Rooters / dirs).mkdir(
        parents=True,
        exist_ok=True,
    )
else:
    for f in (Rooters / dirs).rglob(
        "*"
    ):
        if f.is_dir():
            rmtree(f)
        else:
            f.unlink(missing_ok=True)

try:
    from pyrogram import Client

    pytel_tgb = Client(
        name="pytel",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=TGB_TOKEN,
        in_memory=True,
    )
    pytel_1 = (
        PytelClient(
            name="pytel1",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION1,
        )
        if SESSION1
        else None
    )
    pytel_2 = (
        PytelClient(
            name="pytel2",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION2,
        )
        if SESSION2
        else None
    )
    pytel_3 = (
        PytelClient(
            name="pytel3",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION3,
        )
        if SESSION3
        else None
    )
    pytel_4 = (
        PytelClient(
            name="pytel4",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION4,
        )
        if SESSION4
        else None
    )
    pytel_5 = (
        PytelClient(
            name="pytel5",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION5,
        )
        if SESSION5
        else None
    )
    pytel = PytelClient(name="pytel")
except Exception as excp:
    send_log.exception(excp)
    exit(1)

pytl = [
    _
    for _ in [
        pytel_1,
        pytel_2,
        pytel_3,
        pytel_4,
        pytel_5,
    ]
    if _
]

if pytel:
    for pytel_ in pytl:
        pytel._client.append(pytel_)
else:
    pytel = None
