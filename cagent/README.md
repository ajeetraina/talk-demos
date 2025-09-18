## Getting Started

## Prereq

- Install Docker Desktop
- Install cagent


## Export keys

```
export ANTHROPIC_API_KEY=your_api_key_here  # first choice. default model claude-sonnet-4-0
export OPENAI_API_KEY=your_api_key_here     # if anthropic key not set. default model gpt-5-mini
export GOOGLE_API_KEY=your_api_key_here     # if anthropic and openai keys are not set. default model gemini-2.5-flash
```

## Getting Started

```
cagent new
```

It will pick up GPT-5-mini by default if you've provided OpenAI API Key

```
> Cafe management system
```

It creates [this](https://github.com/ajeetraina/talk-demos/blob/main/cagent/cafe_management_system.yaml) file.

It ask you further:

```
Next steps:
- Tell me any specific preferences (tech stack choices, must-have integrations like Square/Stripe, expected scale, offline support, or deployment target) and I'll have the root agent start by asking clarifying questions and producing a project plan."
```

```
cagent run cafe_management_system.yaml
```

Now type the follow prompt

```
Please build a complete cafe management system for Rameshwaram Cafe:

BUSINESS CONTEXT:
- Traditional South Indian restaurant in Rameshwaram  
- Serves dosas, idli, vada, filter coffee, traditional meals
- 50 seats, 200 orders/day during peak season
- Staff: 2 cashiers, 3 cooks, 1 manager

TECHNICAL REQUIREMENTS:
- Tech stack: Python backend, React frontend
- Payment: UPI (GPay/PhonePe), cash, credit cards
- Must work offline (frequent power outages)
- Local server + cloud backup architecture
- Integration with kitchen display screens

SPECIAL FEATURES:
- Multi-language: English + Tamil interface
- Allergen tracking (nuts, dairy, etc.)
- Customer loyalty points system  
- Inventory management with auto-reordering
- Staff scheduling and payroll
- Sales analytics and reporting

TARGET DEPLOYMENT:
- Local server in restaurant
- Cloud backup on AWS/Google Cloud
- Mobile app for managers
- Tablet-based POS terminals"
```





