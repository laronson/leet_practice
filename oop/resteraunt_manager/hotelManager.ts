/**
 * 
 * Hotel Management System
 * 
 * Users: People who work at hotel
 * 	- hotel manager
 * 	- Receptionist
 *  - HouseKeeper
 * 	- **Customers to book hotel stay
 * 
 * 
 * Functional Requirements:
 * 	- Manager should be able to operational stats
 * 		- rooms avaialble/booked
 * 		- total income
 * 	- Manager should be be able to schedule workers shifts
 * 	- Manager should be able to add/remove locations
 * 	- Receptionist should be able to book rooms
 * 		- search rooms based off type and availability
 * 	- Receptionist should be able to check in guests
 * 	- Receptionist should be able to call houseKeeper to room
 * 	- HouseKeeper should be able to clean rooms
 * 
 * - Give operational stats
 * - Book rooms
 * - search rooms 
 * - clean rooms
 * 
 * Entities:
 * 	- Hotel
 * 		- Rooms
 * 			- isInuse
 * 			- isClean
 * 			- type: normal | suite
 * 			- SleeperSurface
 * 				- type: bed | cot | couch
 * 				- capacity
 * 				- size
 * 			- Booking
 * 				- roomId
 * 				- customerId
 * 				- startTime
 * 				- endTime
 * 	- BookingService
 * 		- making/canceling bookings
 * 		- tracking existing booking
 * 	- HouseKeepingService
 * 		- dispatching HouseKeepers
 *  -MgmtService 
 * 		- worker schedules 
 * 		- operational stats
 */

type RoomType = "suite" | "normal"
type SleeperType = "bed" | "cot" | "couch"

class Booking {
	roomId: number
	customerId: numer
	startTime: Date
	endTime: Date

	edit(statTime:Date|null, endTime:Date|null):null{}
}

class Room {
	isUse:boolean
	isClean: boolean
	type: RoomType
	sleeperSurfaces: SleeperSurface[]

	ctor({type}:{type:RoomType}){
		this.type = type
	}

}

class Suite extends Room {
	ctor(){
		super({type:"suite"})
	}
}


class SleeperSurface {
	capacity: number 
	type: SleeperType
	size: number
}

class Hotel {
	rooms: Room[]


}

class DataService {
	hotels: Hotels[]
	workerSchedule: []

	crudHotel(){}
	crudWorkerSchedule(){}
}


class System {
	ctor(){
		dataService = new DataService()
		this.hotels = []
		this.bookingService = new BookingService(dataService)
		this.managementService = new ManagementService(dataService)
	}

	findRooms() {
		return this.bookingService.searchForAvailableRooms(this.hotels)
	}

	bookRoom(hotelId,roomId) {
		try {
			this.bookingService.bookingRoom(hotels,hotelId, roomId)
		} catch {
			// what do we do when we fail?
		}
	}

	isHotelCovered(hotelId):boolean {
		return this.managementService.isHotelCovered(hotelId, this.workerSchedules)
	}
}

class BookingService() {
	ctor(dataService){
		this.dataService = dataService
	}

	searchForAvailableRooms({hotelId, numberOfGuests, roomType}):Rooms[] {
		hotels = this.dataService.getHotels()
		//searching hotel for avaialbe rooms based on query 
	}

	bookRoom(hotels, hotelId, roomId) {
		//validation that booking is ok
		// create booking
		//return booking
	}
}

class HotelService {
	hotels:Hotels[]

	ctor(hotels){
		this.hotels = hotels
	}

	addLocation() {
		hotelsList.append()
	}
	removeLocation() {}
}

class ManagementService {
	isHotelCovered(workderSchedules, hotelId) {
		//Search workerSchedulkes for schedules at hotel
		// perform interval check to make sure that all ranges for hotel are cover
		//return boolean
	}
}

type THotelRoomQuery = {hotelId:number, numberOfGuests:number, roomType:RoomType|null, startDate, endDate}







