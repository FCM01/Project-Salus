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
  public loginForm: FormGroup;
  public User_number :any;
  public Password :any;
  public token:any;
  public i = 0;
  public temp:any ;
  public response:any;
  public request:any;
  private final_payload ={};
  public type_user:any;
  public error_message ='';
  public user_check_false= false;
  public titleAlert1 :string ="This field is required"


  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) 
  {
    
      this.loginForm = fb.group({
        "User_number":['',Validators.required],
        "password": ['', Validators.compose([Validators.required, Validators.minLength(8),Validators.maxLength(12)])],
        "validate": ''
      });
   
  }

  ngOnInit(): void {

  }

  setValues(post:any){
    this.User_number = post.User_number;
    this.Password = post.Password;
    this.final_payload = {"data":{"user_number":this.User_number,"password":this.Password}}
    this.request = this.log.LoginCredentialSend(this.final_payload)
    
      .subscribe(
        (data) => {
          console.log(data["user"])
          localStorage.setItem('user_profile',JSON.stringify(data["user"])); 
          if(data["token"] == "active" )
        {
          if (data["type_user"]=="student"){
            this.router.navigate(['/studentdash'])
          }
          else if(data["type_user"]=="teacher")
          {
            this.router.navigate(['/teacherdash']) 
          }
          else if(data["type_user"]=="domestic")
          { 
            this.router.navigate(['/domesticdash'])
          }
          else if(data["type_user"]=="security")
          {
            this.router.navigate(['/securitydash'])
          }
          else if(data["type_user"]=="visitor")
          {
            this.router.navigate(['/visitordash'])
          }
          else if(data["type_user"]=="admin")
          {
            this.router.navigate(['/admindash'])
          }
    
        }
        else(data["token"] == "down")
        {
          this.user_check_false = true
          this.error_message = data["message"]
        }
         
       },
      )
      console.log(this.response)
   

  }
 
}
