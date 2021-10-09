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

  constructor(private sub:SubservicesService,private log :SalusloginService,private router: Router,private fb: FormBuilder) { 
    this.databaseForm = fb.group(
      { "database_name":['',Validators.required],})
  }

  ngOnInit(): void {  
    //Sessions
    const user_profile_recieved = (localStorage.getItem('user_profile'));
    this.data = user_profile_recieved
    this.user_profile = JSON.parse(this.data);
    //set user_number for breach alram
    let session_payload  = {
      "user_number":this.user_profile["staff_number"],
      "user_type":"admin"
    }
    //database tool
    this.payload = {
      "data":{
        "database_name":"student"
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
          this.wait=false
          console.log(data)
        }
      )
  }

}
