from typing import List

class Media:
    def __init__(self, *, data: dict):
        self._data = data

    @property
    def type(self) -> str:
        """Returns the type of Media. Example: GIF (gif).

        :rtype: str
        """
        return self._data.get("type")

    @property
    def id(self) -> str:
        """Returns the id of the Media Object. Example: SyBtFOwyGO4JW

        :rtype: str
        """
        return self._data.get("id")

    @property
    def url(self) -> str:
        """Returns the URL of the Media Object.

        :rtype: str
        """
        return self._data.get("url")

    @property
    def slug(self) -> str:
        """Returns the slug of a Giphy URL. This is usually the suffix of a Giphy view page.

        :rtype: str
        """
        return self._data.get("slug")

    @property
    def bitly_gif_url(self) -> str:
        """Returns the bitly_gif_url property of the Media Object returned.

        :rtype: str
        """
        return self._data.get("bitly_gif_url")

    @property
    def bitly_url(self) -> str:
        """Returns the bitly_url of the Media Object returned.

        :rtype: str
        """
        return self._data.get("bitly_url")
    
    @property
    def embed_url(self) -> str:
        """Returns the embed_url. This url has embed og:properties.

        :rtype: str
        """
        return self._data.get("embed_url")

    @property
    def title(self) -> str:
        """Returns the title of the Media Object. Usually the name of the object.

        :rtype: str
        """
        return self._data.get("title")
    
    @property
    def rating(self) -> str:
        """Returns the age rating of the Media Object.

        :rtype: str
        """
        return self._data.get("rating")


class Meta:
    def __init__(self, *, payload: dict):
        self._payload = payload

    @property
    def status(self) -> int:
        """Returns the status code of the request.

        :rtype: int
        """
        return self._payload.get("status")

    @property
    def message(self) -> str:
        """Returns the message linked to the status of the request.

        :rtype: str
        """
        return self._payload.get("msg")

    @property
    def msg(self) -> str:
        """Alias for `message`.

        :rtype: str
        """
        return self._payload.get("msg")

    @property
    def response_id(self) -> str:
        """Returns the response_id of the request.

        :rtype: str
        """
        return self._payload.get("response_id")


class GiphyResponse:
    def __init__(self, *, raw_payload: dict):
        self._rp = raw_payload

    @property
    def media(self) -> List[Media]:
        """Returns a list of Media Objects.

        :return: A list of Media Objects containing properties such as `.url`
        :rtype: List[Media]
        """
        media_objs = []
        for i in self._rp.get("data"):
            media_objs.append(Media(data = i))

        return media_objs

    @property
    def meta(self) -> Meta:
        """Returns the Meta object.

        :return: Meta Object - Holds request information.
        :rtype: Meta
        """
        meta_array = self._rp.get("meta")
        return Meta(payload = meta_array)

