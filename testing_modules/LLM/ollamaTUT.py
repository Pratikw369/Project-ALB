import ollama

response = ollama.generate(
    model='llama3',
    prompt='Explain ROS2 in simple terms.'
)

print(response['response'])
