# Design Amazon Locker

## Problem Statement
Design a secure, scalable, and efficient system for an Amazon Locker service. Customers receive a code to pick up their packages from a physical locker located at various hubs.

## Requirements

### Functional
- **Locker Allocation**: System should find and assign a locker of appropriate size to a package.
- **Package Drop-off**: Delivery person drops off the package and a notification is sent to the customer.
- **Package Pickup**: Customer enters a code at the locker hub to open the assigned locker.
- **Locker Management**: Lockers should be marked as available once the package is picked up.
- **Expiration**: If a package is not picked up within 3 days, it should be marked for return.

### Non-Functional
- **Availability**: The system must be highly available for both delivery and pickup.
- **Scalability**: Support millions of lockers globally.
- **Security**: Locker codes must be secure and unique.
- **Low Latency**: Assignment and pickup operations should be fast.

## Key Components
- **Locker Service**: Orchestrates the allocation and tracking of lockers.
- **Hub Service**: Manages the state and location of physical hubs.
- **Notification Service**: Sends SMS/Email codes to customers.
- **Locker Hub Controller**: Local software at the hub that interacts with the physical hardware.

## Data Model
- **Hub**: `hub_id`, `location`, `locker_list`
- **Locker**: `locker_id`, `hub_id`, `size` (S, M, L, XL), `status` (Available, Occupied, OutOfOrder)
- **Package**: `package_id`, `size`, `customer_id`
- **Booking**: `booking_id`, `locker_id`, `package_id`, `otp`, `booking_time`, `expiry_time`
