def traffic_light(light_color):
    light_color = light_color.lower()

    if light_color == 'red':
        return 'Stop'
    elif light_color == 'yellow':
        return 'Yield'
    elif light_color == 'green':
        return 'Go'

print(traffic_light('Yellow'))

