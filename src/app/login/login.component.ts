import { Component, OnInit } from '@angular/core';
import { SalusloginService } from '../saluslogin.service';
import { Router } from '@angular/router';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  // public rForm: FormGroup;
  public responce:any ;
  public User_number :any;
  public Password :any;
  public i = 0;
  public temp:any ;
  private final_payload ={};
  public loginForm: any;
  public titleAlert: string = "Please enter in your email"
  public titleAlert2 :string ="Please enter in an password"

  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) 
  {
    
      this.loginForm = new FormGroup({
        "User_number": new FormControl(null,[Validators.required, Validators.pattern('[0-9]*')]),
        "Password": new FormControl(null, [Validators.required, Validators.pattern('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+')])
      });
   
  }

  ngOnInit(): void {

  }

  setValues(user_num :any ,pass:any){
    this.User_number = user_num;
    this.Password = pass;
    this.final_payload = {"data":{"user_number":this.User_number,"password":this.Password}}
    console.log("what the subcribed observable gave back ==>",this.final_payload );
    this.responce=this.log.LoginCredentialSend(this.final_payload)
      .subscribe()
    
    this.temp =this.responce["_subscriptions"]
    console.log(this.temp)

    for(this.i = 0; this.i <5;this.i++){
      console.log(this.responce["_subscriptions"][this.i]);
    }
  }
 
}
