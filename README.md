# HR Management System

## Overview
This project is a desktop HR management application built to help a company manage its employee database in one place. It provides a simple interface for storing employee details, updating records, tracking leave, reviewing budget information, and handling other day-to-day HR tasks.

The main goal of the system is to give businesses a practical internal tool where staff can add, edit, search, and maintain employee information while also supporting related administrative features such as leave tracking, budgeting, and feedback collection.

## Core Features
- Add new employees to the company database
- Edit existing employee records
- Delete employee records when needed
- Search for employees by name
- Track employee leave and available leave balances
- Manage employee budget and salary data
- Record extra employee-related costs
- View total, used, and remaining budget values
- Support employee login and password changes
- Collect and review employee feedback

## Project Goal
The purpose of this project is to serve as a lightweight HR system for companies that need a straightforward way to maintain employee data. Instead of handling employee details manually across multiple files or tools, the application centralizes information in a database-driven desktop app.

This makes it easier to:
- keep employee records organized
- update information as employees join or change roles
- monitor leave usage
- track salary and budget-related data
- support basic employee self-service actions

## Tech Stack
- Python
- Tkinter for the desktop GUI
- MySQL for data storage
- `tkcalendar` for date selection
- Pillow (`PIL`) for image handling

## Project Structure
- `main.py` - main application interface and page flow
- `functions.py` - database operations and business logic

## Setup Notes
Before running the project, make sure you have:
- Python installed
- A MySQL database configured
- Required Python packages installed:
  - `mysql-connector-python`
  - `tkcalendar`
  - `Pillow`

You will also need to update the database connection details in `functions.py` before starting the app.

## Running the Application
Run the project with:

```bash
python main.py
```

## Future Improvements
- Stronger authentication and password security
- Role-based access for HR staff, managers, and employees
- Improved reporting and analytics
- Better validation and error handling
- Export options for employee and leave records

## Summary
This HR Management System is designed as a company-facing tool for managing employee information, leave tracking, and related HR processes through a simple Python desktop application.
