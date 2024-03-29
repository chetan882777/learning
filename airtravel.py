"""Model for aircraft flights"""

# from pprint import pprint as pp

class Flight:
    """A Flight with a particular passenger aircraft"""

    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows,seats=self._aircraft.seating_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def _parse_seat(self,seat):
        """Parse a seat designator into a valid row and letter"""
        row_numbers,seat_letters=self._aircraft.seating_plan()

        letter=seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text=seat[:-1]
        try:
            row=int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in row_numbers:
            raise ValueError("Invalid row number {}".format(row))

        return row,letter

    def allocate_seat(self,seat,passenger):
        """Allocate a seat to passenger"""

        # rows,seat_letters=self._aircraft.seating_plan()

        row,letter=self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passanger(self,from_seat,to_seat):
        """Relocate a passenger to a different seat."""

        from_row,from_letter=self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in seat {}".format(from_seat))

        to_row,to_letter=self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied ".format(to_seat))

        self._seating[to_row][to_letter]= self._seating[from_row][from_letter]
        self._seating[from_row][from_letter]=None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def num_occupied_seats(self):
        return sum(sum(1 for s in row.values() if s is not None)
                    for row in self._seating
                    if row is not None)

    def make_boarding_cards(self,card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger,seat,self.number(),self.aircraft_model())

    def _passenger_seats(self):
        row_numbers,seat_letters=self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger,"{}{}".format(row,letter))

class Aircraft:

    def __init__(self,registration,model ,num_rows,num_seats_per_row):
        self._registration=registration
        self._model=model
        self._num_rows=num_rows
        self._num_seats_per_row=num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1,self._num_rows+1),
                "ABCDEFGHJK"[:self._num_seats_per_row])

def make_flight():
    f = Flight("SN309", Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6))
    f.allocate_seat('12A','Darshan')
    f.allocate_seat('15F','Aakash')
    f.allocate_seat('15E','Bhupen')
    f.allocate_seat('1C','Vandan')
    f.allocate_seat('1D','Chetan')
    return f

def console_card_printer(passenger,seat,flight_number,aircraft):
    output = "| Name : {0}"\
            "   Flight : {1}"\
            "   Seat : {2}"\
            "   Aircraft : {3}"\
            "|".format(passenger,flight_number,seat,aircraft)
    banner = '+' + '-' * (len(output)-2) + '+'
    border = '|' + ' ' * (len(output)-2) + '|'
    lines = [banner,border,output,border,banner]
    card = '\n'.join(lines)
    print(card)
    print()

def strt():
    f=make_flight()
    f.make_boarding_cards(console_card_printer)

# if __name__== '__main__':
#
#     # f=Flight("SN309")
#     # print("Flight Number - ",f.number())
#     # print("Airline Number - ",f.airline())
#
#     a= Aircraft("G-EUPT","Airbus A319",22,num_seats_per_row=6)
#     print(a.registration())
#     print(a.model())
#     print(a.seating_plan())

    # f = Flight("SN309", Aircraft("G-EUPT", "Airbus A319", 22, num_seats_per_row=6))
    # print(f.aircraft_model())
    # print(f.aircraft_registration())

    # a=Aircraft('3349AA','AAA39',20,10)
    # print(a.registration())
    # print(a.model())