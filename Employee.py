class Employee:
    def __init__(self, name, id_number, employee_number, email, phone):
        """אתחל את המחלקה עם המאפיינים שנדרשו"""
        self.name = name
        self.id_number = id_number
        self.employee_number = employee_number
        self.email = email
        self.phone = phone

    def __str__(self):
        """הצגת המידע של העובד בצורה קריאה"""
        return (f"שם עובד: {self.name}\n"
                f"תעודת זהות: {self.id_number}\n"
                f"מספר עובד: {self.employee_number}\n"
                f"כתובת מייל: {self.email}\n"
                f"מספר טלפון: {self.phone}")