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
import pygame


class Legend:
    def __init__(self, screen, font, ui_theme, legend_position, legend_width, legend_height, legend_item_height, selected_node_color):
        self.screen = screen
        self.font = font
        self.ui_theme = ui_theme
        self.legend_position = legend_position
        self.legend_width = legend_width
        self.legend_height = legend_height
        self.legend_item_height = legend_item_height
        self.author_color_cache = {}
        self.legend_entries = {}
        self.selected_node_color = selected_node_color
        self.legend_surface_rect = pygame.Rect(legend_position[0], legend_position[1], legend_width, legend_height)


    def draw(self):
        # Berechnen der Höhe der Legende basierend auf der Anzahl der Autoren
        dynamic_legend_height = len(self.author_color_cache) * self.legend_item_height
        dynamic_legend_height = max(dynamic_legend_height, self.legend_item_height)

        if len(self.author_color_cache) < 2:
            return
        x, y = self.legend_position
        item_height = self.legend_item_height

        # Erstellen eines neuen Surface mit der dynamischen Höhe
        legend_surface = pygame.Surface((self.legend_width, dynamic_legend_height), pygame.SRCALPHA)
        legend_surface.fill(self.ui_theme.MAIN_MENU_BACKGROUND_COLOR)  # Füllen des Surface mit der Hintergrundfarbe

        # Zeichnen des Hintergrunds der Legende auf das Surface
        self.screen.blit(legend_surface, (x, y))

        # Variable zum Verfolgen der Anzahl der dargestellten Autoren
        displayed_authors = 0

        # Zeichnen der Einträge in der Legende
        for author, color in self.author_color_cache.items():
            if author is not None and author != "":
                item_y = y + displayed_authors * item_height
                if item_y + item_height > y + dynamic_legend_height:
                    break

                # Zeichnen des Farbrechtecks
                pygame.draw.rect(self.screen, color, (x + 5, item_y + 5, 10, 10))

                # Berechne die Position des Textes, um ihn mittig zum Farbrechteck zu positionieren
                author_text = self.font.render(author, True, (255, 255, 255))
                text_height = author_text.get_height()
                text_y = item_y + 5 + (10 - text_height) // 2  # Zentriert den Text vertikal im Farbrechteck

                # Zeichnen des Autor-Namens
                self.screen.blit(author_text, (x + 20, text_y))

                displayed_authors += 1
                # Speichern der Koordinaten und des Autors
                self.legend_entries[(x, item_y, x + self.legend_width, item_y + item_height)] = author
        self.legend_surface_rect.height = dynamic_legend_height


    def update_author_color_cache(self, author, color):
        self.author_color_cache[author] = color

