class Issue:
    """מחלקה שמייצגת תקלה"""
    def __init__(self, issue_code, issue_type, description, status="פתוחה"):
        self.issue_code = issue_code  # קוד תקלה ייחודי
        self.issue_type = issue_type  # סוג התקלה, ניתן להזין כל ערך
        self.description = description  # תיאור התקלה
        self.status = status  # סטטוס התקלה (פתוחה, בטיפול, טופלה, אי התאמה)
        self.required_equipment = self.determine_required_equipment()  # קביעת הציוד הנדרש

    def determine_required_equipment(self):
        """פונקציה לקביעת הציוד הנדרש, כרגע ריק כי אין רשימת סוגי תקלות מוגדרת מראש"""
        return ["ציוד כללי לתיקון"]

    def update_status(self, new_status):
        """מעדכן את סטטוס התקלה"""
        self.status = new_status

    def __str__(self):
        """הצגת פרטי התקלה בצורה קריאה"""
        return (f"קוד תקלה: {self.issue_code}\n"
                f"סוג תקלה: {self.issue_type}\n"
                f"תיאור תקלה: {self.description}\n"
                f"סטטוס תקלה: {self.status}\n"
                f"ציוד נדרש: {', '.join(self.required_equipment)}")