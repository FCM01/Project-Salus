import { Component, OnInit } from '@angular/core';
import { SubservicesService } from '../subservices.service';
import { SalusloginService } from '../saluslogin.service';

@Component({
  selector: 'app-visitordashboard',
  templateUrl: './visitordashboard.component.html',
  styleUrls: ['./visitordashboard.component.css']
})
export class VisitordashboardComponent implements OnInit {
  //Session varibale
  public user_profile:any;
  public data :any ;

   //timer avriable
   public show = false;
   // breach varibales 
   public message_alert= false;
   public breach_type:any;
   public quadrent:any;
  constructor(private sub:SubservicesService ,private log:SalusloginService) { }

  ngOnInit(): void {
    //Sessions
    const user_profile_recieved = (localStorage.getItem('user_profile'));
    this.data = user_profile_recieved
    this.user_profile = JSON.parse(this.data);

    //edit variable
    let edit_session_payload ={
      "user_number":this.user_profile["student_number"]
    }
    localStorage.setItem('user_edit_profile',JSON.stringify(edit_session_payload));

     //breach alram fetch
     this.sub.getBreach()
     .subscribe(
       (data)=>{
         if(data != ""){
           this.message_alert = true
             this.breach_type = data["response"]["breach_type"]
             this.quadrent = data["response"]["quadrant"]
           
         }
       }
     )
  }

  GenerateVQR()
  {
    this.show = true
    let payload  =
    {
      "data":{
        "user_number":this.user_profile["student_number"],
        "user_type":"student"
      }
    }
    this.startTimer()
    this.sub.GenerateToken(payload)
      .subscribe(
        (data)=>{
          if (data["message"]=="successful")
          {
            this.pauseTimer()
          }
        }
      )


    
  }
  Cancel(){
    this.show = false
  }
  //timer area
  timeLeft: number = 6;
  interval:any;

  startTimer() {
    this.interval = setInterval(() => {
      if(this.timeLeft > 0) {
        this.timeLeft--;
      } else {
        this.timeLeft = 6;
      }
    },1000)
  }
  pauseTimer() {
    clearInterval(this.interval);
  }

}
