# --------- Challenge: Database Connection ---------
"""
Create a DatabaseConnection class that:

    1- Follows the Singleton pattern (only one connection object).
    2- Has a connect() method that prints:
    "Database connected." (only once).
    3- Has a disconnect() method that prints:
    "Database disconnected." (only once).
    
-------

✅ Bonus Challenge (If You Want More!):

    Keep track of a status attribute (connected = True/False).
    Ensure calling connect() twice doesn’t print again.

"""


# Answer

class DatabaseConntion:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            
        return cls._instance
    
    def __init__(self):
        self.status = False

    def connect(self):
        if not self.status:
            self.status = True
            print("Database Connected.")
    
    def disconnect(self):
        if self.status:
            self.status = False
            print("Database Disconnected.")
            
            
# --------- Challenge: Logger with Multiple Log Levels ---------
"""
Create a Logger class that:

    1- Follows the Singleton pattern.
    2- Supports multiple log levels:
    DEBUG, INFO, WARNING, ERROR, CRITICAL.
    3- Each log level should have a different format when printing the message.
    For example, DEBUG might print [DEBUG] message, and ERROR could print [ERROR] message.
    4- Has a method get_log_history() that returns all logged messages.
    5- Ensures all instances share the same log history.
    
--------

🔥 Hints:
    - Use the Singleton pattern to make sure the log history is shared.
    - For each log level, create a separate method that formats the message differently.
    - Store all log messages in a list, and implement get_log_history() to return the full history.
"""


# Asnswer
class Logger:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            
        return cls._instance
    

            
    def __init__(self):
        if not hasattr(self, "log_history"):
            self.log_history = []
        
    
    def debug(self, message):
        self.log_history.append(f"[DEBUG] {message}")
        print(f"[DEBUG] {message}")
    
    def info(self, message):
        self.log_history.append(f"[Info] {message}")
        print(f"[INFO] {message}")
        
    def warning(self, message):
        self.log_history.append(f"[WARNING] {message}")
        print(f"[WARNING] {message}")
        
    def error(self, message):
        self.log_history.append(f"[ERROR] {message}")
        print(f"[ERROR] {message}")
        
    def critical(self, message):
        self.log_history.append(f"[CRITICAL] {message}")
        print(f"[CRITICAL] {message}")
        
    def get_log_history(self):
        if self.log_history:
            for log in self.log_history:
                print(log)
        else:
            print("There is no log")
            