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

import os

import pygame

from GraphController.GraphExporter import GraphExporter
from GraphController.GraphImporter import GraphImporter
from GraphController.GraphVisualizerController.IGraphVisualizerController import IGraphVisualizerController
# from GraphController.SimilarityDetection.BERTSimilarityCalculator import BERTSimilarityCalculator
from GraphController.SimilarityCalculation.ISimilarityCalculator import ISimilarityCalculator
from GraphModel.EdgeRenderingMasterStates import EdgeRenderingMasterStates
from GraphModel.Graph import Graph
from View.UI.MainMenu.MenuItemButton import MenuButton
from View.UI.MainMenu.ToggleButton import ToggleButton
from View.UI.Label import Label
from View.UI.UIThemes import UITheme


class MainMenu:
    """
    The MainMenu class is responsible for managing and displaying the main menu in a graph visualization application.
    It provides interactive options such as exporting and importing graph data and handles user interactions
    with these options. The class integrates with the GraphExporter and GraphImporter for respective functionalities
    and manages the visual presentation and layout of the menu and its items.
    """

    def __init__(self, graph: Graph, window_width, window_height, menu_x, menu_y, spacing, ui_theme: UITheme,
                 resources_folder_path,
                 graph_exporter: GraphExporter, graph_importer: GraphImporter,
                 similarity_calculator: ISimilarityCalculator,
                 graph_visualizer_controller: IGraphVisualizerController,
                 edge_rendering_master_states: EdgeRenderingMasterStates,
                 create_similarity_toggle: bool = True,
                 create_connections_toggle: bool = True,
                 create_add_button: bool = True):
        """
        Initializes the MainMenu with necessary components, settings, and dimensions.

        :param: window_width: The width of the window where the menu is displayed.
        :param: window_height: The height of the window where the menu is displayed.
        :param: menu_x: The x-coordinate for the menu's position.
        :param: menu_y: The y-coordinate for the menu's position.
        :param: spacing: The spacing between menu items.
        :param: ui_theme: The UI theme used for styling the menu.
        :param: resources_folder_path: The path to the folder containing resources like icons.
        :param: graph_exporter: The GraphExporter instance used for exporting graph data.
        :param: graph_importer: The GraphImporter instance used for importing graph data.
        :param: similarity_calculator: Similarity Detector for Node Content
        :param: IGraphVisualizerController: Controller for the visualization of the Graph
        :param: create_similarity_toggle: Flag to create similarity toggle button.
        :param: create_connections_toggle: Flag to create connections toggle button.
        :param: create_add_button: Flag to create add button.
        """
        self.graph = graph
        self.similarity_calculator = similarity_calculator
        self.graph_visualizer_controller = graph_visualizer_controller
        self.edge_rendering_master_states = edge_rendering_master_states

        # Import Export
        self.graph_exporter = graph_exporter
        self.graph_importer = graph_importer

        # Icons
        icon_path = self.image_path = os.path.join(resources_folder_path, 'Icons')
        menu_button_icon_full_path = os.path.join(icon_path, "bars-solid.png")
        export_button_icon_full_path = os.path.join(icon_path, "file-export-solid.png")
        import_button_icon_full_path = os.path.join(icon_path, "file-import-solid.png")
        add_button_icon_full_path = os.path.join(icon_path, "add-solid.png")
        similarity_calc_button_icon_full_path = os.path.join(icon_path, "cos-similarity-solid.png")

        menu_button_icon = pygame.image.load(menu_button_icon_full_path)
        export_button_icon = pygame.image.load(export_button_icon_full_path)
        import_button_icon = pygame.image.load(import_button_icon_full_path)
        add_button_icon = pygame.image.load(add_button_icon_full_path)
        similarity_calc_button_icon = pygame.image.load(similarity_calc_button_icon_full_path)

        # Background Surface
        menu_background_width = window_width * 0.382 * 0.382
        menu_background_height = window_height
        self.menu_background_surface = pygame.Surface((menu_background_width, menu_background_height), pygame.SRCALPHA)
        self.menu_background_surface.fill(ui_theme.MAIN_MENU_BACKGROUND_COLOR)
        self.menu_x = menu_x + spacing
        self.menu_y = menu_y + spacing

        button_height = 30
        button_width = menu_background_width

        # Bestimmen des längsten Labels
        labels = [Label.MAIN_MENU, Label.EXPORT_BUTTON, Label.IMPORT_BUTTON, Label.ADD_BUTTON,
                  Label.SHOW_CONNECTION_EDGES, Label.SHOW_SIMILARITY_EDGES]
        longest_label = max(labels, key=len)

        # Berechnen der maximalen Schriftgröße
        self.label_area_width = (button_width * 0.618) * 0.618
        max_font_size = self.calculate_max_font_size(longest_label, self.label_area_width)

        # Erstellen des Font-Objekts
        self.font = pygame.font.SysFont(None, max_font_size)

        self.menu_button = MenuButton(self.menu_x, self.menu_y,
                                      button_width, button_height,
                                      self.menu_background_surface,
                                      ui_theme,
                                      icon=menu_button_icon,
                                      icon_x_offset=0,
                                      label=Label.MAIN_MENU,
                                      font=self.font)

        self.export_button = MenuButton(self.menu_x, self.menu_y + button_height + 10,
                                        button_width, button_height,
                                        self.menu_background_surface,
                                        ui_theme,
                                        icon=export_button_icon,
                                        icon_x_offset=3.5,
                                        label=Label.EXPORT_BUTTON,
                                        font=self.font)

        self.import_button = MenuButton(self.menu_x, self.menu_y + 2 * (button_height + 10),
                                        button_width, button_height,
                                        self.menu_background_surface,
                                        ui_theme,
                                        icon=import_button_icon,
                                        icon_x_offset=-3.5,
                                        label=Label.IMPORT_BUTTON,
                                        font=self.font)

        if create_add_button:
            self.add_button = MenuButton(self.menu_x, self.menu_y + 3 * (button_height + 10),
                                         button_width, button_height,
                                         self.menu_background_surface,
                                         ui_theme,
                                         icon=add_button_icon,
                                         icon_x_offset=0,
                                         label=Label.ADD_BUTTON,
                                         font=self.font)

            # Toggle-Button Hinzufügen
        if create_connections_toggle:
            self.connections_toggle = ToggleButton(self.menu_x, self.menu_y + 4 * (button_height + 10),
                                                   button_width, button_height,
                                                   self.menu_background_surface,
                                                   ui_theme,
                                                   label=Label.SHOW_CONNECTION_EDGES,
                                                   font=self.font)

        if create_similarity_toggle:
            self.similarity_toggle = ToggleButton(self.menu_x, self.menu_y + 5 * (button_height + 10),
                                                  button_width, button_height,
                                                  self.menu_background_surface,
                                                  ui_theme,
                                                  label=Label.SHOW_SIMILARITY_EDGES,
                                                  font=self.font)

        if self.similarity_calculator is not None:
            self.similarity_calc_button = MenuButton(self.menu_x, self.menu_y + 6 * (button_height + 10),
                                                     button_width, button_height,
                                                     self.menu_background_surface,
                                                     ui_theme,
                                                     icon=similarity_calc_button_icon,
                                                     icon_x_offset=0,
                                                     label=Label.SIMILARITY_CALC_BUTTON,
                                                     font=self.font)

        self.show_menu = False
        self.sync_toggle_to_modell()

    def calculate_max_font_size(self, text, max_width):
        # Starten mit einer angenommenen Schriftgröße
        font_size = 30
        font = pygame.font.SysFont(None, font_size)
        text_width, _ = font.size(text)

        # Verringerne der Schriftgröße, bis der Text in die Area passt
        while text_width > max_width:
            font_size -= 1
            font = pygame.font.SysFont(None, font_size)
            text_width, _ = font.size(text)

            if text_width < max_width:
                return font_size  # Die letzte passende Größe zurückgeben

        return font_size

    def calculate_max_font_size(self, text, max_width):
        # Starten mit einer angenommenen Schriftgröße
        font_size = 30
        font = pygame.font.SysFont(None, font_size)
        text_width, _ = font.size(text)

        # Verringerne der Schriftgröße, bis der Text in die Area passt
        while text_width > max_width:
            font_size -= 1
            font = pygame.font.SysFont(None, font_size)
            text_width, _ = font.size(text)

            if text_width < max_width:
                return font_size  # Die letzte passende Größe zurückgeben

        return font_size

    def handle_event(self, event):
        """
        Handles user interaction events with the menu, including clicks for expanding the menu,
        and exporting and importing actions.

        :param: event: The Pygame event to be processed.
        """
        if self.menu_button.click(event):
            self.show_menu = not self.show_menu

        if self.show_menu:
            self.menu_button.maximized = True
            if self.export_button.click(event):
                self.export_action()

            if self.import_button.click(event):
                self.import_action()

            if hasattr(self, 'add_button') and self.add_button.click(event):
                self.add_action()

            if self.similarity_calculator is not None and hasattr(self, 'similarity_calc_button'):
                if self.similarity_calc_button.click(event):
                    self.calculate_similarity_action()

            if hasattr(self, 'connections_toggle') and self.connections_toggle.click(event):
                self.toggle_connections()

            if hasattr(self, 'similarity_toggle') and self.similarity_toggle.click(event):
                if not self.similarity_toggle.disabled:
                    self.toggle_similarity()
        else:
            self.menu_button.maximized = False

    def draw(self, screen):
        """
        Draws the main menu and its items onto the screen.

        :param: screen: The Pygame screen object where the menu is rendered.
        """
        if self.show_menu:
            self.menu_button.draw(screen, True)
            screen.blit(self.menu_background_surface, (self.menu_x, self.menu_y))
            self.export_button.draw(screen)
            self.import_button.draw(screen)
            if hasattr(self, 'add_button'):
                self.add_button.draw(screen)
            if self.similarity_calculator is not None and hasattr(self, 'similarity_calc_button'):
                self.similarity_calc_button.draw(screen)
            # Zeichne den Toggle-Button
            if hasattr(self, 'similarity_toggle'):
                if self.graph.similarity_dict is None or not self.graph.similarity_dict:
                    self.similarity_toggle.disable(True)
                elif self.graph.similarity_dict is self.graph.similarity_dict and self.similarity_toggle.disabled:
                    self.similarity_toggle.disable(False)
                    self.sync_toggle_to_modell()
                self.similarity_toggle.draw(screen)
            if hasattr(self, 'connections_toggle'):
                self.connections_toggle.draw(screen)
        else:
            self.menu_button.draw(screen)

    def export_action(self):
        """
        Executes the action for exporting graph data. This method triggers the graph export process.
        """
        self.graph_exporter.export_graph()

    def import_action(self):
        """
        Executes the action for importing graph data. This method triggers the graph import process.
        """
        self.graph_importer.import_graph()
        self.graph_visualizer_controller.request_update_node_color_by_type()

    def add_action(self):
        """
        Executes the action for importing graph data. This method triggers the graph import process.
        The imported Graph will be added to the existing Graph.
        """
        self.graph_importer.import_graph(True)
        self.graph_visualizer_controller.request_update_node_color_by_type()

    def calculate_similarity_action(self):
        """
        Start Generation of Embeddings and calculate Similarities of Nodes.
        """
        self.similarity_calculator.start_similarity_computation()

    def toggle_connections(self):
        self.graph_visualizer_controller.toggle_connection_edges()
        self.sync_toggle_to_modell()

    def toggle_similarity(self):
        self.graph_visualizer_controller.toggle_similarity_edges()
        self.sync_toggle_to_modell()

    def sync_toggle_to_modell(self):
        if hasattr(self, 'connections_toggle'):
            self.connections_toggle.set_state(self.edge_rendering_master_states.connections_master_state)
        if hasattr(self, 'similarity_toggle'):
            self.similarity_toggle.set_state(self.edge_rendering_master_states.similarity_master_state)
