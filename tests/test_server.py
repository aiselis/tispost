#
#    Copyright 2020 Alessio Pinna <alessio.pinna@aiselis.com>
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from tispost.server import Server
from unittest.mock import patch, AsyncMock
import pytest


@patch('tispost.server.aiopg', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_connect(mock):
    server = Server()
    assert not server.pool
    await server.connect()
    assert server.pool


@patch('tispost.server.aiopg', new_callable=AsyncMock)
@pytest.mark.asyncio
async def test_close_valid(mock):
    server = Server()
    await server.connect()
    await server.close()
    server.pool.close.assert_called()
