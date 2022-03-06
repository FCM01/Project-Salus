import { Component, OnInit } from '@angular/core';
import { SalusloginService } from '../saluslogin.service';
import { Router } from '@angular/router';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"


@Component({
  selector: 'app-visitorssu',
  templateUrl: './visitorssu.component.html',
  styleUrls: ['./visitorssu.component.css']
})
export class VisitorssuComponent implements OnInit {
  public wait = false;
  public signupForm : FormGroup;
  public payload:any;
  public error_message ="";
  public titleAlert2 :string ="Please enter in an password that is 8 charaters long"
  public titleAlert1 :string ="This field is required"
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) {
    this.signupForm =fb.group(
      {
      "name": ['', Validators.required],
      "surname": ['', Validators.required],
      "id_number": ['', Validators.required],
      "date_of_birth": ['', Validators.required],
      "email": ['', Validators.email],
      "purpose": ['', Validators.required],
      "password": ['', Validators.compose([Validators.required, Validators.minLength(8),Validators.maxLength(12)])],
        "passwordconfirm": ['', Validators.compose([Validators.required, Validators.minLength(8),Validators.maxLength(12)])],
      "cnr": ['',Validators.required],
      "address": ['',Validators.required],
      "city": ['',Validators.required],
      "pcode": ['',Validators.required],
      "validate": ''
      })
   }

  ngOnInit(): void {
  }
  password_check(password_1:any,password_2:any){
    let final_password;
    if (password_2 == password_1){
      final_password = password_2
      return {"responce":1,"password":final_password}
    }
    else{
      return {"responce":0}
    }
  }
  setValues(post:any){
    this.wait = true;
    let checked_password =this.password_check(post.password,post.passwordconfirm)
    if (checked_password["responce"] ==0){
      this.wait =false
      this.error_message = "Passwords dont match"

    }
    else{

    this.payload ={
      "data":{
                "name":post.name,
                "surname":post.surname,
                "id_number":post.id_number,
                "date_of_birth":post.date_of_birth,
                "email":post.email,
                "phone_number":post.cnr,
                "address":post.address,
                "city":post.city,
                "pcode":post.pcode,
                "password":checked_password["password"],
                "staff_number":post.visitornum,
                "position":post.position,
                "purpose_of_visit":post.purpose,
      }
    
    
    }
    let session_payload = {"name":post.name,"surname":post.surname,"visitor_number":post.visitornum}
    localStorage.setItem('user_profile',JSON.stringify( session_payload))
    this.log.VisitorSignUp(this.payload)
        .subscribe(
          (data)=>{
            this.wait=false
            if (data["message"]=="succeessful")
            {
              this.router.navigate(["/visitordash"]);
              
            }
          }
        )
    
  
}
  }
}
