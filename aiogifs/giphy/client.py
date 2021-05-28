from .http import HTTPClient, Route
from typing import Optional
from .types import AgeRating
from aiohttp import ClientSession # just for type hinting
import asyncio

class GiphyClient:
    def __init__(self, *, api_key: str, session: Optional[ClientSession] = None):
        self._auth = api_key
        self.http = HTTPClient(api_key = self._auth, session = session)
        self.open()

    async def search(self, query: str, *, limit: Optional[int] = 25, offset: Optional[int] = 0, rating: Optional[AgeRating] = None, language: Optional[str] = None, user_proxy: Optional[str] = None):
        params = {
            "q": query,
            "limit": limit,
            "offset": offset,
            "rating": rating,
            "lang": language,
            "random_id": user_proxy
        }
        params = self._filter_params(params)
        route = Route("/gifs/search", params)
        resp = await self.http.request(route)
        return resp
        
    def  _filter_params(self, map: dict) -> dict:
        new_dict = {k: v for k, v in map.items() if v is not None}
        return new_dict

    async def close(self):
        """Cleans up. Primarily HTTP Session closing.
        """
        return await self.http.cleanup()

    def open(self):
        """Called in __init__. Opens the aiohttp.ClientSession()
        """
        asyncio.get_event_loop().run_until_complete(self.http.open_session())
