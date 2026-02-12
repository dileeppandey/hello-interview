# Designing a Parking Lot — First-Principles Thinking Guide

## 1. Understanding the Problem
**Goal**: Model the real-world logic of a parking lot. This is usually an Object-Oriented Design (OOD) question disguised as system design.

**Core Entities**: Vehicles, Spots, Floors, Tickets, Gates, Payment Systems.

## 2. Designing the Hierarchy
- **Encapsulation**: Vehicles should know their license plate, but the `ParkingLot` should know where vehicles are.
- **Polymorphism**: A `Van` is a `Vehicle`. It might consume one "Large" spot or three "Compact" spots depending on the business logic.
- **Composition**: A `ParkingLot` *has* `ParkingFloor`s. A `ParkingFloor` *has* `ParkingSpot`s.

## 3. Key Challenges & Patterns
- **Concurrency**: How do we handle multiple cars trying to enter the same spot? (Row-level locking in DB or synchronized methods in code).
- **Flexibility**: What if we add EV charging spots? Using an abstract `ParkingSpot` class with specializations makes this easier.
- **Fare Calculation**: Use the **Strategy Pattern** to handle different pricing (e.g., weekend rates vs. weekday rates).

## 4. Scaling (If Cloud-based)
- **Database Indexing**: Index available spots by type and floor.
- **Distributed Lock**: If the parking lot is massive with many entry points, use a distributed lock (like Redis Redlock) to ensure no two vehicles get the same spot.
