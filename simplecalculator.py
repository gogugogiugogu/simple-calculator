while True:
    expr = input("Enter calculation (or 'q' to quit): ").strip()
    if expr.lower() == "q":
        break
    try:
        result = eval(expr, {"__builtins__": None}, {})
        print("Result:", result)
    except Exception as e:
        print("Error:", e)