from datetime import datetime
from google.adk.agents.callback_context import CallbackContext
from typing import Optional
from google.genai import types


def before_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:

    # get the current state
    state = callback_context.state

    # record the timestamp
    timestamp = datetime.now()

    if "agent_name" not in state:
        state["agent_name"] = "NewsAgent"
    
    if "request_counter" not in state:
        state["request_counter"] = 1
    
    else:
        state["request_counter"] += 1

    #update the request start time 
    state["request_start_time"] = timestamp

    print("==AGENT EXECUTED COMPLETED==")
    print(f"Request #: {state['request_counter']}")
    print(f"Timestamp: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

    # Print to console
    print(f"\n[BEFORE CALLBACK] Agent processing request #{state['request_counter']}")

    return None

def after_agent_callback(callback_context: CallbackContext) -> Optional[types.Content]:

    # get the curernt state 
    state = callback_context.state

    timestamp = datetime.now()
    duration = None
    if "request_start_time" in state:
        duration = (timestamp - state["request_start_time"]).total_seconds()

    # Log the completion
    print("=== AGENT EXECUTION COMPLETED ===")
    print(f"Request #: {state.get('request_counter', 'Unknown')}")
    if duration is not None:
        print(f"Duration: {duration:.2f} seconds")

    # Print to console
    print(
        f"[AFTER CALLBACK] Agent completed request #{state.get('request_counter', 'Unknown')}"
    )
    if duration is not None:
        print(f"[AFTER CALLBACK] Processing took {duration:.2f} seconds")

    return None


