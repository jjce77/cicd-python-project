from app.dictionary import Dictionary


def test_dictionary_placeholder() -> None:
    dictionary = Dictionary()
    assert isinstance(dictionary, Dictionary)
