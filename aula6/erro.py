class Error:

    @staticmethod
    def error_500() -> None:
        print("Internal Server Error!")

    @staticmethod
    def error_404() -> None:
        print("Page not found!")

Error.entrada()