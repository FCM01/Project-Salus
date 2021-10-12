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
  //qr loading screen
  public wait = false;

  public selected_file:any;
  public user_profile:any;
  public data:any;
   //breach varaiables 
   public breach_status = ""
   public breach_number :any;
   public breach_type:any;
   public quadrent:any;
   public missing:any;
   public not_at_school:any;
   public message_alert = false;
   public show_make_breach =true;
 //toolbar variable
 public toolbar_show:any;
 public toolbar_default = true;
 public toolbar_report = false;

 //timer variable
 public show = false;
 public message="";
  constructor(private sub:SubservicesService,private log :SalusloginService) { }

  ngOnInit(): void {
     //Sessions
     const user_profile_recieved = (localStorage.getItem('user_profile'));
     this.data = user_profile_recieved
     this.user_profile = JSON.parse(this.data);
     //edit variable
    let edit_session_payload ={
      "user_number":this.user_profile["staff_number"]
    }
    localStorage.setItem('user_edit_profile',JSON.stringify(edit_session_payload));
    
     //set user_number for breach alram
    let session_payload  = {
      "user_number":this.user_profile["staff_number"],
      "user_type":"security" 
    }
    localStorage.setItem('global_user_number',JSON.stringify(session_payload));
    
    //breach status 
    this.sub.getBreach()
      .subscribe(
        (data)=>{
          if(data != ""){
            this.message_alert = true
            this.show_make_breach =false
              this.breach_number =data["response"]["breach_number"]
              this.breach_type = data["response"]["breach_type"]
              this.quadrent = data["response"]["quadrant"]
              this.missing =data["response"]["students_missing"]
              this.not_at_school=data["response"]["stundents_not_at_school"]
            if (data["response"]["status"]== "onroute"){
              this.breach_status = "AID is on the Way" 
            }
            
          }
        }
      )
      
  }
   //toolbar functions
   toolbarControlEdit()
   {
     this.toolbar_show="edit"
     this.toolbar_default =false;
   }
 
   toolbarControlHome()
   {
     this.toolbar_show=""
     this.toolbar_default =true;
   }
   toolbarControlReport()
   {
     this.toolbar_report =true;
     this.toolbar_default=false;
     this.toolbar_show="";
 
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
    this.wait = true;
    let user_number  = this.user_profile["staff_number"]
    let payload = {
      "data":{
        "user_number":user_number
      }
    }
    this.sub.GenerateEnterGroundsQR(payload)
      .subscribe(
        (data)=>{
          if (data != ""){
            this.wait=false;
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
