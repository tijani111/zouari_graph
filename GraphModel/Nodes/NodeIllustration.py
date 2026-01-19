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

from GraphModel.Nodes.Node import Node


class NodeIllustration(Node):
    """
    The `NodeIllustration` class extends the `Node` class by incorporating specific properties required
    for representing an illustrated node within a graph model. This class allows nodes to have an associated image.

    """

    def __init__(self, titel, image_name="image_placeholder.png", x=0, y=0):
        """
        Initializes a new instance of the Node class.

        :param: image_name: A string specifying the filename of the image representing the node.
                           Defaults to a placeholder image. All images are stored in the Resources Folder/Images.
        """
        self.image_name = image_name
        super().__init__(titel, x=0, y=0)
