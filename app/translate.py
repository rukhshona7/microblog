from deep_translator import GoogleTranslator
from flask_babel import _


def translate(text, source_language, dest_language):
    try:
        result = GoogleTranslator(source=source_language, target=dest_language).translate(text)
        return result
    except Exception:
        return _('Error: the translation service failed.')