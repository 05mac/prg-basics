class EBook:
    def __init__(self, title, author, total_pages):
        # wartosci przekazane jako argument
        self.title = title
        self.author = author
        self.total_pages = total_pages

        # wartosci ktore zawsze sa takie same na starcie
        self.currentPages = 0
        self.is_open = False

    def openBook(self):
        self.is_open = True
        print("Książka została otwarta!")

    def closeBook(self):
        self.is_open = False
        print("Książka została zamknięta...")

    def readBook(self, numberPages):
        if self.is_open:
            self.currentPages += numberPages
            if self.currentPages > self.total_pages:
                self.currentPages = self.total_pages
            print(f"Czytasz... Jesteś na stronie {self.currentPages}")
        else:
            print("Książka jest zamknięta, nie da sie czytać")

    def showStatus(self):
        if self.is_open:
            print(f"Tytuł książki to: {self.title}")
            print(f"Autor książki to: {self.author}")
            print(f"Liczba stron książki to: {self.total_pages}")
            print(f"Aktualna strona książki to: {self.currentPages}")
        else:
            print("Nie wiemy zbyt wiele, książka jest zamknięta...")

    def nextPage(self):
        if self.is_open:
            self.currentPages += 1
            if self.currentPages > self.total_pages:
                self.currentPages = self.total_pages
        else:
            print("Baranie ksiażka jest zamknięta...")

    def previousPage(self):
        if self.is_open:
            self.currentPages -= 1
            if self.currentPages > self.total_pages:
                self.currentPages = self.total_pages
        else:
            print("Baranie ksiażka jest zamknięta...")
    