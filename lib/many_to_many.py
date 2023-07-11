class Author:

    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.author]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:

    all = []
    
    def __init__(self, title):
        self.title = title
        self.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.book]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:

    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise Exception
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self._date = date
        else:
            raise Exception
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if isinstance(royalties, int):
            self._royalties = royalties
        else:
            raise Exception
        
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: contract.date)
    
    # @classmethod
    # def contracts_by_date(cls, date):
    #     return [contract for contract in cls.all if contract.date == date]