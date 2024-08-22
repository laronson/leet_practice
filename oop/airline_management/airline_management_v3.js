/**
 * Airline management system
 *
 * Who are our users? Customers and Admins
 * - Customers
 * - System Users
 *  - Admin
 *  - Gate Worker
 *
 *
 * System Requirements
 * - Customer can Book/edit/delete flights
 *  - search for flights (source/Destination, time, price)
 *  - book a flight
 *  - pay for flight
 * - Admin can manage flight and plane information
 *  - Add and remove planes from our fleet
 *  - Create schedules for planes
 *  - Assign Pilots to planes
 *  - cancel flights
 * - Gate Worker
 *  - Check people into flights
 *
 * System Actors -> system
 * - Customer
 * - Admin
 * - Gate worker
 *
 * System Entities:
 * - Flight
 *  - Plane
 *  - Pilot **
 *  - manifest -> list of customers on plane
 *  - source/destination
 *  - takeoff/landing times
 *  - status
 *
 * - Plane
 *  - planeId
 *  - year/make/model
 *  - seatCapacity
 *  - fn: takeoff() // dont take off if no pilots or manifest length is > capacity
 *
 * - Pilot
 *  - yrsOfExperience
 *  - planesCapableFlying
 *
 * - Schedule
 *  - flightsByDay {[UnixDateTimeStamp]: [Flights]}
 *  - fn:searchFlights()
 *
 * - System:
 *  - FlightSchedule
 *  - PlaneList
 *  - PilotList
 */

class Plane {
  planeId;
  model;
  seatCapacity;
  pilotCountRequirement;
  PlaneSchedule;
  ctor() {}

  //Plane takes off if pilots have ability to fly plane and customerCount < seatCapacity
  takeoff(pilots, customerCount) {}
}

class Pilot {
  pilotId;
  modelsTrainedToFly;
  yearsOfExperience;
  PilotSchedule;
  //First or second captain
  ctor() {}
}

const FlightStatuses = {
  ON_ROUTE: 1,
  DELAYED: 2,
  CANCELED: 3,
  NOT_CONFIRMED: 4,
};

class Flight {
  plane;
  pilots;
  manifest;
  source;
  destination;
  takeoffTime;
  landingTimes;
  status;
  ctor() {
    this.plane = null;
    this.pilots = [];
    this.manifest = [];
    this.source = "";
    this.destination = "";
    this.takeoffTime = null;
    this.landingTimes = null;
    this.status = FlightStatuses.NOT_CONFIRMED;
  }

  //Call would come from system that was interating with end user
  addCustomerToFlight() {}

  //Tell plane to takeoff
  takeOff() {
    if (
      this.manifest.length <= this.plane.seatCapacity &&
      this.pilots.length >= this.plane.pilotCountRequirement
    ) {
      this.plane.takeOff(this.pilots, this.manifest.length);
    }
  }

  //
  cancelFlight() {
    this.status = "CANCELED";
  }
}

class Schedule {
  flights; // [Flights]
}
class PlaneSchedule extends Schedule {
  hourRestrictions;
  gasRestrictions;
}
class PilotSchedule extends Schedule {
  unionRestrictions;
}

class FlightBuilder {
  Pilots;
  Planes;
  ctor() {
    this.plane = null;
    this.pilots = [];
    this.manifest = [];
    this.source = "";
    this.destination = "";
    this.takeoffTime = null;
    this.landingTimes = null;
    this.status = FlightStatuses.NOT_CONFIRMED;
  }

  //Check to see if we can add plane using schedule and restrictions before adding.  Throw error if not
  addPlane() {}

  //...//
}

class System {
  pilots;
  planes;
  flights;
  ctor() {}

  createFlight() {
    fb = new FlightBuilder();
    //Try to add all things to flight
    newFlight = fb.build();
  }

  cancelFlight(flightId) {
    flightToCancel = this.flights.find(
      (flight) => flight.getFlightId() === flightId
    );
    //flight
  }
}
