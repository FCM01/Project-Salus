import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SalusloginService } from '../saluslogin.service';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"


@Component({
  selector: 'app-adminsu',
  templateUrl: './adminsu.component.html',
  styleUrls: ['./adminsu.component.css']
})
export class AdminsuComponent implements OnInit {
  public databaseForm: FormGroup;
  public payload = {};
  public userarray:any;
  public titleAlert1 :string ="This field is required"
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) { 
    this.databaseForm =fb.group(
      { "database_name":['',Validators.required],})
  }

  ngOnInit(): void {
  }

  setValues(post:any)
  {
    this.payload = {
      "data":{
        "database_name":post.database_name
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

}
}
