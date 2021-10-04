import { Component, OnInit } from '@angular/core';
import { NgModel } from '@angular/forms';
import { SalusloginService } from '../saluslogin.service';
import { Router } from '@angular/router';
import { FormBuilder,FormControl, FormGroup, Validators } from "@angular/forms"


@Component({
  selector: 'app-registercheck',
  templateUrl: './registercheck.component.html',
  styleUrls: ['./registercheck.component.css']
})
export class RegistercheckComponent implements OnInit {
  public signupForm : FormGroup;
  public titleAlert1 :string ="This field is required"
  constructor(private log :SalusloginService,private router: Router,private fb: FormBuilder) { 
    this.signupForm = fb.group(
      {"usernum": ['',Validators.required],})
  }


  ngOnInit(): void {
  }

  setValue(post:any){
    console.log(post.usernum)
    
  }

}
