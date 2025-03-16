class FourDigitYearConverter:
    regex = r"\d{4}"

    def to_python(self, value: str) -> int:
        """Преобразует строку в число (год)"""
        return int(value)

    def to_url(self, value: int) -> str:
        """Преобразует число обратно в строку"""
        return f"{value}"