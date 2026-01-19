"""
Copyright (C) 2023 TH Köln – University of Applied Sciences

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

from GraphModel.Nodes.NodeSource import NodeSource


class NodeSourceBook(NodeSource):
    """
    The `NodeSourceBook` class extends the `NodeSource` class and adds specific attributes for representing
    bibliographic information of a book within a graph model.
    This class encapsulates details such as the book's title, author, publication year, and other
    essential bibliographic metadata like place of publication, publisher, edition, and ISBN.
    """

    def __init__(self, titel_of_the_book, source_author, year_of_publication, place_of_publication, publisher, ISBN,
                 comment="", edition="1st edition", x=0, y=0):
        """
        Initializes a new instance of the Node class.

        :param: titel_of_the_book,source_author: The complete title of the book, and any subtitle if present.
        :param: source_author: Author(s) of the Book
        :param: year_of_publication: Year of publication of the Source
        :param: place_of_publication: The city where the publisher is located.
        :param: publisher: The name of the publishing company.
        :param: ISBN: International Standard Book Number
        """
        self.titel_of_the_book = titel_of_the_book
        self.edition = edition
        self.place_of_publication = place_of_publication
        self.publisher = publisher
        self.ISBN = ISBN

        super().__init__(source_author, year_of_publication, comment, x, y)

    def generate_description(self):
        self.description = ("\n### Autor:\n" + self.source_author +
                            "\n### Veröffentlichungsjahr:\n" + self.year_of_publication +
                            "\n### Titel:\n" + self.titel_of_the_book +
                            "\n ### Auflage:\n" + self.edition +
                            "\n### Ort:\n" + self.place_of_publication +
                            "\n### Verlag:\n" + self.publisher +
                            "\n### ISBN:\n" + self.ISBN)
