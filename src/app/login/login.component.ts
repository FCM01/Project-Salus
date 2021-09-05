import { Component, OnInit } from '@angular/core';
import { SalusloginService } from '../saluslogin.service';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from "@angular/forms"



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public rForm: FormGroup;
  public responce:any ;
  public user_number ="" ;
  public password ="";
  private final_payload ={};
  public titleAlert: string = "Please enter in your email"
  public titleAlert2 :string ="Please enter in an password"

  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) 
  {
    this.rForm = fb.group({
      "user_email": ['', Validators.email],
      "password": ['', Validators.compose([Validators.required, Validators.maxLength(8)])],
      "validate": ''
    })
  }

  ngOnInit(): void {

  }

  setValues(user_num :any ,pass:any){
    this.user_number = user_num;
    this.password= pass;
    this.final_payload = {"data":{"user_number":this.user_number,"password":this.password}}
    this.responce=this.log.LoginCredentialSend(this.final_payload)
      .subscribe()
    console.log("what the subcribed observable gave back ==>",this.responce);
  }
 
}
