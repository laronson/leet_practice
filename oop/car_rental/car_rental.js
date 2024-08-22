/**
 * Car Rental System
 * The customers of the system are Consumers and Admins
 * 
 * Consumers can rent a car
 * 	- Search for a car (price, car type, color, #of seats, pickup location, dropoff location)
 * 	- Request a rental
 * 	- Pay for a rental
 * 
 * System
 * 	-Keep track of bookings
 *	 	- What car is used on the booking
 * 		- Has it been paid for (sttus)
 * 		- What customer
 * 		- Duration of rental
 * 	- Keep track of car inventory
 * 	- 
 * 
 * Admin
 * 	- Add cars and remove cars to our fleet
 * 	- Move cars around to different locations
 * 	- Add or remove locations 
 * 
 * 
 * Entities
 * 	Users:
 * 		Consumer
 * 		System
 * 		Admin
 * 	
 * 	Cars
 * 		- # of seats
 * 		- color
 * 		-car type
 * 	Booking
 * 	Store
 * 	Inventory
 * 	CarBuilderClass**
 * 	PricingSystem - take into account the attributes of a car generate the price off of that
 * 		
 * 	
 */
 

const PersonType = {
	ADMIN: 'admin',
	CUSTOMER: 'customer'
}

class Car {
	color
	make
	model
	plateNumber
	ctor(){}
}


class Store {
	capacity
	carsInFleet
	carsAvailable

	ctor(){}
}

class System{
	bookCar(){}
}


class Customer {
	reserveCar(system) {

	}
}




