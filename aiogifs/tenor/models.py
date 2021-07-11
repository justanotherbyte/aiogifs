from typing import List, Union, Optional


class MP4:
    __slots__ = ("_data", "size", "dimensions", "duration", "preview_url", "url")

    def __init__(self, *, data: dict):
        self.size = data.get("size")
        self.dimensions = data.get("dims")
        self.duration = data.get("duration")
        self.preview_url = data.get("preview")
        self.url = data.get("url")


class GIF:
    __slots__ = ("size", "dimensions", "preview_url", "url")
    
    def __init__(self, *, data: dict):
        self.size = data.get("size")
        self.dimensions = data.get("dims")
        self.preview_url = data.get("preview")
        self.url = data.get("url")
    

class WebM(GIF):
    pass

class TinyMP4(MP4):
    pass

class LoopedMP4(MP4):
    pass

class NanoMP4(MP4):
    pass

class TinyGIF(GIF):
    pass

class NanoGIF(GIF):
    pass

class TinyWebM(WebM): 
    pass

class MediumGIF(GIF):
    pass

class Media:
    def __init__(self, *, data: dict, raw_object: dict):
        self._data = data
        self._raw_data = raw_object

    def _create_cls(self, key: str, cls):
        obj = self._data.get(key)
        if obj is None:
            return None
        else:
            return cls(data = obj)
    @property
    def url(self) -> str:
        """Returns a quick access url for the `Media` object. Usually a `GIF` file type.

        :return: A string containing a URL.
        :rtype: str
        """
        return self._raw_data.get("url")

    @property
    def item_url(self) -> str:
        """Returns a url that links to the official Tenor Page to the GIF.

        :return: A string containing a URL.
        :rtype: str
        """
        return self._raw_data.get("itemurl")

    @property
    def mp4(self) -> Optional[MP4]:
        """Returns a `MP4` object. Contains Media Properties.

        :return: Returns a `MP4` object.
        :rtype: Optional[MP4]
        """
        return self._create_cls("mp4", MP4)

    @property
    def gif(self) -> Optional[GIF]:
        """Returns a `GIF` object. Contains Media Properties.

        :return: Returns a `GIF` object.
        :rtype: Optional[GIF]
        """
        return self._create_cls("gif", GIF)
    
    @property
    def webm(self) -> Optional[WebM]:
        """Returns a `WebM` object. Contains Media Properties.

        :return: Returns a `WebM` object.
        :rtype: Optional[WebM]
        """
        return self._create_cls("webm", WebM)
    
    @property
    def tiny_mp4(self) -> Optional[TinyMP4]:
        """Returns a `TinyMP4` object. Contains Media Properties.

        :return: Returns a `TinyMP4` object. Subclasses `MP4`.
        :rtype: Optional[TinyMP4]
        """
        return self._create_cls("tinymp4", TinyMP4)

    @property
    def looped_mp4(self) -> Optional[LoopedMP4]:
        """Returns a `LoopedMP4` object. Contains Media Properties.

        :return: Returns a `LoopedMP4` object. Subclasses `MP4`.
        :rtype: Optional[LoopedMP4]
        """
        return self._create_cls("loopedmp4", LoopedMP4)

    @property
    def nano_mp4(self) -> Optional[NanoMP4]:
        """Returns a `NanoMP4` object. Contains Media Properties.

        :return: Returns a `NanoMP4` object. Subclasses `MP4`.
        :rtype: Optional[NanoMP4]
        """
        return self._create_cls("nanomp4", NanoMP4)

    @property
    def tiny_gif(self) -> Optional[TinyGIF]:
        """Returns a `TinyGIF` object. Contains Media Properties.

        :return: Returns a `TinyGIF` object. Subclasses `GIF`.
        :rtype: Optional[TinyGIF]
        """
        return self._create_cls("tinygif", TinyGIF)

    @property
    def nano_gif(self) -> Optional[NanoGIF]:
        """Returns a `NanoGIF` object. Contains Media Properties.

        :return: Returns a `NanoGIF` object. Subclasses `GIF`.
        :rtype: Optional[NanoGIF]
        """
        return self._create_cls("nanogif", NanoGIF)

    @property
    def tiny_webm(self) -> Optional[TinyWebM]:
        """Returns a `TinyWebM` object. Contains Media Properties.

        :return: Returns a `TinyWebM` object. Subclasses `WebM`.
        :rtype: Optional[TinyWebM]
        """
        return self._create_cls("tinywebm", TinyWebM)

    @property
    def medium_gif(self) -> Optional[MediumGIF]:
        """Returns a `MediumGIF` object. Contains Media Properties.

        :return: Returns a `MediumGIF` object. Subclasses `GIF`.
        :rtype: Optional[MediumGIF]
        """
        return self._create_cls("mediumgif", MediumGIF)



class TenorResponse:
    def __init__(self, *, data: dict):
        self._data = data
        
    @property
    def media(self) -> List[Optional[Media]]:
        """Generates the media objects and returns them in a list.

        :return: A list of `Media` objects.
        :rtype: Optional[List[Media]]
        """
        results = self._data.get("results")
        if results is None or len(results) == 0:
            return None
        
        media_objs = []
        for i in results:
            media_obj = Media(data = i.get("media")[0], raw_object = i)
            media_objs.append(media_obj)

        return media_objs

    @property
    def raw(self) -> dict:
        """Returns the raw json payload received from the Tenor API.

        :return: The raw json payload fetched from the Tenor API.
        :rtype: dict
        """
        return self._data
