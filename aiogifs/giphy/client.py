from .http import HTTPClient, Route
from typing import Optional
from .types import AgeRating
from .models import GiphyResponse
from aiohttp import ClientSession # just for type hinting
import asyncio

class GiphyClient:
    def __init__(self, *, api_key: str, session: Optional[ClientSession] = None):
        self._auth = api_key
        self.http = HTTPClient(api_key = self._auth, session = session)

    async def search(self, query: str, *, limit: Optional[int] = 25, offset: Optional[int] = 0, rating: Optional[AgeRating] = None, language: Optional[str] = None, user_proxy: Optional[str] = None) -> GiphyResponse:
        """Searches the Giphy API.

        :param query: Search query term or phrase.
        :type query: str
        :param limit: The maximum number of objects to return, defaults to 25
        :type limit: Optional[int], optional
        :param offset: The maximum number of objects to return, defaults to 0
        :type offset: Optional[int], optional
        :param rating: Filters results by specified rating, defaults to None
        :type rating: Optional[AgeRating], optional
        :param language: Specify default language for regional content, defaults to None
        :type language: Optional[str], optional
        :param user_proxy: An ID/proxy for a specific user, defaults to None
        :type user_proxy: Optional[str], optional
        :return: A GiphyResponse object. Holds properties such as `.media` and `.meta`.
        :rtype: GiphyResponse
        """
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
        return GiphyResponse(raw_payload = resp)

    async def trending(self, *, limit: Optional[int] = 25, offset: Optional[int] = 0, rating: Optional[AgeRating] = None, language: Optional[str] = None, user_proxy: Optional[str] = None) -> GiphyResponse:
        """Fetches the trending GIF's from Giphy.

        :param limit: The maximum number of objects to return, defaults to 25
        :type limit: Optional[int], optional
        :param offset: The maximum number of objects to return, defaults to 0
        :type offset: Optional[int], optional
        :param rating: Filters results by specified rating, defaults to None
        :type rating: Optional[AgeRating], optional
        :param language: Specify default language for regional content, defaults to None
        :type language: Optional[str], optional
        :param user_proxy: An ID/proxy for a specific user, defaults to None
        :type user_proxy: Optional[str], optional
        :return: A GiphyResponse object. Holds properties such as `.media` and `.meta`.
        :rtype: GiphyResponse
        """
        params = {
            "limit": limit,
            "offset": offset,
            "rating": rating,
            "lang": language,
            "random_id": user_proxy
        }
        params = self._filter_params(params)
        route = Route("/gifs/search", params)
        resp = await self.http.request(route)
        return GiphyResponse(raw_payload = resp)
        
    def  _filter_params(self, map: dict) -> dict:
        new_dict = {k: v for k, v in map.items() if v is not None}
        return new_dict

    async def connect(self):
        """Opens the aiohttp.ClientSession(), thus allowing connections to the Giphy API
        """
        return await self.http.open_session()

    def open(self):
        """Called in __init__. Opens the aiohttp.ClientSession()
        """
        asyncio.get_event_loop().run_until_complete(self.http.open_session())