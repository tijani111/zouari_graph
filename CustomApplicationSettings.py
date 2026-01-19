from ApplicationSettings import ApplicationSettings


class CustomApplicationSettings(ApplicationSettings):
    def __init__(self):
        super().__init__()

        # AutoLayout Settings (mehr Abstand, ruhigeres Layout)
        self.base_convergence_steps = 140
        self.base_max_velocity = 60
        self.base_repulsion_force_modification = 360.0
        self.base_attraction_force_modification = 30.0
        self.minimum_convergence_factor = 0.001

        # Graph Visualization (bessere Lesbarkeit)
        self.start_x = 150
        self.start_y = 150
        self.zoom = 3.0
        self.base_node_diameter = 8
        self.base_node_highlight_diameter = 14
        self.selected_node_special_highlight_diameter = 30
        self.team_legend_activated = False
