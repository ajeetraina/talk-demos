
## Demo for OpenAI 

Export the OpenAI Key from https://gist.github.com/ajeetraina/b3608bc6b4c12ba4fd5e8f1395f05f3a

```
export OPENAI_API_KEY=sk-proj-XXX
```

```
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
```

```
{
  "id": "chatcmpl-BXVPNwvDCifzGUk9c5FIyEGXOtUGP",
  "object": "chat.completion",
  "created": 1747325257,
  "model": "gpt-4o-2024-08-06",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you today?",
        "refusal": null,
        "annotations": []
      },
      "logprobs": null,
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 19,
    "completion_tokens": 10,
    "total_tokens": 29,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
    }
  },
  "service_tier": "default",
  "system_fingerprint": "fp_d8864f8b6b"
}
```


Congrats! You've successfully made the API call to OpenAI's Chat Completions endpoint with GPT-4o. The response shows:

- You received a standard greeting response: "Hello! How can I assist you today?"
- The model used was gpt-4o-2024-08-06
- Token usage breakdown:

   - 19 prompt tokens
   - 10 completion tokens
   - 29 total tokens


The request completed normally (finish_reason: "stop")

This is exactly what you'd expect from a successful API call. 
The JSON structure contains all the standard fields in an OpenAI completion response, including the unique completion ID, usage statistics, and service tier information.
