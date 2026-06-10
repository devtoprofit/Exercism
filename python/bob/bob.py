"""Function to determine what Bob will reply to someone
when they say something to him or ask him a question.
"""


def response(hey_bob: str) -> str:
    """Determine what Bob will reply to someone.

    Args:
        hey_bob (str): Narration or a question to Bob.
    """
    speech = hey_bob.strip()

    if speech.isupper() and speech.endswith("?"):
        reply = "Calm down, I know what I'm doing!"
    elif speech.isupper():
        reply = "Whoa, chill out!"
    elif speech.endswith("?"):
        reply = "Sure."
    elif speech == "":
        reply = "Fine. Be that way!"
    else:
        reply = "Whatever."
    
    return reply
