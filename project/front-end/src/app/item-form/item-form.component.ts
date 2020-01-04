import { Component, OnInit } from '@angular/core';
import { ItemData } from '../models/item-data';
import { environment } from 'src/environments/environment';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-item-form',
  templateUrl: './item-form.component.html',
  styleUrls: ['./item-form.component.scss']
})
export class ItemFormComponent implements OnInit {

  public model = new ItemData();
  public predictedPrice: number = 0;
  constructor(private http: HttpClient) { }

  public async onSubmit(data: any) {
    const response: any = await this.askServerForPrediction(data);
    this.predictedPrice = response.price.toFixed(2);
  }

  private askServerForPrediction(data: any) {
    const url = environment.server_address + 'get_prediction';
    return this.http.post<any>(url, data).toPromise();
  }

  ngOnInit() {
  }

}
