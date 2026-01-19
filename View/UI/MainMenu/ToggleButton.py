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

from View.UI.MainMenu.Toggle import Toggle
from View.UI.UIThemes import UITheme


class ToggleButton:
    """
    The ToggleButton class represents a customizable toggle button in a UI,
    often used for settings or switchable options. It features a dynamic
    design with an integrated toggle and optional label text.

    Class Attributes:
        maximized (bool): Indicates whether the button is in a maximized state.
        FONT_SIZE (int): The font size for the button label.
        TOGGLE_WIDTH, TOGGLE_HEIGHT, TOGGLE_RADIUS (int): Constants defining the toggle's dimensions and appearance.
    """

    maximized = True
    FONT_SIZE = 25
    disabled = False  # New attribute to track disabled state

    # Toggle Consts
    TOGGLE_WIDTH = 30
    TOGGLE_HEIGHT = 20
    TOGGLE_RADIUS = 10

    def __init__(self, x, y, width, height, parent_surface, ui_theme: UITheme,
                 icon_x_offset=0, label='', font=None):
        """
        Initializes a MenuButton with specified properties and dimensions.

        :param: x: The x-coordinate of the button.
        :param: y: The y-coordinate of the button.
        :param: width: The width of the button.
        :param: height: The height of the button.
        :param: icon: The Pygame surface representing the button's icon.
        :param: icon_x_offset: The horizontal offset for the toggle within the button.
        :param: parent_surface: The parent Pygame surface to which this button belongs.
        :param: ui_theme: The UI Theme

        :param: label: The text label of the button.
        """
        self.font = font if font is not None else pygame.font.SysFont(None, 25)
        self.ui_theme = ui_theme
        self.disabled_color = ui_theme.DISABLED_LABEL_COLOR  # Assuming the theme has a color for disabled labels
        self.icon_size = height  # Die Größe des Icons ist gleich der Höhe des Buttons
        self.text = label
        self.clicked = False
        self.label_color = ui_theme.MAIN_MENU_LABEL_COLOR
        self.highlight_color = ui_theme.MAIN_MENU_HIGHLIGHT_COLOR
        self.background_color = ui_theme.MAIN_MENU_BACKGROUND_COLOR
        self.toggle_off_color = ui_theme.MAIN_MENU_BACKGROUND_COLOR
        self.icon_offset = icon_x_offset

        # Berechne die absolute Position des Buttons relativ zum parent_surface
        parent_x, parent_y = parent_surface.get_abs_offset()
        self.x = parent_x + x
        self.y = parent_y + y
        self.width = width
        self.height = height

        self.icon_area_width = width * 0.382
        self.label_area_width = self.width * 0.618

        # Erstelle einen Toggle
        toggle_x_pos = self.x + (self.icon_area_width // 2) - self.icon_size // 2 + self.icon_offset

        # Berechnen der y Position basierend auf der Font Size
        font = pygame.font.SysFont(None, self.FONT_SIZE)  # Sie könnten die Schriftart und -größe anpassen
        text_surface = font.render(self.text, True, self.label_color)
        text_mid_y = (self.height - text_surface.get_height()) // 2

        # Setze die y-Position des Toggle-Buttons auf die Mitte des Text-Labels
        toggle_y_pos = self.y + text_mid_y + (
                text_surface.get_height() - self.TOGGLE_HEIGHT) // 2
        self.toggle_button = Toggle(toggle_x_pos, toggle_y_pos, self.TOGGLE_WIDTH, self.TOGGLE_HEIGHT,
                                    self.highlight_color, self.toggle_off_color, self.TOGGLE_RADIUS)

        self.button_background_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self.button_background_surface.fill(self.background_color)

    def draw(self, screen, is_selected: bool = False):
        """
        Draws the button on the provided screen.

        :param: screen: The Pygame screen where the button will be drawn.
        :param: is_selected: Indicates whether the button is currently selected.
        """
        # Zeichne das Surface
        screen.blit(self.button_background_surface, (self.x, self.y))

        self.toggle_button.draw(screen)

        # Zeichne den Text, wenn vorhanden und maximiert
        if self.text != '' and self.maximized:
            self.button_background_surface.fill(self.background_color)
            font = self.font
            if is_selected:
                text_surface = font.render(self.text, True, self.highlight_color)
            else:
                text_surface = font.render(self.text, True, self.label_color)

            # Label position
            text_x = self.x + self.icon_area_width
            text_y = self.y + (self.height - text_surface.get_height()) // 2

            screen.blit(text_surface, (text_x, text_y))
        else:
            self.button_background_surface.fill((0, 0, 0, 0))

    def click(self, event):
        """
        Handles click events on the button, toggling its 'clicked' state and determining if the click event
        occurred within the button's area.

        :param: event: The Pygame event to be processed.
        :return: A boolean indicating whether the button was clicked.
        """
        if event.type != pygame.MOUSEBUTTONDOWN:
            return False  # Ignoriere Nicht-Mausklick-Events

            # Überprüfe, ob auf den restlichen Teil des MenuButtons geklickt wurde
        if self.x <= event.pos[0] <= self.x + self.width and self.y <= event.pos[1] <= self.y + self.height:
            self.toggle_button.toggle()
            self.clicked = not self.clicked
            return True

        return False

    def set_state(self, state: bool):
        """
        Sets the state of the toggle button.

        :param: state: The boolean state to set the toggle to (True for on, False for off).
        """
        self.toggle_button.set_state(state)

    def disable(self, state: bool):
        """
        Disables or enables the button based on the provided state.
        When disabled, the text label is grayed out, and the toggle state is set to False.

        :param state: Boolean value to set the disabled state (True for disabled, False for enabled).
        """
        self.disabled = state
        self.toggle_button.set_state(not state)
        if state:
            self.label_color = self.disabled_color
        else:
            self.label_color = self.ui_theme.MAIN_MENU_LABEL_COLOR

    def enable(self):
        """
        Enables the button, restoring the original text label color and toggle state.
        """
        self.disable(False)  # Reuse the disable method with False to enable the button
