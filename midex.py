class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls._hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self._seats = {}  
        self._show_list = []  
        self._rows = rows  
        self._cols = cols  
        self._hall_no = hall_no  
        Star_Cinema.entry_hall(self)  

    def __entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time) 
        self._show_list.append(show_info)  
        seat_arrangement = [['0' for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[id] = seat_arrangement

    def __book_seats(self, show_id, seats_to_book):
        if show_id not in self._seats:
            raise ValueError("Invalid show ID")

        for seat in seats_to_book:
            row, col = seat
            if not (0 <= row < self._rows) or not (0 <= col < self._cols):
                raise ValueError("Invalid seat")

            if self._seats[show_id][row][col] != '0':
                raise ValueError("Seat already booked")

            self._seats[show_id][row][col] = 'X'  

    def __view_available_seats(self, show_id):
        if show_id not in self._seats:
            raise ValueError("Invalid show ID")

        available_seats = []
        for row in range(self._rows):
            for col in range(self._cols):
                if self._seats[show_id][row][col] == '0':
                    available_seats.append((row, col))

        return available_seats

    def view_show_list(self):
        return self._show_list

    def view_available_seats(self, show_id):
        return self.__view_available_seats(show_id)

    def book_seats(self, show_id, seats_to_book):
        self.__book_seats(show_id, seats_to_book)

    def entry_show(self, id, movie_name, time):
        self.__entry_show(id, movie_name, time)
        

hall1 = Hall(7, 7, 2)

show_id = input("Enter show ID: ")
movie_name = input("Enter movie name: ")
show_time = input("Enter show time: ")
hall1.entry_show(show_id, movie_name, show_time)

print("\nShowing All Shows:")
print(hall1.view_show_list())

try:
    num_seats_to_book = int(input("\nNumber of seats to book: "))
    seats_to_book = []
    for _ in range(num_seats_to_book):
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        seats_to_book.append((row, col))
    hall1.book_seats(show_id, seats_to_book)
except ValueError as e:
    print(e)

print("\nAvailable Seats:")
print(hall1.view_available_seats(show_id))

def counter_replica_system():
    print("Welcome to Star Cinema Counter Replica System")
    print("=============================================")

    while True:
        print("\nMenu:")
        print("1. View all shows running")
        print("2. View available seats in a show")
        print("3. Book tickets in a show")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("\nShows Running:")
            for hall in Star_Cinema._hall_list:
                print(f"Hall No: {hall._hall_no}")
                for show in hall.view_show_list():
                    print(f"ID: {show[0]} ||| Movie: {show[1]} ||| Time: {show[2]}")
            print()

        elif choice == '2':
            show_id = input("Enter the ID of the show: ")
            for hall in Star_Cinema._hall_list:
                if show_id in hall._seats:
                    try:
                        available_seats = hall.view_available_seats(show_id)
                        print(f"Available seats for Show ID: {show_id}")
                        print(available_seats)
                    except ValueError as e:
                        print(e)
                    break
            else:
                print("Invalid show ID!")

        elif choice == '3':
            show_id = input("Enter the ID of the show: ")
            for hall in Star_Cinema._hall_list:
                if show_id in hall._seats:
                    try:
                        available_seats = hall.view_available_seats(show_id)
                        print(f"Available seats for Show ID: {show_id}")
                        print(available_seats)
                        if available_seats:
                            row_col = input("Enter row and column of seat (comma-separated): ")
                            row, col = map(int, row_col.split(','))
                            if (row, col) in available_seats:
                                try:
                                    hall.book_seats(show_id, [(row, col)])
                                    print("Seat booked successfully!")
                                except ValueError as e:
                                    print(e)
                            else:
                                print("Invalid seat!")
                    except ValueError as e:
                        print(e)
                    break
            else:
                print("Invalid show ID!")

        elif choice == '4':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice! Try again")

counter_replica_system()