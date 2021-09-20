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

  public signupForm:any;
  constructor() { }

  ngOnInit(): void {
  }

}
