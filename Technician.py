import Employee

class Technician(Employee):
    """מחלקת טכנאי היורשת מעובד"""
    def __init__(self, name, id_number, employee_number, email, phone, availability_status="פעיל"):
        super().__init__(name, id_number, employee_number, email, phone)
        self.availability_status = availability_status  # פעיל / לא פעיל

    def view_issue_description(self, issue_description):
        """פונקציה להצגת תיאור התקלה"""
        return f"תיאור התקלה: {issue_description}"

    def diagnose_issue(self, issue_type):
        """פונקציה לאבחון התקלה אם היא פתירה ברמת הטכנאי"""
        if issue_type in ["חשמל", "אינטרנט", "מים", "גז"]:
            return f"התקלה מסוג {issue_type} ניתנת לטיפול ברמת הטכנאי."
        return f"התקלה מסוג {issue_type} דורשת מומחה נוסף - אי התאמה."

    def __str__(self):
        return super().__str__() + f"\nסטטוס זמינות: {self.availability_status}"