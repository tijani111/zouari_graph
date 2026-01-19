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
import pygame.gfxdraw


class Toggle:
    def __init__(self, x, y, width, height, color_on, color_off, radius=20):
        self.rect = pygame.Rect(x, y, width, height)
        self.circle_radius = radius
        self.is_on = False
        self.color_off = color_off
        self.color_on = color_on
        self.color_background = (100, 100, 100)

    def draw_rounded_rect(self, surface, rect, color, radius=0.4):
        """
        Drawing a rounded rectangle
        """
        rect = pygame.Rect(rect)
        color = pygame.Color(*color)
        alpha = color.a
        color.a = 0
        pos = rect.topleft
        rect.topleft = 0, 0
        rectangle = pygame.Surface(rect.size, pygame.SRCALPHA)

        circle = pygame.Surface([min(rect.size) * 3] * 2, pygame.SRCALPHA)
        pygame.draw.ellipse(circle, (0, 0, 0), circle.get_rect(), 0)
        circle = pygame.transform.smoothscale(circle, [int(min(rect.size) * radius)] * 2)

        radius = rectangle.blit(circle, (0, 0))
        radius.bottomright = rect.bottomright
        rectangle.blit(circle, radius)
        radius.topright = rect.topright
        rectangle.blit(circle, radius)
        radius.bottomleft = rect.bottomleft
        rectangle.blit(circle, radius)

        rectangle.fill((0, 0, 0), rect.inflate(-radius.w, 0))
        rectangle.fill((0, 0, 0), rect.inflate(0, -radius.h))

        rectangle.fill(color, special_flags=pygame.BLEND_RGBA_MAX)
        rectangle.fill((255, 255, 255, alpha), special_flags=pygame.BLEND_RGBA_MIN)

        return surface.blit(rectangle, pos)

    def draw(self, surface):
        # Abgerundetes Rechteck mit Antialiasing
        self.draw_rounded_rect(surface, self.rect, self.color_background, radius=0.5)

        # Position des Kreises basierend auf dem Zustand ändern
        circle_x = self.rect.right - self.circle_radius if self.is_on else self.rect.x + self.circle_radius
        circle_color = self.color_on if self.is_on else self.color_off

        # Kreis mit Antialiasing
        pygame.gfxdraw.filled_circle(surface, circle_x, self.rect.centery, self.circle_radius, circle_color)
        pygame.gfxdraw.aacircle(surface, circle_x, self.rect.centery, self.circle_radius, circle_color)

    def toggle(self):
        self.is_on = not self.is_on

    def set_state(self, state):
        self.is_on = state

    def get_state(self):
        return self.is_on
