from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from dotenv import load_dotenv

load_dotenv()

def generate_training_program(exercise_type, difficulty, api_key):
    llm = ChatOpenAI(api_key=api_key, temperature=0.5)

    prompt_template_program = PromptTemplate(
        input_variables=['exercise_type', 'difficulty'],
        template="I want to create a training program for {exercise_type}. The program should be {difficulty}."
    )

    program_chain = LLMChain(llm=llm, prompt=prompt_template_program, output_key="training_program")

    response = program_chain.invoke({'exercise_type': exercise_type, 'difficulty': difficulty})
    return response