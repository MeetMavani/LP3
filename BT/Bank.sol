//SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;  // use this or above this version of solidity

contract Bank {

    address public accountHolder;  // address datatype for public id of wallet
    uint256 balance = 0;

    constructor() {
        accountHolder = msg.sender; // msg is like this in other languages
    }


    function withdraw() public payable {
        require(balance > 0, "Insufficient Balance");
        require(msg.sender == accountHolder, "You are not the owner of this account");
        payable(msg.sender).transfer(balance);
        balance = 0;
    }

    function deposit() public payable{
        require(msg.value > 0, "Deposit amout should be grater than 0");
        require(msg.sender == accountHolder, "You are not the owner of this account");
        balance += msg.value;
    }

    function showBalance() public view returns(uint) {
        require(msg.sender == accountHolder, "You are not the owner of this account");
        return balance;
    }
}