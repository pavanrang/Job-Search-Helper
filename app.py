import dash
from dash import Dash, html, dcc, Input, Output, State, callback_context
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage, AIMessage

load_dotenv()

app = Dash(__name__, external_stylesheets=['https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css'])
chat = ChatGroq(temperature=0, model_name="llama3-70b-8192")
messages = [SystemMessage(content="Hi! I am your friendly Job Search Helper. Please provide your resume.")]

app.layout = html.Div(
    style={
        'font-family': 'Arial, sans-serif',
        'height': '100vh',
        'display': 'flex',
        'flex-direction': 'column',
        'background-color': '#f5f5f5'
    },
    children=[
        html.H1("Job Search Helper", style={'text-align': 'center', 'margin': '20px 0', 'flex-shrink': '0'}),
        html.Div(id="chat-display", style={'flex-grow': '1', 'background-color': '#fff', 'padding': '20px', 'border-radius': '8px', 'box-shadow': '0 2px 6px rgba(0, 0, 0, 0.1)', 'overflow-y': 'auto'}),
        html.Div(style={'display': 'flex', 'margin': '20px', 'flex-shrink': '0'}, children=[
            dcc.Input(id="user-input", placeholder="Type your message...", style={'flex-grow': '1', 'border-radius': '4px', 'padding': '8px', 'border': '1px solid #ccc'}),
            html.Button("Send", id="send-button", n_clicks=0, style={'margin-left': '10px', 'background-color': '#4CAF50', 'color': '#fff', 'border': 'none', 'border-radius': '4px', 'padding': '8px 16px', 'cursor': 'pointer'})
        ])
    ]
)

@app.callback(
    Output("chat-display", "children"),
    Input("send-button", "n_clicks"),
    State("user-input", "value")
)
def update_chat(n_clicks, user_input):
    global messages
    if n_clicks > 0 and user_input:
        messages.append(HumanMessage(content=user_input))

        if "resume" in user_input.lower():
            messages.append(AIMessage(content="I have received your resume. Can you now provide the job description for the role you are applying to?"))
        elif "job description" in user_input.lower():
            messages.append(AIMessage(content="I have received the job description. Here's how you can improve your resume... Do you want to have a mock interview?"))
        elif "yes" in user_input.lower():
            messages.append(AIMessage(content="Great! Let's start the mock interview. Here's the first question..."))
        else:
            response = chat(messages)
            messages.append(AIMessage(content=response.content))

    chat_display = [
        html.Div([
            html.Span(f"{message.type.capitalize()}: {message.content}", style={'display': 'block', 'padding': '10px', 'border-radius': '8px', 'background-color': '#f5f5f5' if message.type == 'human' else '#e6f7ff', 'margin-bottom': '10px'})
        ])
        for message in messages
    ]

    return chat_display

@app.callback(
    Output("user-input", "value"),
    Input("user-input", "n_submit"),
    State("user-input", "value")
)
def handle_enter_key(n_submit, user_input):
    if n_submit:
        update_chat(0, user_input)
        return ""
    return user_input

if __name__ == "__main__":
    app.run_server(debug=True)
