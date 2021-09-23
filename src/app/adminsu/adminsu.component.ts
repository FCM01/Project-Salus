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
  public num = 0;
  public userarray:any;
  public databaseselected:any; 
  public titleAlert1 :string ="This field is required"
  list1 = [
    { text: 'Domestic', selected: false, value:"domestic"},
    { text: 'Security', selected: false, value:"security"},
    { text: 'Student', selected: false,  value:"student"},
    { text: 'Teacher', selected: false,  value:"teacher"},
    { text: 'Visitor', selected: false,  value:"visitor"}
  ];
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) { 
    this.databaseForm = fb.group(
      { "database_name":['',Validators.required],})
  }

  ngOnInit(): void {
  }
  public toggleSelection(item:any, list:any) {
    item.selected = !item.selected;
    this.databaseselected= item.value;

  }

  setValues()
  {
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
