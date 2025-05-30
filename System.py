class System:
    """מחלקת מערכת לניהול תקלות ושליחת התראות"""

    def update_issue_description(self, issue, new_description):
        """עדכון תיאור התקלה"""
        issue.description = new_description
        return f"תיאור התקלה עודכן ל: {new_description}"

    def update_issue_status(self, issue, new_status):
        """עדכון סטטוס התקלה"""
        issue.status = new_status
        alert_message = f"סטטוס התקלה עודכן ל: {new_status}"

        # אם הסטטוס הוא 'אי התאמה', מפעילים התראה
        if new_status == "אי התאמה":
            self.notify_dispatcher(issue)

        return alert_message

    def notify_dispatcher(self, issue):
        """שליחת התראה למוקדן המשלח במקרה של 'אי התאמה'"""
        notification = f"התראה: התקלה {issue.issue_code} אינה ניתנת לטיפול! יש לפעול בהתאם."
        print(notification)  # ניתן להחליף במערכת הודעות אמיתית
        return notification