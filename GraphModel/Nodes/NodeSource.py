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

from abc import ABC, abstractmethod
from GraphModel.Nodes.NodeKnowledge import NodeKnowledge


class NodeSource(NodeKnowledge):
    """
    The `NodeSource` class extends the `NodeKnowledge` class and serves as an abstract base class for
    nodes representing sources within a graph model.
    It is designed to encapsulate basic bibliographic information, including
    the author and publication year of a source.

    :param: titel: Titel of the Source
    :param: source_author: Author(s) of the Source
    :param: year_of_publication: Year of publication of the Source
    :param: comment: An optional comment or additions to the source
    """

    def __init__(self, source_author, year_of_publication, comment, x=0, y=0):
        self.description = ""
        self.titel = ""

        self.source_author = source_author
        self.year_of_publication = year_of_publication
        self.comment = comment

        self.generate_titel()
        self.generate_description()
        self.add_comment_to_description()

        super().__init__(self.description, self.titel, x, y)

    def generate_titel(self):
        self.titel = ("(" + self.source_author + ", " + self.year_of_publication + ")")

    @abstractmethod
    def generate_description(self):
        pass

    def add_comment_to_description(self):
        self.description = self.description + ("\n### Anmerkungen:\n" + self.comment)
