# Lab 3 - Class Diagram

## System: Lost & Found Portal

### Classes:

- User: represents system users with authentication and actions  
- Admin: inherits from User and manages reports  
- Item: represents lost or found items  
- Report: connects users with items  
- Message: enables communication between users  

### Relationships:

- User creates Reports (1..*)  
- Report is linked to one Item (1..1)  
- User sends Messages (1..*)  
- Admin inherits from User  

### Description:

The system allows users to register, log in, report lost or found items, and communicate with other users. Admins manage reports and maintain system integrity.

### Diagram:
[UML_class_diagram.pdf](https://github.com/user-attachments/files/27382140/UML_class_diagram.pdf)
