def show_day(day: int, total_ndays: int) -> None:
    if day > total_ndays:
        print("Harvest time!")
        return
    print(f"Day {day}")
    show_day(day + 1, total_ndays)


def ft_count_harvest_recursive() -> None:
    total_nd = int(input("Days until harvest: "))
    show_day(1, total_nd)
