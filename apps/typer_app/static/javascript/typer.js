$(document).ready(function(){
    // logged keystrokes that are correct.  
    stopwatch()
// starting time
    var correct = 0
    var completed = ""
    var original = $(".upcoming").text()
    var mistakes = 0
    var total_keystrokes = 0
    var user_typed = ""
    $(document).keydown(function(e){
        // Check if shift was pressed
        console.log(e.key);
        var input = $("#user_input").val()
        var completed = $(".completed").text()
        var current_word = $(".current_word").text()
        var upcoming = $(".upcoming").text()
        var typed = $(".typed").text()
        var target = $('#target_id').text()

        if(e.key == "Shift"){
            console.log("Do nothing");
        }
        // Check for backspace
        else if(e.key == "Backspace"){
            if(user_typed != completed){
                $('.upcoming')
            }
            user_typed = user_typed.slice(0, -1);
            $(".typed").text(user_typed)
            // 
        }
        // check for space
        else if(e.key == "Space"){
        }
        // every other key
        else{
            input += e.key
            // console.log(`Now comparing ${e.key} with ${upcoming[0]}`);
            if(e.key==upcoming[0] && completed == user_typed){
                $('.upcoming').css("background-color", "white")
                var s2 = upcoming.substring(1);
                console.log('match');
                $(".completed").text(completed + e.key);
                $(".upcoming").text(s2);
                console.log(input)                                                                          
                correct +=1;
            }
            else{
                mistakes +=1;
                $(".upcoming").css("background-color", "red")
                
            }
            total_keystrokes ++;
            $("#total_keystrokes").text(`Total Keystrokes: ${total_keystrokes}`);
            $("#mistakes").text(`Errors: ${mistakes}`);
            $("#correct").text(`Correct: ${correct}`);
            user_typed += e.key;
            $(".typed").text(user_typed)


        }
        //update hidden form values
        $("#total_char").val(total_keystrokes)
        $("#num_correct").val(correct)
        $("#mistakes").val(mistakes)
        $("#whole_string").val(user_typed)

        console.log(`User: ${user_typed} vs. ${original}`)
        if (user_typed == original){
            // ending time
            console.log('Race is finished')
            $("#hidden-form").submit()
        }
    })


});
    // var time = "{{time}}";

    function stopwatch() {
        var seconds = 0;
        var minutes = 0;
        setInterval(function () {
            //Stops the race and submits hidden form
            if (seconds == 0 && minutes == 30) {
                $("#hidden-form").submit()
            } else {

                // two if seconds < 10
                // create a varible with padded number
                // if minutes < 10 
                // create a variable with padded number
                // concat the two variables together

                // compare each second to the start time

                if (seconds == 59 && minutes < 10) { // 08:59 09:00
                    $("#stopwatch").text(`0${minutes}:${seconds}`)
                    minutes++;
                    seconds = 0;
                } else if (seconds == 59 && minutes > 9) { // 10:59 11:00
                    console.log("11th minute")
                    $("#stopwatch").text(`${minutes}:${seconds}`)
                    minutes++;
                    seconds = 0;
                } else if (minutes < 10 && seconds < 10) {
                    $("#stopwatch").text(`0${minutes}:0${seconds}`)
                    seconds++;
                } else if (minutes < 10 && seconds > 9) {

                    $("#stopwatch").text(`0${minutes}:${seconds}`)
                    seconds++;
                } else if (minutes > 9 && seconds < 10) {

                    $("#stopwatch").text(`${minutes}:0${seconds}`)
                    seconds++;
                } else {
                    $("#stopwatch").text(`${minutes}:${seconds++}`)
                    seconds++;

                }
            }
            // update form
            $("#seconds").val(seconds)
            $("#minutes").val(minutes)
        }, 1000)
    }
