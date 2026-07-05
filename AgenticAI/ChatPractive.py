from langgraph.graph import StateGraph , START , END 
from typing import TypedDict , Annotated
from langchain_groq import ChatGroq
from langchain_core.message import BaseMessage , HumanMessage , AIMessage  
from langgraph.message import add_messages


class ChatState(TypedDict):
    messages : Annotated(list[BaseMessage] , add_messages)

llm  = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

def chatNode (state : ChatState) : 
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

graph = StateGraph(ChatState) 
graph.add_node('chat' , chatNode)


graph.add_edge(START , 'chat')
graph.add_edge('chat' , END)

app = graph.compile()
app.invoke('Hello , my name is Anant')
