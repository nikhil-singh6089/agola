import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ChatService {
  private chatsSubject = new BehaviorSubject<{ text: string, sender: string }[]>([]);
  chats$ = this.chatsSubject.asObservable();

  loadInitialChats(chats: { text: string, sender: string }[]) {
    chats.forEach(chat => {
      const currentChats = this.chatsSubject.getValue();
      this.chatsSubject.next([...currentChats, chat]);
    });
  }

  addChat(chat: { text: string, sender: string }) {
    const currentChats = this.chatsSubject.getValue();
    this.chatsSubject.next([...currentChats, chat]);
  }
}
