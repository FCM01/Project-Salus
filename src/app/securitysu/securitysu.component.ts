import { Component, OnInit } from '@angular/core';
import { SalusloginService } from '../saluslogin.service';
import { Router } from '@angular/router';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-securitysu',
  templateUrl: './securitysu.component.html',
  styleUrls: ['./securitysu.component.css']
})
export class SecuritysuComponent implements OnInit {
  public signupForm : FormGroup;
  public payload:any;
  public titleAlert2 :string ="Please enter in an password that is 8 charaters long"
  public titleAlert1 :string ="This field is required"
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) {
    this.signupForm = fb.group({
      "name": ['', Validators.required],
      "surname": ['', Validators.required],
      "id_number": ['', Validators.required],
      "date_of_birth": ['', Validators.required],
      "petrol_sector": ['', Validators.required],
      "register_class": ['', Validators.required],
      "position": ['', Validators.required],
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
    console.log("working")
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
                "petrol_sector":post.petrol_sector,
      }
    
    
    }
    this.log.SecuritySignUp(this.payload)
        .subscribe(
          (data)=>{
            console.log(data);
            if (data["message"]=="succeessful")
            {
              this.router.navigate(["/securitydash"])
            }
          }
        )
    
  
}

}
