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

    def aircraft_registration(self):
        return self._aircraft.registration()

    def allocate_seat(self,seat,passenger):
        """Allocate a seat to passenger"""

        rows,seat_letters=self._aircraft.seating_plan()

        letter = seat[-1]

        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text=seat[:-1]
        try:
            row=int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number".format(row))

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

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

if __name__== '__main__':
#
#     # f=Flight("SN309")
#     # print("Flight Number - ",f.number())
#     # print("Airline Number - ",f.airline())
#
#     a= Aircraft("G-EUPT","Airbus A319",22,num_seats_per_row=6)
#     print(a.registration())
#     print(a.model())
#     print(a.seating_plan())

    f = Flight("SN309", Aircraft("G-EUPT", "Airbus A319", 22, num_seats_per_row=6))
    print(f.aircraft_model())
    print(f.aircraft_registration())

    # a=Aircraft('3349AA','AAA39',20,10)
    # print(a.registration())
    # print(a.model())