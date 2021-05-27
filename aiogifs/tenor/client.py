from .http import HTTPClient, Route
import asyncio
from aiohttp import ClientSession # just for type hinting
from typing import Optional
from .types import MediaFilter, AspectRatio, ContentFilter
from .models import TenorResponse


class TenorClient:
    def __init__(self, *, api_key: str, session: Optional[ClientSession] = None):
        self._auth = api_key
        self.http = HTTPClient(api_key = self._auth, session = session)
        self.open()

    async def search(self, query: str, *, locale: Optional[str] = None, content_filter: Optional[ContentFilter] = "off", media_filter: Optional[MediaFilter] = None, ar_range: Optional[AspectRatio] = None, limit: Optional[int] = None, pos: Optional[int] = None, anon_id: Optional[str] = None) -> TenorResponse:
        params = {
            "q": query,
            "locale": locale,
            "contentfilter": content_filter,
            "mediafilter": media_filter,
            "ar_range": ar_range,
            "limit": limit,
            "pos": pos,
            "anon_id": anon_id

        }
        params = self._filter_params(params)
        route = Route("/search", params = params)
        data = await self.http.request(route)
        return TenorResponse(data = data)

    async def close(self):
        return await self.http.cleanup()

    def open(self):
        asyncio.get_event_loop().run_until_complete(self.http.open_session())

    def  _filter_params(self, map: dict) -> dict:
        new_dict = {k: v for k, v in map.items() if v is not None}
        return new_dict
