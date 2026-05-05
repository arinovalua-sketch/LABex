# Lab 4 - Sequence Diagrams

## Overview

This lab presents multiple sequence diagrams that demonstrate interactions between system components in different real-world systems.

The diagrams illustrate how users and system components communicate step-by-step to complete specific processes.

---

## 1. ATM System

### Description

The ATM sequence diagram shows how a customer interacts with an ATM machine to perform a transaction.

### Participants:

* Customer
* ATM Machine
* Bank Server
* Account Database

### Flow:

1. Customer inserts card
2. System requests and verifies PIN
3. Customer selects transaction (e.g., withdraw cash)
4. ATM communicates with the bank server
5. Server checks account balance
6. Transaction is approved or rejected
7. ATM dispenses cash and prints receipt

📄 Diagram:
[Open ATM Diagram (PDF)](ATM.pdf)

---

## 2. Medical Clinic System

### Description

This diagram represents the workflow of a patient interacting with a medical clinic system.

### Participants:

* Patient
* Reception
* Doctor
* System

### Flow:

1. Patient arrives at the clinic
2. Reception registers the patient
3. Patient waits for appointment
4. Doctor examines the patient
5. System records diagnosis
6. Prescription or treatment is provided

📄 Diagram:
[Medical clinic.pdf](https://github.com/user-attachments/files/27382205/Medical.clinic.pdf)
 

---

## 3. Car Insurance System

### Description

This diagram shows the process of handling an insurance claim.

### Participants:

* Customer
* Insurance System
* Claims Department
* Payment System

### Flow:

1. Customer submits a claim
2. System validates claim details
3. Claim is investigated
4. Decision is made (approve/reject)
5. Payment is processed if approved
6. Customer receives compensation

📄 Diagram:
[Car insurance.pdf](https://github.com/user-attachments/files/27382222/Car.insurance.pdf)
 
---

## Notes

* Each diagram represents a real-world scenario
* The diagrams follow sequential interaction logic
* They demonstrate communication between users and system components

---

## Author

Software Engineering Lab – Sequence Diagrams
