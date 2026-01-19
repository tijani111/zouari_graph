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


class NodeSourcePaper(NodeSource):
    """
    The `NodeSourcePaper` class extends the `NodeSource` class and is tailored for representing scholarly articles
    within a graph model. It includes specific attributes essential for detailed bibliographic representation
    of academic papers, such as the article title, journal title, and volume and issue information,
    in addition to the author and year of publication.

    """

    def __init__(self, titel_of_the_article, source_author, year_of_publication, titel_of_the_journal, volume_and_issue,
                 comment="",
                 x=0, y=0):
        """
        Initializes a new instance of the Node class.

        :param: titel_of_the_article: Titel of the Article
        :param: source_author: Author(s) of the Article
        :param: year_of_publication: Year of publication of the Source
        :param: titel_of_the_journal: The name of the journal in which the article was published.
        :param: volume_and_issue:   The volume number and, if applicable, the issue number
                                    of the journal where the article appears.
        """
        self.titel_of_the_article = titel_of_the_article
        self.titel_of_the_journal = titel_of_the_journal
        self.volume_and_issue = volume_and_issue

        super().__init__(source_author, year_of_publication, comment, x, y)

    def generate_description(self):
        self.description = ("\n### Autor:\n" + self.source_author +
                            "\n### Veröffentlichungsjahr:\n" + self.year_of_publication +
                            "\n### Titel:\n" + self.titel_of_the_article +
                            "\n### In:\n" + self.titel_of_the_journal +
                            "\n### Bandnummer(Ausgabennummer):\n" + self.volume_and_issue)
