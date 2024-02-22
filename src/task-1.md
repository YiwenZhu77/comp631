# Task 1 report 

In the data collection phase, we utilized the Wikipedia API to gather information. Due to the non-tree-like structure of Wikipedia data, which may contain loops and multi-edges, we adopted a search approach rather than simply gathering pages under a parent category. Specifically, we searched for pages under a parent category and its sub-categories up to a depth of 4.

The parent category we selected for this task is 'Space Science', resulting in a total of approximately 70,000 pages. We collected the data from these pages and saved it in a JSON file.

During the preprocessing phase, we focused on cleaning and organizing the collected data. We removed duplicate pages and irrelevant content, ensuring that the data is sensible and coherent. The resulting data was then structured and stored in a JSON file for further analysis and processing.

The crawler file and the JSON file containing the data are available in the project repository (https://github.com/YiwenZhu77/comp631.git).