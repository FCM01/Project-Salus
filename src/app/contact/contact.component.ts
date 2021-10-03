import { Component, OnInit } from '@angular/core';
import { SubservicesService } from '../subservices.service';
import { Router } from '@angular/router';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.css']
})
export class ContactComponent implements OnInit {

  public signupForm : FormGroup;
  public payload:any;
  public titleAlert1 :string ="This field is required"
  constructor(private fb: FormBuilder,private sub:SubservicesService,private router: Router) {
    this.signupForm = fb.group({
      "name": ['', Validators.required],
      "email": ['', Validators.email],
      "message": ['', Validators.required],
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
                "message":post.message,
                "email":post.email
      }
    }
    this.sub.leaveComments(this.payload)
      .subscribe(
        (data)=>
        {
          console.log(data)
          if (data["message"] =="successful")
          {
            location.reload();
            alert("Message Sent")

          }
        }
      )



}
}