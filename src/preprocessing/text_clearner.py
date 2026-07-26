class TextCleaner:
    def clean(self, text):
        text = self.normalize(text)
        text = self.remove_symbols(text)
        return text

    def normalize(self, text):
        return text.lower()

    def remove_symbols(self, text):
        symbols = ",.;:¡!¿?()[]{}\"'"
        for symbol in symbols:
            text = text.replace(symbol, "")
        return text
