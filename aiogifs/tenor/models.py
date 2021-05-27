

class TenorResponse:
    def __init__(self, *, payload: dict):
        self.payload = payload

    




class Asset:
    def __init__(self, *, media_type: str, object_data: dict):
        self._type = media_type
        self._data = object_data

    @property
    def type(self) -> str:
        return self._type
    