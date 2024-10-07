import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

import {ChatsComponent} from './components/chats/chats.component';
import { GraphComponent } from './components/graph/graph.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, ChatsComponent, GraphComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'frontend';
}
