// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract MarksManagmtSys {
	struct Student {
		int ID;
		string fName;
		string lName;
		int marks;
	}

	address owner;
	int public stdCount = 0;
	mapping(int => Student) public stdRecords;

	modifier onlyOwner() {
		require(msg.sender == owner, "Only owner can call this function.");
		_;
	}

	constructor() {
		owner = msg.sender;
	}

	function addNewRecords(int _ID, string memory _fName, string memory _lName, int _marks) public onlyOwner {
		stdCount++;
		stdRecords[stdCount] = Student(_ID, _fName, _lName, _marks);
	}

	function bonusMarks(int _bonus) public onlyOwner {
		for (int i = 1; i <= stdCount; i++) {
			stdRecords[i].marks += _bonus;
		}
	}
}