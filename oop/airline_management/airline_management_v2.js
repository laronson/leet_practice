/**
 * airline management system
 * Users: Consumers (aka flyers) and airline administration
 *
 * - manage flights for customers
 * - manage schedules for planes and airline staff
 *
 * System Requirements
 * - Book/edit/cancel flights
 *  - Searching for flights
 *      - name, place, time,
 *  - paying for bookings and changes
 *  - Alerts for changes in my flights
 *  - Provide me with a ticket
 * - Manage planes in fleet
 *  - Add/Remove planes from fleet
 *  - Schedule flights for each plane in fleet
 *  - Track location of planes
 * - Manage personal and tasks needed for flights
 *  - Assigning Pilots to schedule
 *  - Assigning gate attendent to flight
 *
 * Entities:
 *  - Customers
 *      attr: (flyerIds, names, addresses, payment_methods)
 *      fn: findFlight() -> system to get flight
 *      fn:
 *  - Airline
 *      - Personal
 *          - Admin
 *          - Gate Attendants
 *          - Pilots
 *      - Planes
 *      - System
 *          - Schedules (planes <> pilots)
 */

//*******Constants ************/
const PersonType = {
  CUSTOMER: "CUSTOMER",
  ATTENDANT: "ATTENDANT",
  PILOT: "PILOT",
  ADMIN: "ADMIN",
};

const PAYMENT_STATUS = {
  PAID: true,
  NOT_PAID: false,
};

//********** PERSON ********/

class Person {
  name;
  address;
  type;
  ctor(name, address, type) {
    this.name = name;
    this.address = address;
    this.type = type;
  }
}

class Customer extends Person {
  flyerId;
  paymentMethods; // {cards:[primary,secondary], cash:number} -> Wallet
  tickets; // {flightId:Ticket}
  ctor(name, address, flyerId, paymentMethods) {
    super(name, address, PersonType.CUSTOMER);
  }

  //Call system to find flight with given filters
  findFlight() {}

  //call system with flightId to book flight
  bookFlight(flightId) {} //Ticket or False for if flight was booked

  //calls system with new flight request and
  requestFlightEdit(flightId, time, place) {} //Ticket or False for if new flight was booked

  //Take amount needed to pay and checks if user can pay with specified payment type(s)
  pay(amount, requiredPaymentType) {}

  //Accept notification from system regarding flight changes
  acceptNotification(notification) {}
}

class FlightQuery {
  ctor() {
    this.flightId = null;
    this.sourceLocation = null;
    this.destinationLocation = null;
    this.departure = null;
  }

  get flightId() {
    return flightId;
  }
  set flightId(id) {
    return flightId;
  }
  get sourceLocation() {
    return sourceLocation;
  }
  set sourceLocation(id) {
    return sourceLocation;
  }
  get destinationLocation() {
    return destinationLocation;
  }
  set destinationLocation(id) {
    return destinationLocation;
  }
  get departure() {
    return departure;
  }
  set departure(id) {
    return departure;
  }
}

class FlightQueryBuilder {
  ctor() {
    this.flightId = null;
    this.sourceLocation = null;
    this.destinationLocation = null;
    this.departure = null;
  }

  addFlightId(flightId) {
    this.flightId = flightId;
  }
  addSourceLocation(sourceLocation) {
    this.sourceLocation = sourceLocation;
  }
  addDestinationLocation(destinationLocation) {
    this.destinationLocation = destinationLocation;
  }
  addDeparture(departure) {
    this.departure = departure;
  }

  build() {
    query = new FlightQueryBuilder();
  }
}

class Admin {
  adminId;
  employeeId;
  ctor(name, address, adminId, employeeId) {
    super(name, address, PersonType.ADMIN);
    this.adminId = adminId;
    this.employeeId = employeeId;
  }
}

class SystemSingleton {
  system;
  ctor(airline) {
    if (this.system) {
      console.log("ALREADY INSTANTIATED");
      return;
    }
    this.system = this;
    this.airline = airline;
  }

  findFlights(filters) {
    availableFlights = this.airline.getSchedules(filters);
    return this._filterFlights(availableFlights, filters);
  }

  // Filter flights based on filters
  _filterFlights(flights, filters) {}
}

class Airline {
  ctor() {}

  //Return all active schedules for the airline
  getSchedules() {}
}

class Ticket {
  flightId;
  paidStatus;
}
