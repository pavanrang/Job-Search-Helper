# Job Search Helper - Chat Interface

This repository contains code for a web-based Job Search Helper application with a chat interface. The application allows users to interact with a virtual assistant to receive assistance in their job search process, including resume improvement suggestions, mock interviews, and more.

## Workflow

1. **User Interaction**: Users interact with the application through a chat interface. They can type messages into the input box provided and click the send button to submit their messages.

2. **Message Processing**: When a user sends a message, it triggers the `update_chat` function. This function processes the user's message, determines the appropriate response based on the message content, and adds it to the chat display.

3. **Response Generation**: Responses are generated based on the user's input using the `ChatGroq` model. The model provides tailored responses to user queries regarding resumes, job descriptions, mock interviews, and other job search-related topics.

4. **Display Update**: After processing the user's message and generating a response, the chat display is updated to show the conversation history, including both user messages and responses from the virtual assistant.

5. **Mock Interviews**: If the user expresses interest in a mock interview by responding positively to the assistant's prompt, the assistant initiates the mock interview process by asking interview questions.

## How it Works

- **Layout**: The application layout is built using Dash, a Python web framework. It consists of a header displaying the application title, a chat display area to show the conversation history, and an input box for users to type messages.

- **Message Handling**: User messages are processed in real-time using callback functions. The `update_chat` function handles user input, determines the appropriate response, and updates the chat display accordingly.

- **Response Generation**: Responses are generated using the `ChatGroq` model, which utilizes natural language processing techniques to provide contextually relevant responses based on user queries.

- **Mock Interviews**: The assistant offers mock interviews to users who express interest. It asks interview questions and guides users through the interview process, providing feedback and suggestions along the way.

This is a timepass weekend project, Keep that in mind and excuse if there are any errors
