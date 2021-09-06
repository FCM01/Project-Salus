import { Component, OnInit } from '@angular/core';
import { NgModel } from '@angular/forms';

@Component({
  selector: 'app-registercheck',
  templateUrl: './registercheck.component.html',
  styleUrls: ['./registercheck.component.css']
})
export class RegistercheckComponent implements OnInit {
  public user_number = NgModel;
  public valid =false;
  constructor() { }


  ngOnInit(): void {
  }

  setValue(user_number:any){
    this.user_number= user_number;
    
  }

}
