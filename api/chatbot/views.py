from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import FAQ
from difflib import get_close_matches
from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch

# Path to the fine-tuned model checkpoint
model_name = "microsoft/DialoGPT-medium"

# Initialize model and tokenizer
try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
except Exception as e:
    model = None
    print(f"Error initializing fine-tuned model: {e}")

class ChatbotResponseAPIView(APIView):
    """
    A class-based view for handling chatbot queries. It first checks the FAQ database for an answer.
    If no match is found, it generates a response using a fine-tuned model.
    """

    def get(self, request, *args, **kwargs):
        # Retrieve the user query
        query = request.query_params.get("query", "").strip()

        # Validate query presence
        if not query:
            return self.handle_error(
                "Query parameter is required.",
                status.HTTP_400_BAD_REQUEST,
            )

        # Check if the query exists in the FAQ database
        faq_response = self.get_faq_response(query)
        if faq_response:
            return self.handle_success(faq_response)

        # Fallback to the fine-tuned model for queries not found in the FAQ database
        if model:
            return self.generate_response_with_fine_tuned_model(query)

        # If model is not available
        return self.handle_error(
            "Fine-tuned model is not available at the moment.",
            status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    def get_faq_response(self, query):
        """
        Retrieves an FAQ response based on the closest matching question.
        """
        # Get all questions from the FAQ database
        faqs = FAQ.objects.all()
        questions = [faq.question for faq in faqs]

        # Find the closest match from the FAQ list
        match = get_close_matches(query, questions, n=1, cutoff=0.6)

        if match:
            faq = faqs.get(question=match[0])
            return {faq.answer}
        else:
            return None

    def generate_response_with_fine_tuned_model(self, query):
        """
        Generates a text response using the fine-tuned model if no FAQ match is found.
        """
        try:
            # Clear CUDA memory before generating a response
            # torch.cuda.empty_cache()

            # Prepend context to the query for a better conversational response (optional)
            context = "You: " + query + "\nAI:"

            # Tokenize the input query
            inputs = tokenizer.encode(context + tokenizer.eos_token, return_tensors="pt").cuda()

            # Generate a response from the model
            outputs = model.generate(inputs, 
                                    max_length=150,  # Increase max_length for longer responses
                                    pad_token_id=tokenizer.eos_token_id, 
                                    do_sample=True, 
                                    top_k=50, 
                                    top_p=0.9,  # Use a slightly higher value for top_p for better diversity
                                    temperature=0.7,  # You can experiment with this to adjust randomness
                                    num_return_sequences=1)  # Return only 1 sequence

            # Decode the response
            response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

            # Extract the part after "AI:" from the generated response
            ai_response = response_text.split("AI:")[1].strip() if "AI:" in response_text else response_text.strip()

            # Return the generated response (only the part after "AI:")
            return self.handle_success(ai_response)

        # except torch.cuda.OutOfMemoryError:
        #     return self.handle_error(
        #         "CUDA out of memory. Please try again later or use a smaller query.",
        #         status.HTTP_500_INTERNAL_SERVER_ERROR,
        #     )
        except Exception as e:
            return self.handle_error(
                f"Fine-tuned model error: {str(e)}", status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def handle_error(self, message, status_code):
        """
        Helper method to handle error responses.
        """
        return Response({"error": message}, status=status_code)

    def handle_success(self, response):
        """
        Helper method to handle successful responses.
        """
        return Response({"response": response}, status=status.HTTP_200_OK)
