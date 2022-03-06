import { Component, OnInit } from '@angular/core';
import { SalusloginService } from '../saluslogin.service';
import { Router } from '@angular/router';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"


@Component({
  selector: 'app-studentsu',
  templateUrl: './studentsu.component.html',
  styleUrls: ['./studentsu.component.css']
})
export class StudentsuComponent implements OnInit {
  public wait = false;
  public signupForm : FormGroup;
  public error_message ='';
  public payload:any;
  public titleAlert2 :string ="Please enter in an password that is 8 charaters long"
  public titleAlert1 :string ="This field is required"
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) {
    this.signupForm = fb.group({
      "name": ['', Validators.required],
      "surname": ['', Validators.required],
      "id_number": ['', Validators.compose([Validators.required, Validators.maxLength(13)])],
      "date_of_birth": ['', Validators.required],
      "studentnum": ['',Validators.required],
      "register_class": ['', Validators.required],
      "email": ['', Validators.email],
      "password": ['', Validators.compose([Validators.required, Validators.minLength(8),Validators.maxLength(12)])],
        "passwordconfirm": ['', Validators.compose([Validators.required, Validators.minLength(8),Validators.maxLength(12)])],
      "cnr": ['',Validators.required],
      "address": ['',Validators.required],
      "city": ['',Validators.required],
      "pcode": ['',Validators.required],
      "pg_name": ['',Validators.required],
      "pg_surname": ['',Validators.required],
      "pg_id_number": ['',Validators.required],
      "pg_cnum": ['',Validators.required],
      "pg_email": ['',Validators.required],
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
                "student_number":post.studentnum,
                "register_class":post.register_class,
                "pg_name": post.pg_name,
                "pg_surname": post.pg_surname,
                "pg_id_number": post.pg_id_number,
                "pg_cnum": post.pg_cnum,
                "pg_email":post.pg_email,
                
      }
    
    
    }
    let session_payload = {"name":post.name,"surname":post.surname,"student_number":post.studentnum}
    localStorage.setItem('user_profile',JSON.stringify(session_payload))
    this.log.StudentSignUp(this.payload)
        .subscribe(
          (data)=>{
            this.wait=false
            if (data["message"]=="succeessful")
            {
              this.router.navigate(["/studentdash"])
            }
            else{
              this.error_message = data["message"]
              console.log(data["message"])
            }
          }
        )
        } 
  
}

}
function stringyfy(arg0: string | undefined): string {
  throw new Error('Function not implemented.');
}

