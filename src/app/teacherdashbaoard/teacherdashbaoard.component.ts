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
    //database tool
    console.log(this.databaseselected)
    this.payload = {
      "data":{
        "database_name":this.databaseselected
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
  
  GenerateQR()
  {
    let user_number  = this.user_profile["staff_number"]
    let payload = {
      "data":{
        "user_number":user_number
      }
    }
    this.sub.RegisterClass(payload)
      .subscribe(
        (data)=>{
          console.log(data)
        }
      )
  }

}
