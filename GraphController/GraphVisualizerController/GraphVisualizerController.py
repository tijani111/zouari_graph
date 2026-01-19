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
from GraphController.GraphLayoutHandler.IGraphLayoutHandler import IGraphLayoutHandler
from GraphController.GraphVisualizerController.IGraphVisualizerController import IGraphVisualizerController
from GraphController.SubtreeMover.SubtreeMover import SubtreeMover
from GraphModel.EdgeRenderingMasterStates import EdgeRenderingMasterStates
from View.GraphView.IGraphVisualizer import IGraphVisualizer


class GraphVisualizerController(IGraphVisualizerController):
    """
    The GraphVisualizerController is responsible for controlling the visualization of a graph.
    It integrates and synchronizes various components like GraphVisualizer and GraphLayoutHandler
    to manage the display and behavior of connection and similarity edges in the graph.
    """

    def __init__(self, graph_visualizer: IGraphVisualizer, graph_layout_handler: IGraphLayoutHandler,
                 edge_rendering_master_states: EdgeRenderingMasterStates, subtree_mover: SubtreeMover):
        self.graph_visualizer = graph_visualizer
        self.graph_layout_handler = graph_layout_handler
        self.edge_rendering_master_states = edge_rendering_master_states
        self.subtree_mover = subtree_mover

        self.__init_states()

    def __init_states(self):
        """
        Initialize and synchronize the master states.
        """
        self.graph_visualizer.set_connection_edges_rendering(self.edge_rendering_master_states.connections_master_state)
        self.graph_visualizer.set_similarity_edges_rendering(self.edge_rendering_master_states.similarity_master_state)
        self.__synchronize_states()

    def __synchronize_states(self):
        """
        Synchronizing of the states. The rendering is the master state. If anything causes the rendering and force
        calculation to be out of sync, the state of the rendering is passed on to the force calculation to ensure
        that they are always in sync. Rendering is preferred as this ensures that the behavior is always coherent
        with what the user sees.
        """
        self.edge_rendering_master_states.connections_master_state = self.graph_visualizer.get_connection_edges_rendering_state()
        self.edge_rendering_master_states.similarity_master_state = self.graph_visualizer.get_similarity_edges_rendering_state()

        self.graph_layout_handler.set_connection_based_attraction_force(
            self.edge_rendering_master_states.connections_master_state)
        self.graph_layout_handler.set_similarity_based_attraction_force(
            self.edge_rendering_master_states.similarity_master_state)

    def toggle_connection_edges(self):
        self.graph_visualizer.set_connection_edges_rendering(
            not self.graph_visualizer.get_connection_edges_rendering_state())
        self.__synchronize_states()

    def toggle_similarity_edges(self):
        self.graph_visualizer.set_similarity_edges_rendering(
            not self.graph_visualizer.get_similarity_edges_rendering_state())
        self.__synchronize_states()

    def move_selected_node_subtree(self, selected_node, dx, dy):
        if self.edge_rendering_master_states.connections_master_state:
            self.subtree_mover.move_selected_node_subtree(selected_node, dx, dy)

        else:
            self.subtree_mover.move_selected_node(selected_node, dx, dy)

    def request_update_node_color_by_type(self):
        self.graph_visualizer.set_node_color_based_on_type()
