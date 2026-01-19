class ApplicationSettings:
    def __init__(self):
        self.debug_mode: bool = False
        self.allow_calculation_of_similarity: bool = False
        self.create_similarity_toggle: bool = False
        self.create_connections_toggle: bool = False
        self.create_add_button: bool = False


        # AutoLayout Settings
        self.base_convergence_steps = 100 # base value 100
        self.base_max_velocity = 100 #base value 10 / Quick Application 100
        self.base_repulsion_force_modification = 200.0 # base value 200
        self.base_attraction_force_modification = 50.0 # base value 50
        self.minimum_convergence_factor = 0.001 # base value 0.001

        # Graph Visualization
        self.start_x = 5000300 #Start X Camera Position
        self.start_y = 5000000 #Start Y Camera Position
        self.zoom = 50.0 # Start Zoom Factor
        self.team_legend_activated = True
        self.base_node_diameter = 5
        self.base_node_highlight_diameter = 10
        self.selected_node_special_highlight_diameter = 24
