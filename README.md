# PyBank
This project is a banking system built with Python using Tkinter for the graphical user interface (GUI). The system allows users to log in, check their account balance, and perform transactions such as deposits and withdrawals. It also includes the functionality for changing the user PIN. Users are stored in a text file with their details (username, PIN, and balance), and the system ensures data persistence through file-based storage.
Key features include:

User Authentication: Users log in with a unique username and PIN.
Transaction Management: Supports deposit and withdrawal operations, with balance checking and updates.
User Management: Admin functionality to add new users with username, PIN, and initial balance. Validation ensures usernames are unique, PINs are 4 digits, and balances are positive numbers.
File Persistence: All user data is stored and retrieved from a text file, ensuring data persists across sessions.
GUI Design: The interface is user-friendly, with buttons for each operation and error handling through message boxes for invalid input.
