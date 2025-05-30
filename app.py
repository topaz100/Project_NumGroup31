import Technician
import Dispatcher
import Issue
import System
import ServiceRequest

# יצירת מוקדן וטכנאי
dispatcher = Dispatcher("ליאורה שמש", "321654987", "D001", "liora@example.com", "050-1230000", "מרכז")
technician = Technician("יוסי כהן", "987654321", "T001", "yossi@example.com", "050-9870000")

# יצירת תקלה וקריאה
issue = Issue("ISS123", "אינטרנט", "אין קליטה בנתב")
request = ServiceRequest("222", "תל אביב")

# הדפסת מצב לפני
print("— סטטוס ראשוני —")
print(issue)
print()

# סימולציה: הטכנאי בודק ומעדכן סטטוס ל"אין התאמה"
system = System()
diagnosis = technician.diagnose_issue(issue.issue_type)
print("אבחון טכנאי:", diagnosis)

# אם יש אי התאמה, עדכון התקלה ושיגור הודעה
if "אי התאמה" in diagnosis:
    system.update_issue_status(issue, "אי התאמה")

print("\n— מצב לאחר העדכון —")
print(issue)
