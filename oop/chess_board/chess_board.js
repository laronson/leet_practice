/**
 * Design a Chess board
 * 
 * A GRIDDED BOARD where a max of 2 PLAYERS move PIECES around the board where the stragegy of how a player moves their pieces coild ldead to a victory
 * 
 * Questions:
 * 	- Do the players of the game know the rules or do they need to be build in checks to our system?
 * 
 * Funtional Requirements:
 * - PLAYERS can move PIECES around the BOARD
 * 		- PIECES can "take" other PIECES from the oposing player which renders them unusable by the other PLAYER through the rest of the game
 * 		- PLAYERS can make a winning move and claim the win
 * - PIECES have restrictions on how they can move depending on what kind of piece they are (aka biship can ony love diagnoly )
 * 		- PIECES cannot move off the board
 * 		- PIECES should have an understanding of how they can move base off of what kind of piece they are
 * 	- BOARD can be used as the play field for each game of chess
 * 		- PLAYERS can set up their pieces for the start of a game
 * 		- PLAYERS can observe the current state of the BOARD
 * 		- PLAYERS can move pieces on the BOARD 
 * 
 * Entities:
 * 	PLAYERS
 * 		name 
 * 		chessRank
 * 		chessPlayerId
 * 		- have the ability to move pieces around the board
 * 		- can claim they win
 * PIECES:
 * 		- move
 * 		- give current location
 * 		- has a piece type (pawn rook ect.. )
 * BOARD 
 * 		- secondary rules?**
 * 		- hold state of pieces in the game
 * 		- show the state of the gmae
 * 
 */

const PIECE_TYPE = {
	ROOK:1,
	BISHUP:2,
	PAWN:3,
	KING:4,
	QUEEN:5,
	KIGHT:6
}

class Piece {
	type
	ctor(type) {
		this.type=type
	}
	move(){
		console.log(" THIS HAS NOT BEEN IMPLEMENTED")
	}
	currentLoc(){
		console.log(" THIS HAS NOT BEEN IMPLEMENTED")
	}
}

class Rook extends Piece {
	ctor() {
		this.super(PIECE_TYPE.ROOK)
	}
	move(x,y) {
		if x>0 && y>0 {
			throw Error("INVALID MOVE")
		}
	}
}
class King extends Pieces {}
class Queen extends Piece { }


class PieceSet {

}

