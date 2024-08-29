/**
 * 
 * restaurant managenment system
 * 
 * User: people who work at the restaurant manager 
 * 	- manager
 * 	- hostest 
 *  - waiter
 * 
 * Functional requirements
 *  - Manager should be able to tracker Workers working at restaurant
 * 		- Who is working what position
 * 		- When are they working
 * 	- Manger should be able to see operational stats about each restaurant location
 * 		- how many people dined
 * 		- What did they order
 * 	- Waiter should be able to input what diners ordered
 * 		- What a waiter enteres shoukld be based off of a Menu
 * 		- Waiter should be able to accept payment
 *  - Hostest should be able to seat diners
 * 		- They should be able to seat people based off capcacity of location
 * 
 * - Trackers workers
 * - Operational stats
 * - Take orders
 * - Seat diners
 * 
 * 
 *  Entities:
 * 		- Restaurant
 * 			- Tables
 * 				-capacity 
 * 			- WorkerSchedule
 * 				- startTime
 * 				- endTime
 * 				- Worker
 *		- Menu
 * 			- name
 * 			- orderTime
 * 			- price
 * 		-System
 * 			fn: login(user)
 * 			- OrderSystem
 * 			- ManagerSystem
 * 			- HostesSystem
 * 
 * 
 */

const WORKER_TYPE ={
	MANAGER:1,
	HOSTESS: 2,
	WAITER:3
}

class Menu {
	menuId
	menuItems

	add()
	remove()
}

class MenuItem {
	name
	orderTime
	price
	section
}

class WorkerSchedule{
	starttime
	endTime
	worker
}


class Worker {
	name
	workerId
	type
	ctor(name,workerId,type){
		this.type
	}
}

class Manager extends Worker {
	ctor(){
		super(WORKER_TYPE.MANAGER)
	}

	hire(system) {
		service = system.login(this, oeration)

		serivice.hire()
	}
}

class Waiter extends Worker{
	takeOrder() {

	}
}
class Hostess extends Worker{}


class Table {
	tableId
	isInUse
	capacity

	seat(peopleCount) {
		if peopleCount > this.capacity {
			throw Error("CANT SIT HERE")
		}
	}
}

class Restaurant {
	tables
	menu
}


class System {
	managerService
	waiterService
	hostessService

	ctor(){
		this.managerService = new ManagerService()
		this.waiterService = new WaiterSystem()
	}

	login(user) {
		if (user.type === WORKER_TYPE.MANAGER){
			return this.managerService
		}
	}

	operationDistributer(operation) {

	}
}

class OrderSystem {
	takeOrder(){}
}






