# Rule-based agent for Mountain Car
class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']
        velocity = observations['velocity']
        left, s_left, center, s_right, right = lidar
