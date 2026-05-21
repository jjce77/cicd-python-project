from app.words import build_word

def test_build_word_placeholder() -> None:
    # Le pasamos None a los parámetros extra para ejecutar la función completa
    resultado = build_word([], None, None, None, None, None, None, None, None)
    assert resultado == []
