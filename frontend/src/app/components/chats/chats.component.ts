import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; // Import CommonModule

// import { HlmInputDirective } from '@spartan-ng/ui-input-helm';
import { MessageComponent } from '../message/message.component';

import { ChatService } from '../../services/chat.service';

@Component({
  selector: 'app-chats',
  standalone: true,
  imports: [CommonModule, MessageComponent],
  templateUrl: './chats.component.html',
  styleUrl: './chats.component.css'
})
export class ChatsComponent {
  chats : { text: string, sender: string }[] = [
    { text: 'Hello, how can I assist you today?', sender: 'ai' },
    { text: 'Can you help me with my project?', sender: 'user' },
    { text: 'Sure, what would you like help with?', sender: 'ai' },
    { text: 'I need help with Angular and UI design.', sender: 'user' }
  ];

  constructor(private chatService: ChatService) {}

  ngOnInit() {
    // Load initial chats
    this.chatService.loadInitialChats(this.chats);

    // Subscribe to new chats
    this.chatService.chats$.subscribe(chats => {
      this.chats = chats;
    });
  }
}
