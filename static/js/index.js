var moment = require('moment')

document.addEventListener('DOMContentLoaded', function () {
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
                url: "http://127.0.0.1:8000/api/training_by_day",
                data: {
                  "user": 1,
                  "date": "2021-07-06"
              },
                success: function (response) {
                  console.log("sukces")
                  console.log(response)
                    // if not valid user, alert the user
                    // console.log(date)
                    // actualdate = moment(date,'YYYY-MM-DD')
                    //actualdate = date
                    // console.log(actualdate)
    
                },
                error: function (response) {
                    console.log("nie działa")
                    console.log(response)
                }
            }) 
      }
        });
        calendar.render();
})
