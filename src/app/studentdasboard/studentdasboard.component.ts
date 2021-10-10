import { Component, OnInit } from '@angular/core';
import { SubservicesService } from '../subservices.service';
import { SalusloginService } from '../saluslogin.service';

@Component({
  selector: 'app-studentdasboard',
  templateUrl: './studentdasboard.component.html',
  styleUrls: ['./studentdasboard.component.css']
})
export class StudentdasboardComponent implements OnInit {
 //Session varibale
  public user_profile:any;
  public data :any ;
  //toolbar variable
  public toolbar_show:any;
  public toolbar_default = true;
  public toolbar_report = false;
  //timer variable
  public show = false;
  public message="";
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

  //Generate VQR
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
            this.message ="QR code has been sent"
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
