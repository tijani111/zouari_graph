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


class IGraphVisualizerController(ABC):

    @abstractmethod
    def toggle_connection_edges(self):
        """
        Toggles the rendering of the regular connection edges on and off.
        """

    @abstractmethod
    def toggle_similarity_edges(self):
        """
        Toggles the rendering of the similarity edges on and off.
        """
    @abstractmethod
    def move_selected_node_subtree(self, selected_node, dx, dy):
        """
        Dragging of the subtree of the selected Node.
        """

    @abstractmethod
    def request_update_node_color_by_type(self):
        """
        Request update of the Colors of all Nodes based on their Typ.
        """