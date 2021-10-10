import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { SalusloginService } from '../saluslogin.service';
import { SubservicesService } from '../subservices.service';

@Component({
  selector: 'app-securitydashboard',
  templateUrl: './securitydashboard.component.html',
  styleUrls: ['./securitydashboard.component.css']
})
export class SecuritydashboardComponent implements OnInit {
  public selected_file:any;
  public user_profile:any;
  public data:any;
   //breach varaiables 
   public breach_status = ""
   public breach_number :any;
   public breach_type:any;
   public quadrent:any;
   public message_alert = false;
   //toolbar variable
  public toolbar_show:any;
   //timer avriable
   public show = false;
  constructor(private sub:SubservicesService,private log :SalusloginService) { }

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
    
     //set user_number for breach alram
    let session_payload  = {
      "user_number":this.user_profile["admin_number"],
      "user_type":"admin" 
    }
    localStorage.setItem('global_user_number',JSON.stringify(session_payload));
    
    //breach status 
    this.sub.getBreach()
      .subscribe(
        (data)=>{
          if(data != ""){
            this.message_alert = true
              this.breach_number =data["response"]["breach_number"]
              this.breach_type = data["response"]["breach_type"]
              this.quadrent = data["response"]["quadrant"]
            if (data["response"]["status"]== "onroute"){
              this.breach_status = "AID is on the Way" 
            }
            
          }
        }
      )
      
  }
  toolbarControlEdit()
  {
    this.toolbar_show="edit"

  }
  
  deleteBreach()
  {
    let payload =
    {
      "data":{
        "breach_number":this.breach_number
      }
    }

    this.sub.DeleteBreachAlarm(payload)
      .subscribe(
        (data)=>{
          if (data["status"]==200){
          
          this.message_alert = false
          }
        }
      )

  }

GenrateQR(){
    let user_number  = this.user_profile["staff_number"]
    console.log(user_number)
    let payload = {
      "data":{
        "user_number":user_number
      }
    }
    this.sub.GenerateEnterGroundsQR(payload)
      .subscribe(
        (data)=>{
          console.log(data)
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
