import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input = input(
            "Enter new coordinates as floats in format 'x,y,z': ")

        coords = user_input.split(',')
        if len(coords) != 3:
            print("Invalid syntax")
            continue

        parsed_coords = []
        invalid = False

        for coord in coords:
            clean_coord = coord.strip()
            try:
                parsed_coords.append(float(clean_coord))
            except ValueError as e:
                err_msg, = e.args
                print(f"Error on parameter '{clean_coord}': {err_msg}")
                invalid = True
                break

        if not invalid:
            return (parsed_coords[0], parsed_coords[1], parsed_coords[2])


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    coord1 = get_player_pos()

    print(f"Got a first tuple: {coord1}")

    x1, y1, z1 = coord1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    dist_center = math.sqrt((x1 - 0)**2 + (y1 - 0)**2 + (z1 - 0)**2)
    print(f"Distance to center: {round(dist_center, 4)}")
    print()
    print("Get a second set of coordinates")
    coord2 = get_player_pos()

    x2, y2, z2 = coord2

    dist_2pts = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets of coordinates: {round(dist_2pts, 4)}")


if __name__ == "__main__":
    main()
