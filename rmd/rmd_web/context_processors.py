# context_processors.py

def user_context(request):
    # Add 'user' to the context if available
    return {'user': request.user}
