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
  public payload:any;
  public titleAlert2 :string ="Please enter in an password that is 8 charaters long"
  public titleAlert1 :string ="This field is required"
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) {
    this.signupForm = fb.group({
      "name": ['', Validators.required],
      "surname": ['', Validators.required],
      "id_number": [''],
      "date_of_birth": ['', Validators.required],
      "studentnum": ['',Validators.required],
      "register_class": ['', Validators.required],
      "email": ['', Validators.email],
      "password": ['', Validators.compose([Validators.required, Validators.maxLength(8)])],
      "passwordconfirm": ['', Validators.compose([Validators.required, Validators.maxLength(8)])],
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
  setValues(post:any){
    this.wait = true;
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
                "password":post.passwordconfirm,
                "student_number":post.studentnum,
                "register_class":post.register_class,
                "pg_name": post.pg_name,
                "pg_surname": post.pg_surname,
                "pg_id_number": post.pg_id_number,
                "pg_cnum": post.pg_cnum,
                "pg_email":post.pg_email,
                
      }
    
    
    }
    this.log.StudentSignUp(this.payload)
        .subscribe(
          (data)=>{
            this.wait=false
            if (data["message"]=="succeessful")
            {
              this.router.navigate(["/studentdash"])
            }
          }
        )
    
  
}

}
