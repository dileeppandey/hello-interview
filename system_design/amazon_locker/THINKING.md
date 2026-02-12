# Amazon Locker — First-Principles Thinking Guide

## 1. Understanding the Problem
**Goal**: Build a system that manages physical lockers for package delivery and pickup.

**Core Workflow**:
1. Package arrives at Hub.
2. System allocates a Locker based on Package size.
3. Notification sent to User with OTP.
4. User picks up package using OTP.
5. Locker is freed.

## 2. Key Challenges
- **Concurrency**: Multiple delivery people might try to book lockers at the same hub simultaneously.
- **Hardware Integration**: The cloud system must talk to offline or periodically online physical hubs.
- **Size Matching**: Optimally using locker space (e.g., don't put a small package in an XL locker if avoidable).

## 3. High-Level Design Decisions
- **Microservices**: Separate `LockerService` (state) from `NotificationService`.
- **Consistency**: Use a RDBMS (like PostgreSQL) for Locker state to ensure ACID properties during allocation (no double-booking).
- **Security**: Use short-lived, cryptographically secure OTPs.

## 4. Scaling & Optimization
- **Geographical Partitioning**: Locations (Hubs) should be indexed spatially (e.g., Geo-hashes or S2 cells).
- **Caching**: Hub availability can be cached, but the final booking must hit the DB.
- **Offline Mode**: Hub controllers should have enough local state to allow pickups even if the cloud connection is briefly interrupted (pre-downloaded OTP hashes).
