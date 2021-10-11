import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SubservicesService } from '../subservices.service';
import { SalusloginService } from '../saluslogin.service';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-domesticdashboard',
  templateUrl: './domesticdashboard.component.html',
  styleUrls: ['./domesticdashboard.component.css']
})
export class DomesticdashboardComponent implements OnInit {
  public user_profile:any;
  public data :any ;
  //toolbar variable
 public toolbar_show:any;
 public toolbar_default = true;
 public toolbar_report = false;
   //timer avriable
   public show = false;
   // breach varibales 
   public message_alert = false;
   public breach_type:any;
   public quadrent:any;
 
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder,private sub:SubservicesService ) { 
 
  }

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
  GenerateVQR()
  {
    this.show = true
    let payload  =
    {
      "data":{
        "user_number":this.user_profile["staff_number"],
        "user_type":"domestic"
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
