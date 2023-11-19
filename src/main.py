from weather import get_weather, get_longitude, get_latitude


def main():
    weather = get_weather("london")
    longidude = get_longitude("london")
    latitude = get_latitude("london")
    print(latitude, longidude, weather)


if __name__ == "__main__":
    main()
