import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SubservicesService } from '../subservices.service';
import { SalusloginService } from '../saluslogin.service';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-teacherdashbaoard',
  templateUrl: './teacherdashbaoard.component.html',
  styleUrls: ['./teacherdashbaoard.component.css']
})
export class TeacherdashbaoardComponent implements OnInit {
  public wait = false;
  public databaseForm: FormGroup;
  public payload = {};
  public num = 0;
  public userarray=null;
  public user_profile:any;
  public data:any;
  public databaseselected="student"; 
  public titleAlert1 :string ="This field is required"
  //toolbar variable
  public toolbar_show:any;
  public toolbar_default = true;
  public toolbar_report = false;

  //timer variable
  public show = false;
  public message="";

  constructor(private sub:SubservicesService,private log :SalusloginService,private router: Router,private fb: FormBuilder) { 
    this.databaseForm = fb.group(
      { "database_name":['',Validators.required],})
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
    //set user_number for breach alram
    let session_payload  = {
      "user_number":this.user_profile["staff_number"],
      "user_type":"teacher"
    }
    localStorage.setItem('global_user_number',JSON.stringify(session_payload));
    //database tool
    this.payload = {
      "data":{
        "database_name":"teacher"
      }
    }
    this.log.GetUsers(this.payload)
      .subscribe(
        (data)=>{

          if (data["response"] != "")
          {
            this.userarray =data["response"]
          }

        }
      )
      console.log (this.userarray)


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

  //Maintain functions
  deletUser(name:any,surname:any)
  {
    console.log ("type user ==>",this.databaseselected)
    this.payload ={
      "data":{
      "name":name,
      "surname":surname,
      "user_type":this.databaseselected
      }
    }
    console.log(this.payload)
    this.log.DeleteUser(this.payload)
      .subscribe(
        (data)=>
        {
          if(data["message"]=="deleted")
          {

            alert("User has been deleted")
            location.reload()

          }
        }
      )

  }
  
  GenerateQR()
  {
    this.wait = true;
    let user_number  = this.user_profile["staff_number"]
    let payload = {
      "data":{
        "user_number":user_number
      }
    }
    this.sub.RegisterClass(payload)
      .subscribe(
        (data)=>{
          if (data != ""){
            this.wait=false;
          }
        }
      )
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
