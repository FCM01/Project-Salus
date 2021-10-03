import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
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
  public databaseselected="student"; 
  public titleAlert1 :string ="This field is required"

  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) { 
    this.databaseForm = fb.group(
      { "database_name":['',Validators.required],})
  }

  ngOnInit(): void {  

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

}
