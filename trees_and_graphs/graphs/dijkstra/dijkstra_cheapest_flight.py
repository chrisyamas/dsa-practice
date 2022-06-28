    # The lines in the below code definitely are not pep8
    # but I did not like the more Pythonic backslashes this time.
    # Code for this function transcribed from Ruby code version in:
    # A Common-Sense Guide to Data Structures and Algorithms
    # by Jay Wengrow, edited by Brian MacDonald

    # Dijkstra's Algorithm for finding cheapest flight path
    # from a starting city to a final destination:

    # 1. We visit the starting city, making it our "current city."
    # 2. We check the prices from the current city to each of its adjacent cities.
    # 3. If the price to an adjacent city from the starting city
    #   is cheaper than the price current in `cheapest_prices_table`
    #   (or the adjacent city isn't yet in the `cheapest prices table` at all):
    #   a. We update the `cheapest_prices_table` to reflect this cheaper price.
    #   b. We update the `cheapest_previous_stopover_city_table`,
    #       making the adjacent city the key and the current city the value.
    # 4. We then visit whichever unvisited city has the cheapest price from the
    #   starting city, making it the current city.
    # 5. We repeat the Steps 2 through 4 until we've visited every known city.

def dijkstra_cheapest_flight_path(starting_city, final_destination):
    cheapest_prices_table = {}
    cheapest_previous_stopover_city_table = {}
    # To keep our code simple, we'll use a basic array to keep track of
    # the known cities we haven't yet visited:
    unvisited_cities = []
    # We keep track of the cities we've visited using a hash table.
    # We could have used an array, but since we'll be doing, lookups,
    # a hash table is more efficient:
    visited_cities = {}
    # We add the starting city's name as the first key inside the
    # cheapest_prices_table. It has a value of 0, since it costs nothing
    # to get there:
    cheapest_prices_table[starting_city.name] = 0
    current_city = starting_city
    # This loop is the core of the algorithm. It runs as long as we can
    # visit a city that we haven't visited yet:
    while current_city:
        print(current_city.name)
        # We add the current_city's name to the visited_cities hash to record
        # that we've officially visited it. We also remove it from the list
        # of unvisited cities:
        visited_cities[current_city.name] = True
        for city in unvisited_cities:
            if city == current_city:
                unvisited_cities.remove(city)
        # We iterate over each of the current_city's adjacent cities:
        for adjacent_city, price in current_city.routes.items():
            # If we've discovered a new city,
            # we add it to the list of unvisited_cities:
            if adjacent_city not in unvisited_cities and adjacent_city.name not in visited_cities:
                unvisited_cities.append(adjacent_city)
            # We calculate the price of getting from the STARTING city to the
            # ADJACENT city using the CURRENT city as the second-to-last stop:
            price_through_current_city = cheapest_prices_table[current_city.name] + price
            # If the price from the STARTING city to the ADJACENT city is
            # the cheapest one we've found so far...
            if adjacent_city.name not in cheapest_prices_table or \
                price_through_current_city < cheapest_prices_table[adjacent_city.name]:
                # ... we update our two tables:
                cheapest_prices_table[adjacent_city.name] = price_through_current_city
                cheapest_previous_stopover_city_table[adjacent_city.name] = current_city.name
        # We visit our next unvisited city. We choose the one that is cheapest
        # to get to from the STARTING city:
        if len(unvisited_cities):
            minimum_price = cheapest_prices_table[unvisited_cities[0].name]
            current_city = unvisited_cities[0]
            for city in unvisited_cities:
                print("we got here!")
                if cheapest_prices_table[city.name] < minimum_price:
                    minimum_price = cheapest_prices_table[city.name]
                    current_city = city
        else:
            current_city = None
    # We have completed the core algorithm. At this point, the
    # cheapest_prices_table contains all the cheapest prices to get to each
    # city from the starting city. However, to calculate the precise path
    # to take from our starting city to our final destination,
    # we need to move on.
    # We'll build the shortest path using a simple array:
    shortest_path = []
    # To construct the shortest path, we need to work backwards from our
    # final destination. So, we begin with the final destination as our
    # current_city_name:
    current_city_name = final_destination.name
    # We loop until we reach our starting city:
    while current_city_name != starting_city.name:
        # We add each current_city_name we encounter to the shortest path array:
        shortest_path.append(current_city_name)
        # We use the cheapest_previous_stopover_city_table to follow each city
        # to its previous stopover city:
        current_city_name = cheapest_previous_stopover_city_table[current_city_name]
    # We cap things off by adding the starting city to the shortest path:
    shortest_path.append(starting_city.name)
    # We reverse the output so we can see the path from beginning to end:
    shortest_path.reverse()
    return shortest_path