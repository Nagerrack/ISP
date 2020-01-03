import { Component, OnInit } from '@angular/core';
import { ItemData } from '../models/item-data';

@Component({
  selector: 'app-item-form',
  templateUrl: './item-form.component.html',
  styleUrls: ['./item-form.component.scss']
})
export class ItemFormComponent implements OnInit {

  public model = new ItemData();
  constructor() { }

  public onSubmit() {
    console.log('submit');
  }
  ngOnInit() {
  }

}
