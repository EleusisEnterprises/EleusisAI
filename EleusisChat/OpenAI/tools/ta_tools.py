import pandas as pd
import pandas_ta as ta

def calculate_technical_indicators(df):
    # Calculate Moving Averages based on your specified lengths
    df['ema_short'] = ta.ema(df['close'], length=9)
    df['ema_medium'] = ta.ema(df['close'], length=21)
    df['ema_long'] = ta.ema(df['close'], length=55)

    # Calculate the Stochastic Oscillator with your settings (13, 6, 3)
    stoch = ta.stoch(df['high'], df['low'], df['close'], k=13, d=6, smooth_k=3)
    df['stoch_k'] = stoch['STOCHk_13_6_3']
    df['stoch_d'] = stoch['STOCHd_13_6_3']

    return df

def generate_analysis_prompt(df):
    # Create a prompt based on the technical indicators calculated
    prompt = "Analyze the following stock market data with detected indicators:\n"
    
    # Include a brief summary of the technical indicators
    prompt += f"EMA Short (9): {df['ema_short'].iloc[-1]:.2f}\n"
    prompt += f"EMA Medium (21): {df['ema_medium'].iloc[-1]:.2f}\n"
    prompt += f"EMA Long (55): {df['ema_long'].iloc[-1]:.2f}\n"
    prompt += f"Stochastic %K (13, 6, 3): {df['stoch_k'].iloc[-1]:.2f}\n"
    prompt += f"Stochastic %D (13, 6, 3): {df['stoch_d'].iloc[-1]:.2f}\n"
    
    # Add more detailed data if needed
    prompt += "\nHere's the recent price data:\n"
    prompt += df.to_string(index=False)
    
    return prompt
