import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { SalusloginService } from '../saluslogin.service';
import { SubservicesService } from '../subservices.service';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-admindashboard',
  templateUrl: './admindashboard.component.html',
  styleUrls: ['./admindashboard.component.css']
})
export class AdmindashboardComponent implements OnInit {
  public databaseForm: FormGroup;
  public payload = {};
  public num = 0;
  public data :any ;
  public datetime:any;
  public user_profile:any;
  public messages =null;
  public userarray=null;
  public status:any;
  public location:any;
  public databaseselected:any; 
  public titleAlert1 :string ="This field is required"
  list1 = [
    { text: 'Domestic', selected: false, value:"domestic"},
    { text: 'Security', selected: false, value:"security"},
    { text: 'Student', selected: false,  value:"student"},
    { text: 'Teacher', selected: false,  value:"teacher"},
    { text: 'Visitor', selected: false,  value:"visitor"}
  ];
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder,private sub :SubservicesService) { 
    this.databaseForm = fb.group(
      { "database_name":['',Validators.required],})
  }

  ngOnInit(): void {
    //date area

    this.datetime = new Date();
   
    //Sessions
    const user_profile_recieved = (localStorage.getItem('user_profile'));
    this.data = user_profile_recieved
    this.user_profile = JSON.parse(this.data);

    //set user_number for breach alram
    let session_payload  = {
      "user_number":this.user_profile["admin_number"],
      "user_type":"admin"
    }
    localStorage.setItem('global_user_number',JSON.stringify(session_payload));
    this.sub.getComments()
    .subscribe(
      (data)=>
      {
        this.messages  = data["response"]

      }
    )
   
  }
  public toggleSelection(item:any, _list:any) {
    item.selected = !item.selected;
    this.databaseselected= item.value;

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
            this.userarray = data["response"]
          }

        }
      )
      console.log (this.userarray)

}
GenerateToken()
{
  console.log("sending")
  this.status="Generating";
  let user_number =this.user_profile["admin_number"]
  this.payload={
    "data":{
      "user_number":user_number,
      "user_type":"admin"
    }
  }
  this.sub.GenerateToken(this.payload)
    .subscribe(
      (data)=>
      {
        if (data["status"]=="200")
        {
          this.status = "TOKEN CReAtED AND SENT "
        }
        console.log(data)
      }
    )
  

}
}


