import logging
from langchain.chains import SimpleSequentialChain
from langchain.llms import OpenAI
import pandas as pd
import pandas_ta as ta
from tools.data_extraction import extract_data_from_image, extract_additional_data
from tools.ta_tools import calculate_technical_indicators, generate_analysis_prompt
import os

# Set up logging with a distinct logger name to avoid conflicts
app_logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Set up OpenAI API key for the model
openai_api_key = os.getenv("OPENAI_API_KEY")

# Initialize the language model with the correct parameters
llm = OpenAI(model_kwargs={"api_key": openai_api_key, "model": "gpt-4"})

def create_analysis_chain():
    # Step 1: Interpret the Image Data
    def interpret_image_step(image_path):
        app_logger.info(f"Interpreting image: {image_path}")
        df = extract_data_from_image(image_path)
        app_logger.info(f"Extracted DataFrame: {df}")
        
        additional_data = extract_additional_data(image_path)
        app_logger.info(f"Extracted additional data: {additional_data}")
        
        combined_df = pd.concat([df, additional_data], ignore_index=True)
        app_logger.info(f"Combined DataFrame: {combined_df}")
        return combined_df

    # Step 2: Perform Technical Analysis
    def technical_analysis_step(df):
        app_logger.info(f"Performing technical analysis on DataFrame: {df}")
        df = calculate_technical_indicators(df)
        prompt = generate_analysis_prompt(df)
        app_logger.info(f"Generated prompt: {prompt}")
        return prompt

    # Step 3: Generate the Response Iteratively
    def generate_response_step(prompt):
        app_logger.info(f"Sending prompt to OpenAI: {prompt}")
        responses = []
        try:
            while prompt:
                response = llm(prompt)
                
                # Add logging to inspect the response structure
                app_logger.info(f"Received response: {response}")
                
                if response and isinstance(response, dict) and 'choices' in response and response['choices']:
                    content = response['choices'][0]['message']['content']
                    responses.append(content)
                    app_logger.info(f"Generated content: {content}")
                    
                    # Check if more analysis is needed (for example, if the content suggests further analysis)
                    prompt = generate_follow_up_prompt(content)
                else:
                    app_logger.error(f"Unexpected response structure: {response}")
                    raise ValueError("Failed to generate response: unexpected structure in response from OpenAI.")
            return "\n".join(responses)
        
        except Exception as e:
            app_logger.error(f"Exception while generating response: {e}")
            raise

    # Set up the chain
    chain = SimpleSequentialChain(
        steps=[
            {"input": "image_path", "output": "df", "function": interpret_image_step},
            {"input": "df", "output": "prompt", "function": technical_analysis_step},
            {"input": "prompt", "output": "response", "function": generate_response_step},
        ]
    )

    return chain

def generate_follow_up_prompt(content):
    # Implement logic to determine if further analysis is needed
    if "further analysis needed" in content:
        return "Please provide more details about the technical indicators mentioned."
    return None
