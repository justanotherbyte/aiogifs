import aiohttp
from typing import Optional
import warnings

class Route:
    __slots__ = ("BASE", "method", "endpoint", "url", "params")
    
    BASE = "https://g.tenor.com/v1"
    
    def __init__(self, endpoint: str, params: dict, method: str = "GET", **kwargs):
        self.method = method
        self.endpoint = endpoint
        self.url = self.BASE + endpoint.format(**kwargs)
        self.params = params



class HTTPClient:
    __slots__ = ("__session", "_auth")

    def __init__(self, *, api_key: Optional[str] = None, session: Optional[aiohttp.ClientSession] = None):
        self.__session = session
        self._auth = api_key
    
    async def open_session(self):
        if not self.__session:
            self.__session = aiohttp.ClientSession(raise_for_status = True)
        elif not self.__session.raise_for_status:
            warnings.warn("raise_for_status is not enabled on your ClientSession. No HTTP Error raising is enabled!")

    async def request(self, route: Route) -> dict:
        if self._auth and route.params.get("key") is None:
            route.params.update(key = self._auth)
        async with self.__session.request(route.method, route.url, params = route.params) as resp:
            data = await resp.json()
        return data

    async def cleanup(self):
        await self.__session.close()
        self.__session = None
    
