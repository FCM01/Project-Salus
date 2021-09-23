import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { SalusloginService } from '../saluslogin.service';

@Component({
  selector: 'app-securitydashboard',
  templateUrl: './securitydashboard.component.html',
  styleUrls: ['./securitydashboard.component.css']
})
export class SecuritydashboardComponent implements OnInit {
  public selected_file:any;
  constructor(private http :HttpClient,private log :SalusloginService) { }

  ngOnInit(): void {
  }
onFileEvent(event:any){
  console.log(event)
  this.selected_file =<File>event.target.files[0]
  const fb = new FormData();
  fb.append('image',this.selected_file,this.selected_file.name);
  this.log.onUpload(fb)
    .subscribe(
      (data)=>{
        console.log(data);
      }
    )

}

}
