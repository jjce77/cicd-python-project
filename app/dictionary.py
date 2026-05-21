class Dictionary:
    def __init__(self) -> None:
        self._entries: dict[str, str] = {}

    def newentry(self, palabra: str, definicion: str) -> None:
        self._entries[palabra] = definicion

    def look(self, palabra: str) -> str:
        if palabra in self._entries:
            return self._entries[palabra]

        return f"Can't find entry for {palabra}"

