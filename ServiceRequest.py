from datetime import datetime

class ServiceRequest:
    """מחלקה שמייצגת קריאת שירות"""
    
    def __init__(self, request_number, location, open_date=None, status="פתוחה"):
        self.request_number = request_number  # מספר קריאה ייחודי
        self.location = location  # מיקום הקריאה
        self.open_date = open_date if open_date else datetime.now().strftime("%Y-%m-%d")  # תאריך פתיחה (ברירת מחדל: היום)
        self.status = status  # סטטוס הקריאה (פתוחה, בטיפול, טופלה, סגורה)

    def update_status(self, new_status):
        """עדכון סטטוס הקריאה"""
        self.status = new_status

    def __str__(self):
        """הצגת פרטי הקריאה בצורה קריאה"""
        return (f"מספר קריאה: {self.request_number}\n"
                f"מיקום: {self.location}\n"
                f"תאריך פתיחה: {self.open_date}\n"
                f"סטטוס קריאה: {self.status}")