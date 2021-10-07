import { Component, OnInit } from '@angular/core';
import { SalusloginService } from '../saluslogin.service';
import { Router } from '@angular/router';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-staffsu',
  templateUrl: './staffsu.component.html',
  styleUrls: ['./staffsu.component.css']
})
export class StaffsuComponent implements OnInit {
  public signupForm : FormGroup;
  public wait = false;
  public payload:any;
  public titleAlert2 :string ="Please enter in an password that is 8 charaters long"
  public titleAlert1 :string ="This field is required"
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) {
    this.signupForm = fb.group({
      "name": ['', Validators.required],
      "surname": ['', Validators.required],
      "id_number": ['', Validators.required],
      "date_of_birth": ['', Validators.required],
      "subject": ['', Validators.required],
      "register_class": ['', Validators.required],
      "position": ['', Validators.required],
      "staffnum": ['',Validators.required],
      "email": ['', Validators.email],
      "password": ['', Validators.compose([Validators.required, Validators.maxLength(8)])],
      "passwordconfirm": ['', Validators.compose([Validators.required, Validators.maxLength(8)])],
      "cnr": ['',Validators.required],
      "address": ['',Validators.required],
      "city": ['',Validators.required],
      "pcode": ['',Validators.required],
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
                "staff_number":post.staffnum,
                "position":post.position,
                "subject":post.subject,
                "register_class":post.register_class,
      }
    
    
    }

    this.log.TeacherSignUp(this.payload)
        .subscribe(
          (data)=>{
            this.wait=false
            if (data["message"]=="succeessful")
            {
              this.router.navigate(["/teacherdash"])
            }
          }
        )
    
  
}


}
