Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> 
... def chatbot():
...     print("Chatbot: Hello! Type 'bye' to exit.")
... 
...     while True:
...         user = input("You: ").lower()
... 
...         if user == "hello":
...             print("Chatbot: Hi!")
... 
...         elif user == "how are you":
...             print("Chatbot: I'm fine, thanks!")
... 
...         elif user == "what is your name":
...             print("Chatbot: I am a simple chatbot.")
... 
...         elif user == "bye":
...             print("Chatbot: Goodbye!")
...             break
... 
...         else:
...             print("Chatbot: Sorry, I don't understand.")
... 
