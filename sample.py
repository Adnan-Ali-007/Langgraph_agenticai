from typing_extensions import TypedDict

class State(TypedDict):
    graph_info: str

def start_play(state: State):
    print("start playing")
    return {"graph_info": state["graph_info"] + " I am planning to play"}

def cricket(state: State):
    print("start cricket")
    return {"graph_info": state["graph_info"] + " fuck cricket"}

def badminton(state: State):
    print("start badminton")
    return {"graph_info": state["graph_info"] + " fuck badminton"}

import random
from typing import Literal

def random_play(state: State) -> Literal['cricket', 'badminton']:
    if random.random() > 0.5:  # Fixed: Now 50/50 chance
        return "cricket"
    else:
        return "badminton"

from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END

graph = StateGraph(State)
graph.add_node("start_play", start_play)
graph.add_node("cricket", cricket)
graph.add_node("badminton", badminton)

# Flow of graph
graph.add_edge(START, "start_play")
graph.add_conditional_edges("start_play", random_play)
graph.add_edge("cricket", END)
graph.add_edge("badminton", END)

# Compile the graph
graph_builder = graph.compile()

# View the graph (displays a flowchart image in Jupyter)
display(Image(graph_builder.get_graph().draw_mermaid_png()))

# Invoke and print result
result = graph_builder.invoke({"graph_info": "My name is Adnan"})
print("Final state:", result)