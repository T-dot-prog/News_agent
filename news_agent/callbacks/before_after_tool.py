from datetime import datetime
from typing import Optional, Dict, Any
from google.genai import types
from google.adk.tools import BaseTool
from google.adk.tools.tool_context import ToolContext


def before_tool_callback(tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext) -> Optional[types.Content]:
    # get the tool name 
    tool_name = tool.name

    print(f'[CALLBACK] Tool Called: {tool_name}')
    print(f'[CALLBACK] Original arguments: {args}')

    if tool_name == "google_search":
        # Get the search query
        search_query = args.get("query", "").lower()
        
        # List of restricted topics
        restricted_topics = [
            "porn", "pornography", "adult content",
            "bully", "bullying", "harassment",
            "explicit", "nsfw"
        ]
        
        # Check if query contains restricted topics
        for topic in restricted_topics:
            if topic in search_query:
                print(f'[CALLBACK] Blocked search containing restricted topic: {topic}')
                return types.Content(
                    text="I apologize, but I cannot search for that type of content. Please try a different search query."
                )
        
        # If query passes checks, proceed with search
        print(f'[CALLBACK] Executing Google Search for: {search_query}')
        timestamp = datetime.now()
        print(f'[CALLBACK] Search initiated at: {timestamp.strftime("%Y-%m-%d %H:%M:%S")}')
        return None

def after_tool_callback(tool: BaseTool, args: Dict[str, Any], tool_context: ToolContext) -> Optional[types.Content]:
    # Get the tool name
    tool_name = tool.name
    
    # Get the search query from args
    search_query = args.get("query", "")
    
    # Get the current timestamp
    timestamp = datetime.now()
    
    if tool_name == "google_search":
        # Log the completion of the search
        print(f'[CALLBACK] Google Search completed for: {search_query}')
        print(f'[CALLBACK] Search completed at: {timestamp.strftime("%Y-%m-%d %H:%M:%S")}')
        
        # Extract user's topic of interest from the search query
        # This could be used for future personalization or recommendations
        user_topic = search_query.split()[0] if search_query else "general"
        print(f'[CALLBACK] User interested in topic: {user_topic}')
        
        # Store the user's topic in the tool context for future reference
        if not hasattr(tool_context, 'user_topics'):
            tool_context.user_topics = []
        tool_context.user_topics.append(user_topic)
        
        # Log the user's topic history
        print(f'[CALLBACK] User topic history: {tool_context.user_topics}')
        
