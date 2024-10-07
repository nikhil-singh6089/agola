import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

import { ChatService } from '../../services/chat.service';

@Component({
  selector: 'app-message',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './message.component.html',
  styleUrl: './message.component.css'
})
export class MessageComponent {
  userMessage: string = '';

  constructor(private http: HttpClient,private chatService: ChatService) {}

  sendMessage() {
    if (this.userMessage.trim()) {
      // Send the message to your API endpoint
      // this.http.post('http://localhost:3000/message', { message: this.userMessage })
      //   .subscribe(response => {
      //     // Handle the response from your API here
      //     console.log('Response from API:', response);
          
          // Add the user message to the chat list
          this.chatService.addChat({ text: this.userMessage, sender: 'user' });
          
          // Optionally, clear the input field
          this.userMessage = '';
        // }, error => {
        //   console.error('Error sending message:', error);
        // });
    }
  }
}
