import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { SalusloginService } from '../saluslogin.service';
import { SubservicesService } from '../subservices.service';

@Component({
  selector: 'app-securitydashboard',
  templateUrl: './securitydashboard.component.html',
  styleUrls: ['./securitydashboard.component.css']
})
export class SecuritydashboardComponent implements OnInit {
  public selected_file:any;
  public user_profile:any;
  public data:any;
  constructor(private sub:SubservicesService,private http :HttpClient,private log :SalusloginService) { }

  ngOnInit(): void {
    //Sessions
    const user_profile_recieved = (localStorage.getItem('user_profile'));
    this.data = user_profile_recieved
    this.user_profile = JSON.parse(this.data);
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

GenrateQR(){
    let user_number  = this.user_profile["staff_number"]
    console.log(user_number)
    let payload = {
      "data":{
        "user_number":user_number
      }
    }
    this.sub.GenerateEnterGroundsQR(payload)
      .subscribe(
        (data)=>{
          console.log(data)
        }
      )


}

}
