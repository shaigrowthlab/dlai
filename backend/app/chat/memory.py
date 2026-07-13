from collections import defaultdict

# In-memory conversation storage
# Later we'll move this to Redis or PostgreSQL.

_conversations = defaultdict(list)


def add_message(session_id: str, role: str, content: str):
    _conversations[session_id].append(
        {
            "role": role,
            "content": content,
        }
    )


def get_messages(session_id: str):
    return _conversations[session_id]


def clear_messages(session_id: str):
    _conversations.pop(session_id, None)