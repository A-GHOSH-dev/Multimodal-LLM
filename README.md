# QUERYMINTAI- Powered by LLM, GenAI And Web Scraping

# Abstract:
The project aims to develop a versatile and powerful Chatbot Software, seamlessly integrating Large Language Models (LLMs), GenerativeAI, Web Scraping powered by Langchain OpenAI, and Python with Streamlit. This Chatbot is designed to cater to a wide audience, including equity researchers, scholars, and data professionals across various domains.
The key features of the Chatbot include:
- Chat with Your Documents: Users can upload PDFs, Word documents, TXT files, or CSVs, effectively turning them into interactive databases. The Chatbot employs LLMs to understand natural language queries, extracting pertinent information from the uploaded documents and providing precise answers.
- Equity Research Analysis ChatBot: Tailored for equity researchers, this feature allows users to input URLs or news links. The Chatbot utilizes advanced web scraping techniques and harnesses the power of LLMs to extract relevant information from the target links. Users can then pose natural language questions, receiving accurate answers based on the analyzed data.
- Chat with Databases: The Chatbot facilitates interaction with SQL databases, interpreting natural language queries into equivalent SQL statements. Users can seamlessly retrieve data from database tables, eliminating the need for explicit SQL knowledge. This feature streamlines the data extraction process, providing a user-friendly interface for querying databases.

The project not only addresses the need for efficient data extraction but also enhances user experience by fostering a conversational interface. The integration of LLMs ensures a more intuitive and natural interaction, making the Chatbot a valuable tool for researchers, data engineers, and professionals dealing with diverse data sources. The Streamlit-powered interface adds a layer of accessibility and simplicity, making the Chatbot an indispensable resource for anyone seeking actionable insights from a variety of data formats and sources.

# Problem Statement:
In the rapidly evolving landscape of information extraction and user interaction, individuals across various domains face challenges in efficiently and intuitively accessing valuable insights from diverse data sources. Existing tools often lack the synergy needed for seamless document interaction, equity research analysis, and database querying in a conversational manner. There is a need for a comprehensive, user-friendly solution that combines the power of Large Language Models (LLMs), advanced web scraping, and a streamlined interface, catering to researchers, scholars, and data professionals.

# Introduction:
In response to the challenges posed by conventional tools, our project aims to introduce a groundbreaking Chatbot Software that seamlessly integrates three powerful components: LLMs, Web Scraping with Langchain OpenAI, and a Python-powered Streamlit interface. The application is designed to be a versatile tool for individuals engaged in equity research, scholarly pursuits, and data engineering, offering a novel approach to data interaction.

# Novelty:
What sets our application apart from existing solutions like ChatGPT or Gemini AI is the fusion of document-centric chat interactions, equity research analysis through web scraping, and conversational database querying—all within a single, user-friendly platform. Unlike conventional LLM applications, our project not only understands natural language queries but leverages web scraping to extract real-time information from external sources, creating a more dynamic and actionable user experience. The Streamlit-powered interface further distinguishes our application by providing a straightforward and visually appealing platform for users to interact with complex data. By seamlessly integrating these components, our Chatbot Software aims to redefine how users engage with documents, conduct equity research, and interact with databases, offering a more holistic and efficient solution in comparison to existing LLM applications in the market.

# Features:
## Chat with Your Documents 
Users can upload PDFs, Word documents, TXT files, or CSVs, effectively turning them into interactive databases. The Chatbot employs LLMs to understand natural language queries, extracting pertinent information from the uploaded documents and providing precise answers.

![image](https://github.com/A-GHOSH-dev/QueryMintAI/assets/75447439/66bfd55e-3f8c-4875-b8ec-4ebe07e8cb8f)

## Equity Research Analysis ChatBot
Tailored for equity researchers, this feature allows users to input URLs or news links. The Chatbot utilizes advanced web scraping techniques and harnesses the power of LLMs to extract relevant information from the target links. Users can then pose natural language questions, receiving accurate answers based on the analyzed data.

![image](https://github.com/A-GHOSH-dev/QueryMintAI/assets/75447439/0d307c6b-c9d2-4e2c-998a-3f2bba03737e)

## Chat with Databases
The Chatbot facilitates interaction with SQL databases, interpreting natural language queries into equivalent SQL statements. Users can seamlessly retrieve data from database tables, eliminating the need for explicit SQL knowledge. This feature streamlines the data extraction process, providing a user-friendly interface for querying databases.

![image](https://github.com/A-GHOSH-dev/QueryMintAI/assets/75447439/58ad2eaf-cd90-4cef-b48b-03d0ea45e597)

# Literature Review:

![image](https://github.com/A-GHOSH-dev/QueryMintAI/assets/75447439/82722f1f-913d-4136-aa23-167497aa8af1)

1.	Can LLM Already Serve as A Database Interface? A Big Bench for Large-Scale Database Grounded Text-to-SQLs 
•	Challenge Identification: Existing text-to-SQL parsing, demonstrated by GPT-4 and Claude-2, focuses on small-scale databases, leaving a gap between academia and real-world applications.
•	Proposal - BIRD Benchmark: The authors introduce BIRD, a large-scale BIg bench for text-to-SQL tasks, containing 12,751 pairs and 95 databases (33.4 GB) across 37 professional domains. Emphasis is placed on dirty/noisy database values.
•	New Challenges Highlighted: Handling dirty and noisy database values, Addressing external knowledge grounding between natural language (NL) questions and database values, Improving SQL efficiency for massive databases.
•	Key Finding: Text-to-SQL models must incorporate database value comprehension alongside semantic parsing to address the challenges posed by large databases effectively.
•	Execution Accuracy Challenge: Even GPT-4, the most effective model, achieves only 54.89% execution accuracy, significantly lower than the human result of 92.96%. Challenges persist in achieving human-like accuracy.
•	Efficiency Analysis: The paper provides an efficiency analysis, emphasizing the importance of generating text-to-efficient-SQLs for practical industry applications.
•	Contributions: BIRD is positioned as a valuable resource for advancing real-world applications of text-to-SQL research, providing a benchmark that reflects the challenges posed by large-scale databases.

2.	Fine-tuned generative LLM oversampling can improve performance over traditional techniques on multiclass imbalanced text classification
•	Challenge Addressed: The class imbalance problem in classification and data mining, where one class has significantly more samples than another, impacting classifier performance.
•	Resampling Defined: Resampling involves adding (oversampling) or removing (undersampling) samples from a dataset to address class imbalance before training a classifier.
•	Generative LLMs in Focus: Recent advances in generative Large Language Models (LLMs) prompt the proposal of using these models for oversampling imbalanced text data.
•	Research Objective: Systematically compare the effectiveness of generative LLMs for oversampling with traditional resampling methods across multiple domains.
•	Research Findings: Generative LLMs generally outperform traditional methods in imbalanced multiclass classification. Fine-tuned LLM-augmented oversampling improves results in multiclass classification but not in binary classification.
•	Tested Resampling Methods: NO (no resampling), CD (Condensed Nearest Neighbors), BS (Borderline-SMOTE), SM (SMOTE), RO (random oversampling), RU (random undersampling), AU (non-finetuned LLM-augmented oversampling), AF (fine-tuned LLM-augmented oversampling).
•	Performance Increase: Results in binary classification tasks varied with resampling methods. Fine-tuned LLM-augmented oversampling showed improvement in multiclass classification.
•	Statistical Significance: The Cochran Q test uniformly produced p-values of p < 0.001, indicating statistical significance. The Dunn test was also performed and p-values taken.
•	In summary, the research explores the use of generative LLMs for oversampling in addressing the class imbalance problem, demonstrating its effectiveness, particularly in multiclass classification scenarios. The results are systematically compared with traditional resampling methods, providing insights into performance variations across different tasks.

3.	Clinical Text Summarization: Adapting Large Language Models Can Outperform Human Experts
•	Objective: The research addresses the identification and characterization of key events in news streams for analyzing political discourse.
•	Proposed Framework: The authors propose a generic framework for news stream clustering, incorporating temporal trends to extract key events and form document clusters in an unsupervised manner.
•	Datasets and Tasks: The framework is evaluated on six datasets covering four clinical summarization tasks: radiology reports, patient questions, progress notes, and doctor-patient dialogue.
•	Domain Adaptation: Eight large language models (LLMs) are subjected to domain adaptation methods to assess their efficacy in clinical summarization tasks.
•	Quantitative Assessment: Thorough quantitative assessment reveals trade-offs between models and adaptation methods, highlighting cases where recent LLM advances may not improve results.
•	Clinical Reader Study: A clinical reader study involving ten physicians demonstrates that summaries from the best-adapted LLMs outperform human summaries in terms of completeness and correctness.
•	Qualitative Analysis: A qualitative analysis explores strengths and weaknesses of both LLMs and human experts in clinical text summarization.
•	Correlation with NLP Metrics: Traditional quantitative NLP metrics are correlated with reader study scores to enhance understanding of alignment with physician preferences.
•	First Evidence: The research claims to be the first to provide evidence of LLMs outperforming human experts in clinical text summarization across multiple tasks.
•	Practical Implications: Integrating LLMs into clinical workflows is suggested as a means to alleviate documentation burdens, allowing clinicians to focus more on personalized patient care and the human aspects of medicine.

4.	Toward the Automatic Generation of an Objective Function for Extractive Text Summarization
•	The study proposes an innovative method for automatic text summarization (ATS) by employing genetic programming (GP) to automatically generate fitness functions for unsupervised approaches. 
•	The approach involves two main stages: GP generates aptitude functions, and a genetic algorithm (GA) evolves clusters of sentences based on the fitness function. The GP algorithm creates functions considering internal validation indices (Davies Bouldin, Dunn, and Silhouette). These functions act as fitness functions in the evolutionary clustering approach, evaluating the quality of the summaries. 
•	The study aims to establish a correlation between the fitness function and the Rouge measure, which assesses summary quality by comparing it to ideal human-written summaries.
•	The proposed GP algorithm constructs a tree structure representing fitness functions, with operators and operands corresponding to internal validation indices. 
•	The resulting functions are used by the GA to optimize clustering, producing high-quality summaries. 
•	The method is tested on DUC02 and CNN/Daily Mail datasets, achieving competitive results compared to baseline and state-of-the-art approaches in terms of Rouge measures. 
•	The proposed system demonstrates effectiveness in automatically generating fitness functions for clustering-based unsupervised ATS.

5.	Resolving the Imbalance Issue in Hierarchical Disciplinary Topic Inference via LLM-based Data Augmentation
•	Findings: Imbalanced data in Natural Language Processing (NLP) hinders precision in downstream topic models for research proposals submitted during funding applications. Imbalances result from variations in discipline popularity and the rise of interdisciplinary studies.
•	Challenges: Research proposals by experts are complex technological texts with intricate terminologies. Augmenting such specialized text data poses unique challenges.
•	Objective: Leverage large language models (Llama V1) for data augmentation in research proposals within intricate disciplinary hierarchies.
•	Methodology: Sample within the hierarchical structure to identify underrepresented classes. Design a keyword-based prompt for generating research proposals.
•	Addressed Issues: Data imbalance in expert-authored proposals. Compromised fairness in AI-assisted reviewer assignment systems.
•	Approach: Use large language models as data generators for augmenting research proposals. Employ keyword-based prompts for effective research proposal generation.
•	Results: Demonstrated efficacy of generated data in overcoming imbalances. Produced high-quality scientific text data.
•	Significance: Enhances equity in expert assignments. Mitigates imbalances in NLP research proposal datasets.

# References:
1.	Li, J., Hui, B., Qu, G., Yang, J., Li, B., Li, B., ... & Li, Y. (2024). Can llm already serve as a database interface? a big bench for large-scale database grounded text-to-sqls. Advances in Neural Information Processing Systems, 36.
2.	Cloutier, N. A., & Japkowicz, N. (2023, December). Fine-tuned generative LLM oversampling can improve performance over traditional techniques on multiclass imbalanced text classification. In 2023 IEEE International Conference on Big Data (BigData) (pp. 5181-5186). IEEE.
3.	Nakshatri, N. S., Liu, S., Chen, S., Roth, D., Goldwasser, D., & Hopkins, D. (2023, December). Using llm for improving key event discovery: Temporal-guided news stream clustering with event summaries. In The 2023 Conference on Empirical Methods in Natural Language Processing.
4.	Hernández-Castañeda, Á., García-Hernández, R. A., & Ledeneva, Y. (2023). Towards the automatic generation of an objective function for extractive text summarization. IEEE Access.
5.	Cai, X., Xiao, M., Ning, Z., & Zhou, Y. (2023, December). Resolving the Imbalance Issue in Hierarchical Disciplinary Topic Inference via LLM-based Data Augmentation. In 2023 IEEE International Conference on Data Mining Workshops (ICDMW) (pp. 1424-1429). IEEE.




