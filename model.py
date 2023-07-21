class Model:
    '''Класс, хранящий информацию о состояние приложения'''

    traps_on_the_field = ["none", "none", "none", "rope", "rope", "rope", "detector", "detector", "detector"]

    cells_coords = {
        1: (60, 45),
        2: (157, 45),
        3: (254, 45),
        4: (60, 142),
        5: (157, 142),
        6: (254, 142),
        7: (60, 239),
        8: (157, 239),
        9: (254, 239)
    }

    cat_coords = []
    vampus_coords = []
    ghost_coords = []

    cat_trajectory = []
    vampus_trajectory = []
    ghost_trajectory = []

    triggered_traps = []

    update_field = True

    directions = ["up", "down", "left", "right"]