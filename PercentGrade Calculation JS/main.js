var x = document.getElementById("btn");
        x.addEventListener("mouseover", calculate);
        function calculate(){
            let nepali = document.studentform.nepali.value;
            let english = document.studentform.english.value; 
            let math = document.studentform.math.value;
            let Science = document.studentform.science.value; 
            let social = document.studentform.social.value;
            let health = document.studentform.health.value; 
            let addm = document.studentform.addm.value;
            let account = document.studentform.account.value;      
            let total = parseFloat(nepali) + parseFloat(english) 
            + parseFloat(math) + parseFloat(Science)
            + parseFloat(social) + parseFloat(health) 
            + parseFloat(addm) + parseFloat(account);
            let percnt = (total/800)*100;
            // alert(percnt);
            if (percnt >= 80 && percnt <= 100 ) {
                grades = 'A';
            } else if(percnt >= 60 && percnt <= 79) {
                grades = 'B';
            }
            else if(percnt >= 40 && percnt <= 59) {
                grades = 'C';
            }
            else {
                grades = 'F';
            }

            if (percnt >= 39.5) {
                document.getElementById("showresult").innerHTML = `Out of 200 your 
            total is ${total} and percentage is ${percnt}%. <br> Your grade is 
            ${grades}. You are Pass.`
            }
            else{
                document.getElementById("showresult").innerHTML = `Out of 800 your 
            total is ${total} and percentage is ${percnt}%. <br> Your grade is 
            ${grades}. You are Fail.`
            }           
            
        }