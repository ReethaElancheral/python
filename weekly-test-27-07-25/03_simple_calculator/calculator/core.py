def evaluate_expression(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception as e:
        return f"Error: {str(e)}"
