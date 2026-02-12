# Design a Parking Lot

## Problem Statement
Design a parking lot that handles different types of vehicles (Car, Bike, Van) and different types of slots (Small, Compact, Large).

## Requirements

### Functional
- **vehicle Entry**: Assign a parking spot to an incoming vehicle if available.
- **Vehicle Exit**: Mark the spot as free and calculate the parking fee.
- **Capacity Tracking**: Show the number of available spots per type/floor.
- **Vehicle Support**: Large vehicles (Vans) might need multiple compact spots or a large spot.

## Key Components
- **Parking Lot**: Singleton that manages floors and entry/exit gates.
- **Parking Floor**: Contains spots and display boards.
- **Parking Spot**: Entity with state (Occupied/Free) and type.
- **Vehicle**: Base class for Car, Bike, Van.
- **Parking Ticket**: Issued at entry, used at exit to calculate fare.

## Data Model
- **Vehicle**: `license_plate`, `type`
- **ParkingSpot**: `spot_id`, `type`, `is_free`, `floor_id`
- **ParkingTicket**: `ticket_id`, `vehicle_id`, `entry_time`, `spot_id`
- **FareStrategy**: Interface for different hourly/flat rate calculations.

## High-Level Workflow
1. **Entry**:
    - Identify vehicle type.
    - Query `ParkingLot` for an available spot of compatible type.
    - Create `ParkingTicket`.
    - Mark spot as Occupied.
2. **Exit**:
    - Scan ticket.
    - Calculate fee based on duration.
    - Mark spot as Free.
    - Process payment.
