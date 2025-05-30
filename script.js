document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("updateForm");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // מונע רענון הדף

        let status = document.getElementById("status").value;
        let notes = document.getElementById("notes").value;

        if (!status) {
            alert("נא לבחור סטטוס");
            return;
        }

        if (status === "אי התאמה") {
            alert("נשלחה הודעה למוקדן המשלח!");
        } else {
            alert("סטטוס עודכן בהצלחה!\n\nסטטוס: " + status + "\nהערות: " + notes);
        }
    });
});

