import google.generativeai as palm

def configure_api(api_key):
    palm.configure(api_key=api_key)

def generate_answer(model_name, question):
    try:
        # Use text-bison-001 model directly
        model = "models/text-bison-001"
            
        # Create the prompt
        prompt = f"Hey AI, give me an answer to this question: {question} in maximum 500 words."
        
        # Generate response
        response = palm.generate_text(
            model=model,
            prompt=prompt,
            temperature=0.7,
            max_output_tokens=800
        )
        
        return response.result
    except Exception as e:
        raise ValueError(f"Error generating response: {str(e)}")