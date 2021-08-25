import moment from "@moment";

document.addEventListener('DOMContentLoaded', function () {
    console.log("Załadowany dokument")
    var calendarEl = document.getElementById('calendarclient');
    var calendar = new FullCalendar.Calendar(calendarEl, {
          initialView: 'dayGridMonth',
          contentHeight: 360,
          eventTextColor: 'red',
          locale: 'pl',
          firstDay: 1,
          navLinks: true,
          navLinkDayClick: function(date, jsEvent) {
            $.ajax({
                type: 'POST',
                url: "{% url 'training_by_day' %}",
                data: {
                  "user": 1,
                  "date": "2021-07-06"
                },
                success: function (response) {
                    // if not valid user, alert the user
                    console.log(date)
                    actualdate = moment(date,'MMDDYYYY')
                    //actualdate = date
                    console.log(actualdate)
    
                },
                error: function (response) {
                    console.log(response)
                }
            }) 
      }
        });
        calendar.render();
})
