class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']
        velocity = observations['velocity']

        left = lidar[0]
        slight_left = lidar[1]
        center = lidar[2]
        slight_right = lidar[3]
        right = lidar[4]

        if center < 1.0 or slight_left < 0.8 or slight_right < 0.8:
            return ('straight', 'brake')

        if left < 1.0:
            return ('right', 'coast')

        if right < 1.0:
            return ('left', 'coast')

        if center > 2.0 and velocity < 0.8:
            return ('straight', 'accelerate')

        return ('straight', 'coast')
