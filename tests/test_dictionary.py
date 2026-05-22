from app.dictionary import Dictionary


def test_newentry_stores_definition() -> None:
    dictionary = Dictionary()
    dictionary.newentry("Apple", "A fruit that grows on trees")

    assert dictionary.look("Apple") == "A fruit that grows on trees"


def test_look_returns_message_for_missing_word() -> None:
    dictionary = Dictionary()

    assert dictionary.look("Banana") == "Can't find entry for Banana"
