import Employee

class Dispatcher(Employee):
    """מחלקת מוקדן משלח היורשת מעובד"""
    def __init__(self, name, id_number, employee_number, email, phone, region):
        super().__init__(name, id_number, employee_number, email, phone)
        self.region = region  # אזור אחריות

    def view_service_request(self, service_request):
        """צפייה בפרטי קריאת שירות"""
        return str(service_request)

    def assign_technician(self, technicians, service_request):
        """בחירת הטכנאי המתאים לקריאה"""
        for technician in technicians:
            if technician.availability_status == "פעיל":
                return f"טכנאי {technician.name} נבחר לקריאה {service_request.request_number}"
        return "אין טכנאי זמין לטיפול בקריאה"

    def __str__(self):
        return super().__str__() + f"\nאזור אחריות: {self.region}"