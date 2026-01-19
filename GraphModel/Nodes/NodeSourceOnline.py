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


class NodeSourceOnline(NodeSource):
    """
    he `NodeSourceOnline` class extends the `NodeSource` class and is specifically designed to represent
    online sources within a graph model. It encapsulates key attributes related to web-based content,
    such as the document title, website title, URL, and access date, alongside the standard source attributes
    such as author and publication year.

    """

    def __init__(self, titel_of_the_document, source_author, year_of_publication, titel_of_the_website, URL,
                 date_of_access, comment="", x=0, y=0):
        """
        Initializes a new instance of the Node class.

        :param: titel_of_the_document: Titel of the Source
        :param: source_author: Author(s) of the Source
        :param: year_of_publication: Year of publication of the Source
        :param: titel_of_the_website: The name of the overall website
        :param: URL: The full web address where the content can be accessed.
        :param: date_of_access: The date the website has been accessed.
        """

        self.titel_of_the_document = titel_of_the_document
        self.titel_of_the_website = titel_of_the_website
        self.URL = URL
        self.date_of_access = date_of_access

        super().__init__(source_author, year_of_publication, comment, x, y)

    def generate_description(self):
        self.description = ("\n### Autor:\n" + self.source_author +
                            "\n### Veröffentlichungsjahr:\n" + self.year_of_publication +
                            "\n### Titel:\n" + self.titel_of_the_document +
                            "\n### Titel der Website:\n" + self.titel_of_the_website +
                            "\n ### Verfügbar unter:\n" + self.URL +
                            "\n### Zugriff am:\n" + self.date_of_access)
