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
  public signupForm:any;
  constructor() { }

  ngOnInit(): void {
  }

}
