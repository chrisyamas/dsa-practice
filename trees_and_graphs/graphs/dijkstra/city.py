from dijkstra_cheapest_flight import dijkstra_cheapest_flight_path

class City:

    def __init__(self, name):
        self.name = name
        self.routes = {}
    
    def add_route(self, city, price):
        self.routes[city] = price


if __name__ == '__main__':
    atlanta = City("Atlanta")
    boston = City("Boston")
    chicago = City("Chicago")
    denver = City("Denver")
    el_paso = City("El Paso")

    atlanta.add_route(boston, 100)
    atlanta.add_route(denver, 160)
    boston.add_route(chicago, 120)
    boston.add_route(denver, 180)
    chicago.add_route(el_paso, 80)
    denver.add_route(chicago, 40)
    denver.add_route(el_paso, 140)

    path = dijkstra_cheapest_flight_path(atlanta, el_paso)
    print(path)
