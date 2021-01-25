import hackchat
import sys
import time
if __name__ == '__main__':
    def greet(chat, sender, *others):
        bot.send_message(f'Welcome to //{server}//! {sender}')
        print(f'[{server}] {sender} is now online')
        return


    def log(chat, sender, *others):
        print(f'[{server}] {sender} is now offline')
        return


    def listener(chat, message, sender):
        if message[0] != '=':
            print(f'[{server}] {sender} sent message://{message}')
        else:
            return

    def commands(chat, message, sender, *others):
        if message[0] == '=':
            print(f'{sender} attempted to issue command://{message}')
            if message[:8] == '=silence':
                try:
                    time.sleep(float(message[9:]))
                    bot.send_message(f'{nick} is online again!')
                    print()
                except ValueError:
                    bot.send_message('ValueError, please send a valid number')
                    print('Command Execution Failed: ValueError')
                    return
            elif message == '=help':
                bot.send_message('''
==========Commands List==========
=help: Print a list of help
=silence [n]: Silence the bot for [n] seconds''')


    server = input("Connect to hack.chat/?:")
    nick = input("Log in as?:")
    bot = hackchat.HackChat(nick, server)
    print("Connection Established")
    bot.on_join += [greet]
    bot.on_leave += [log]
    bot.on_message += [listener, commands]
    bot.run()

