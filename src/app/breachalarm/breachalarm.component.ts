import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-breachalarm',
  templateUrl: './breachalarm.component.html',
  styleUrls: ['./breachalarm.component.css']
})
export class BreachalarmComponent implements OnInit {
  public quadrent:any;
  constructor() { }

  ngOnInit(): void {
  }
  GetQuadrent(q:string)
  {
    console.log(q)
    if ( q =="Quadrant 1"){
      this.quadrent = "q1"
    }
    

  }

}
