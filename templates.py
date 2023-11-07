ZERO_SHOT_CLF_PROMPT_TEMPLATE = """
You will be provided with the following information:
1. An arbitrary text sample. The sample is delimited with triple backticks.
2. List of categories the text sample can be assigned to. The list is delimited with square brackets. The categories in the list are enclosed in the single quotes and comma separated.

Perform the following tasks:
1. Identify to which category the provided text belongs to with the highest probability.
2. Assign the provided text to that category.
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the assigned category. Do not provide any additional information except the JSON.

List of categories: {labels}

Text sample: ```{x}```

Your JSON response:
"""

FEW_SHOT_CLF_PROMPT_TEMPLATE = """
You will be provided with the following information:
1. An arbitrary text sample. The sample is delimited with triple backticks.
2. List of categories the text sample can be assigned to. The list is delimited with square brackets. The categories in the list are enclosed in the single quotes and comma separated.
3. Examples of text samples and their assigned categories. The examples are delimited with triple backticks. The assigned categories are enclosed in a list-like structure. These examples are to be used as training data.

Perform the following tasks:
1. Identify to which category the provided text belongs to with the highest probability.
2. Assign the provided text to that category.
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the assigned category. Do not provide any additional information except the JSON.

List of categories: {labels}

Training data:
{training_data}

Text sample: ```{x}```

Your JSON response:
"""

FEW_SHOT_MLCLF_PROMPT_TEMPLATE = """
You will be provided with the following information:
1. An arbitrary text sample. The sample is delimited with triple backticks.
2. List of categories the text sample can be assigned to. The list is delimited with square brackets. The categories in the list are enclosed in the single quotes and comma separated.
3. Examples of text samples and their assigned categories. The examples are delimited with triple backticks. The assigned categories are enclosed in a list-like structure. These examples are to be used as training data.
4. Description of each category label, which should be consulted when making the classifications.

Perform the following tasks:
1. Identify to which category the provided text belongs to with the highest probability, please refer to the category descriptions.
2. Assign the text sample to at least 1 but up to {max_cats} categories based on the probabilities.
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the array of assigned categories. Do not provide any additional information except the JSON.

List of categories: {labels}

Description of categories:
1. problem identification and resolution: Issues potentially impacting safety are promptly identified, fully evaluated, and promptly addressed and corrected commensurate with their significance.
2. work processes: The process of planning and controlling work activities is implemented so that safety is maintained.
3. questioning attitude: Individuals avoid complacency and continuously challenge existing conditions and activities in order to identify discrepancies that might result in error or inappropriate action.
4. continuous learning: Opportunities to learn about ways to ensure safety are sought out and implemented.
5. personal accountability: All individuals take personal responsibility for safety.
6. respectful work environment: Trust and respect permeate the organization.
7. decision making: Decisions that support or affect nuclear safety are systematic, rigorous, and thorough.
8. leadership safety values and actions: Leaders demonstrate a commitment to safety in their decisions and behaviors.
9. effective safety communication: Communications maintain a focus on safety.
10. environment for raising concerns: A safety- conscious work environment (SCWE) is maintained where personnel feel free to raise safety concerns without fear of retaliation, intimidation, harassment, or discrimination.

Training data:
{training_data}

Text sample: ```{x}```

Your JSON response:
"""

ZERO_SHOT_MLCLF_PROMPT_TEMPLATE = """
You will be provided with the following information:
1. An arbitrary text sample. The sample is delimited with triple backticks.
2. List of categories the text sample can be assigned to. The list is delimited with square brackets. The categories in the list are enclosed in the single quotes and comma separated. The text sample belongs to at least one category but cannot exceed {max_cats}.
3. Description of each category label, which should be used when making the classification.

Perform the following tasks:
1. Identify to which categories the provided text belongs to with the highest probability, please refer to the category descriptions.
2. Assign the text sample to at least 1 but up to {max_cats} categories based on the probabilities.
3. Provide your response in a JSON format containing a single key `label` and a value corresponding to the array of assigned categories. Do not provide any additional information except the JSON.

List of categories: {labels}

Description of categories:
1. problem identification and resolution: Issues are promptly identified, addressed, and resolved. Identification and resolution of a broad spectrum of problems, including organizational issues. The organization takes effective corrective actions to address issues in a timely manner. Trends in safety performance indicators are acted on.
2. work processes: Work activities are properly planned, controlled, and implemented in order to ensure safety. The organization operates and maintains equipment within design margins. Individuals follow processes, procedures, and work instructions.
3. questioning attitude: Individuals avoid complacency and challenge existing conditions and activities in order to identify discrepancies that might result in error or inappropriate action. All employees are watchful for assumptions, anomalies, values, conditions, or activities that can have an undesirable effect on plant safety.
4. continuous learning: Employees must continuously learn to ensure safety. Operating experience is highly valued, and the capacity to learn from experience is well developed. The organization provides training and ensures knowledge transfer.
5. personal accountability: Individuals must take personal responsibility for safety. Individuals understand the importance of adherence to nuclear standards. Individuals and work groups communicate and coordinate their activities within and across organizational boundaries.
6. respectful work environment: The work environment should be full of trust and respect through timely and accurate communication. Employee concerns shall be addressed.
7. decision making: Decisions must be systematic, rigorous, and thorough in order to ensure safety. Senior leaders support and reinforce conservative decisions.
8. leadership safety values and actions: Leaders must demonstrate commitment to safety in their decisions and behaviors. Corporate policies emphasize the overriding importance of nuclear safety. Leaders ensure that personnel, equipment, procedures, and other resources are available and adequate. Leaders use a systematic process for evaluating and implementing change.
9. effective safety communication: Leaders and workers must communicate the importance of safety. Leaders ensure that the bases for operational and organizational decisions are communicated in a timely manner.
10. environment for raising concerns: Employees must feel free to raise concerns and should be promptly addressed. Environment does not tolerate harassment, intimidation, retaliation, or discrimination.

Text sample: ```{x}```

Your JSON response:
"""
    
SUMMARY_PROMPT_TEMPLATE = """
Your task is to generate a summary of the text sample.
Summarize the text sample provided below, delimited by triple backticks, in at most {max_words} words.

Text sample: ```{x}```
Summarized text:
"""

FOCUSED_SUMMARY_PROMPT_TEMPLATE = """
As an input you will receive:
1. A focus parameter delimited with square brackets.
2. A single text sample delimited with triple backticks.

Perform the following actions:
1. Determine whether there is something in the text that matches focus. Do not output anything.
2. Summarise the text in at most {max_words} words.
3. If possible, make the summarisation focused on the concept provided in the focus parameter. Otherwise, provide a general summarisation. Do not state that general summary is provided.
4. Do not output anything except of the summary. Do not output any text that was not present in the original text.
5. If no focused summary possible, or the mentioned concept is not present in the text, output "Mentioned concept is not present in the text." and the general summary. Do not state that general summary is provided.

Focus: [{focus}]

Text sample: ```{x}```

Summarized text:
"""

TRANSLATION_PROMPT_TEMPLATE = """
If the original text, delimited by triple backticks, is already in {output_language} language, output the original text.
Otherwise, translate the original text, delimited by triple backticks, to {output_language} language, and output the translated text only. Do not output any additional information except the translated text.

Original text: ```{x}```
Output:
"""
