import os

from CustomApplicationSettings import CustomApplicationSettings
from ComponentAssembly.GraphAnalyzer import GraphAnalyzer
from GraphController.GraphExporter import GraphExporter
from GraphController.GraphImporter import GraphImporter
from GraphController.GraphLayoutHandler import IGraphLayoutHandler
from GraphController.GraphLayoutHandler.GraphLayoutHandler import AutoLayoutHandler
from GraphController.GraphVisualizerController.GraphVisualizerController import GraphVisualizerController
from GraphController.NodeFinder.NodeFinder import NodeFinder
from GraphController.SubtreeMover.SubtreeMover import SubtreeMover
from GraphModel.EdgeRenderingMasterStates import EdgeRenderingMasterStates
from GraphModel.Graph import Graph
from GraphModel.RandomGraphGenerator import RandomGraphGenerator
from GraphModel.SelectedNodeContainer import SelectedNodeContainer
from ComponentAssembly.IComponentProvider import IComponentProvider
from GraphController.ScaleOffSetTransformer import IScaleOffsetTransformer
from View.GraphView.CustomGraphVisualizer import CustomGraphVisualizer
from GraphController.ScaleOffSetTransformer.ScaleOffsetTransformer import ScaleOffsetTransformer
from GraphController.ScreenDragHandler.ScreenDragHandler import ScreenDragHandler, IDragHandler
from View.GraphView.ViewPort import ViewPort
from View.UI.NodeDetailsWindow import INodeDetailsWindow
from View.UI.NodeDetailsWindow.MarkdownTextRenderer import MarkdownTextRenderer
from View.UI.NodeDetailsWindow.NodeDetailsWindow import NodeDetailsWindow
from View.UI.UIThemes import LightBlueTheme
from View.UI.Colors import Colors
from View.UI.MainMenu.MainMenu import MainMenu


class CustomComponentAssembler(IComponentProvider):
    """
    Custom ComponentAssembler fuer den persoenlichen Graphen.
    Verwendet angepasste Layout- und Visualisierungseinstellungen,
    ohne den Stammcode zu veraendern.
    """

    uiTheme = LightBlueTheme()

    def __init__(self, graph: Graph, screen, window_width, window_height):
        self.application_settings = CustomApplicationSettings()
        self.screen = screen
        self.window_width = window_width
        self.window_height = window_height

        # Graph
        self.graph = graph

        # Analyzing the contents of the graph
        graph_analyzer = GraphAnalyzer()
        graph_analyzer.display_statistics(graph)

        # Container for currently selected Node
        self.selected_node_container = SelectedNodeContainer()

        if self.application_settings.debug_mode:
            self.graph.nodes.clear()
            self.node_generator = RandomGraphGenerator(self.graph)
            self.node_generator.create_random_nodes(100, 150)

        # Scale and Offset Handling
        self.scale_offset_transformer: IScaleOffsetTransformer
        self.scale_offset_transformer = ScaleOffsetTransformer(self.window_width, self.window_height,
                                                               self.application_settings)

        # Calculate Similarity
        self.SIMILARITY_Threshold = 0.8
        if self.application_settings.allow_calculation_of_similarity:
            from GraphController.SimilarityCalculation.MiniLMSimilarityCalculator import MiniLMSimilarityCalculator
            self.similarity_calculator = MiniLMSimilarityCalculator(self.graph, self.SIMILARITY_Threshold)
        else:
            self.similarity_calculator = None

        # Graph Model Layout
        self.graph_layout_handler: IGraphLayoutHandler
        self.graph_layout_handler = AutoLayoutHandler(0, 0, 50000000,
                                                      self.scale_offset_transformer, self.screen,
                                                      self.uiTheme.BARNES_HUT_COLOR, self.graph,
                                                      self.SIMILARITY_Threshold, self.application_settings)

        # Drag Screen
        self.drag_handler: IDragHandler
        self.drag_handler = ScreenDragHandler(self.scale_offset_transformer)

        # Drag Graph
        self.subtree_mover = SubtreeMover()

        # Graph Visualization
        self.view_port = ViewPort(self.scale_offset_transformer, self.window_width, self.window_height)
        self.graph_visualizer = CustomGraphVisualizer(self.window_width, self.scale_offset_transformer,
                                                      self.screen, self.graph, self.selected_node_container,
                                                      self.uiTheme, self.SIMILARITY_Threshold,
                                                      self.view_port, self.application_settings)
        self._apply_custom_node_colors()
        self._center_view_on_graph()
        self.scale_offset_transformer.subscribe(self.graph_visualizer)

        # Controller for the Graph Visualization
        edge_rendering_master_states = EdgeRenderingMasterStates()
        self.graph_visualizer_controller = GraphVisualizerController(self.graph_visualizer,
                                                                     self.graph_layout_handler,
                                                                     edge_rendering_master_states,
                                                                     self.subtree_mover)

        # Resources Path
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self.resources_folder_path = os.path.join(current_directory, '../Resources')

        # Text Renderer
        markdown_text_renderer = MarkdownTextRenderer(self.uiTheme)

        # Node Details Window
        self.node_details_window: INodeDetailsWindow
        self.node_details_window = NodeDetailsWindow(self.window_width, self.window_height, self.screen, self.uiTheme,
                                                     self.selected_node_container,
                                                     self.resources_folder_path, markdown_text_renderer)

        # Find Node at Position
        self.node_finder = NodeFinder(self.graph, self.scale_offset_transformer)

        self.graph_exporter = GraphExporter(self.graph, self.resources_folder_path)
        self.graph_importer = GraphImporter(self.graph, self.resources_folder_path, graph_analyzer)

        # Initialisiere das Menue
        self.main_menu = MainMenu(self.graph, self.window_width, self.window_height, 0, 0, 10, self.uiTheme,
                                  self.resources_folder_path, self.graph_exporter,
                                  self.graph_importer, self.similarity_calculator,
                                  self.graph_visualizer_controller, edge_rendering_master_states,
                                  self.application_settings.create_similarity_toggle,
                                  self.application_settings.create_connections_toggle,
                                  self.application_settings.create_add_button)

    def _apply_custom_node_colors(self):
        for node in self.graph.nodes:
            author = getattr(node, "author", "")
            if author == "Topic":
                node.color = Colors.VANADYL_BLUE
            elif author == "Kategorie":
                node.color = Colors.HARLEY_DAVIDSON_ORANGE
            elif author == "Perspektive":
                node.color = Colors.PROTOSS_PYLON
            elif author == "Wissen":
                node.color = Colors.HINT_OF_PENSIVE
            elif author == "Quelle":
                node.color = Colors.NODE_SOURCE_ONLINE

    def _center_view_on_graph(self):
        if not self.graph.nodes:
            return
        min_x = min(node.x for node in self.graph.nodes)
        max_x = max(node.x for node in self.graph.nodes)
        min_y = min(node.y for node in self.graph.nodes)
        max_y = max(node.y for node in self.graph.nodes)
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2

        self.scale_offset_transformer.offset_x = self.window_width // 2 - int(center_x * self.scale_offset_transformer.zoom)
        self.scale_offset_transformer.offset_y = self.window_height // 2 - int(center_y * self.scale_offset_transformer.zoom)
        self.scale_offset_transformer.change_notifier()

    def get_screen(self):
        return self.screen

    def get_ui_theme(self):
        return self.uiTheme

    def get_node_details_window(self):
        return self.node_details_window

    def get_scale_offset_transformer(self):
        return self.scale_offset_transformer

    def get_selected_node_container(self):
        return self.selected_node_container

    def get_graph_layout_handler(self):
        return self.graph_layout_handler

    def get_node_finder(self):
        return self.node_finder

    def get_drag_handler(self):
        return self.drag_handler

    def get_subtree_mover(self):
        return self.subtree_mover

    def get_main_menu(self):
        return self.main_menu

    def get_graph_visualizer(self):
        return self.graph_visualizer

    def get_graph_visualizer_controller(self):
        return self.graph_visualizer_controller
