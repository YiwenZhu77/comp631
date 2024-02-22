# Proposal for task 3 

## 1. Introduction

In this project, we aim to build an information retrieval system on Wikipedia pages related to the topic of space physics. The primary motivation behind this is to create a database specifically tailored for the topic, providing better ranking and suggestions, and adding more tolerance in searching for technical words. 

## 2. Data Collection

We will use the Wikipedia API (wikmedia API) to collect the data. The data we will collect includes the content of Wikipedia pages related to space physics. We will retrieve the pages using relevant keywords and categories to ensure the data is comprehensive and relevant.

## 3. Data Cleaning and Preprocessing

Once the data is collected, we will perform necessary cleaning and preprocessing steps. This includes removing irrelevant information, handling duplicate content, and standardizing the data format. We will also apply techniques such as tokenization, stemming, and stop-word removal to improve the quality of the data.

## 4. Indexing with Solr

The main index and search engine for our information retrieval system will be Solr, which is a popular open-source search platform. We will use Solr to build the index for the Wikipedia pages related to space physics. This involves creating a schema to define the fields and their types, and then indexing the cleaned and preprocessed data into Solr.

## 5. Search and Ranking Algorithms

To enhance the search capabilities of our system, we will test and compare different search and ranking algorithms provided by Solr. These algorithms include BM25, DFR, and LMDirichlet. We will evaluate their performance in terms of precision, recall, and relevance to determine the best algorithm for our search engine.

## 6. Evaluation and Improvement

We will evaluate the performance of our information retrieval system by comparing the search results against the relevance and accuracy of the Wikipedia pages related to space physics. We will measure the quality of the ranking and suggestion features, as well as the tolerance in searching for technical words. Metrics such as precision, recall, and speed will be used for evaluation. Based on the evaluation results, we will make necessary improvements to enhance the system's performance and user experience.

## 7. Method Evaluation

Our method will be evaluated by domain experts in the field of space physics. They will assess the effectiveness of the search engine in retrieving relevant and accurate information. Additionally, we will conduct user testing to gather feedback and measure user satisfaction. The evaluation process will involve comparing our system's performance with existing information retrieval systems and assessing its advantages and limitations.

## 8. Project Timeline

We have outlined the following timeline for our project:

- Data Collection: 2 weeks
- Data Cleaning and Preprocessing: 1 week
- Indexing with Solr: 1 week
- Search and Ranking Algorithm Testing: 2 weeks
- Evaluation and Improvement: 2 weeks
- Method Evaluation and User Testing: 1 week
- Finalizing the Project: 1 week

We will adhere to this timeline to ensure timely completion of the project and allow for any necessary adjustments along the way.
