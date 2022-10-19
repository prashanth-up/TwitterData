# NLP Project Assignment

## GOAL
Your task:

1.  Scrape tweets from Twitter or crawl the web to find related tweets or news items (you only need to do one of these two. Choose the one you are most familiar with);
    
2.  Train a classifier to separate opinions that either support or are against this decision.
## Progress Tracking: 
TASKS:
- [x] Get real data from twitter relating to the topic given
- [x] Build a custom Scraper to scrape twitter
- [x] Clean the data 
- [x] Organize the data 
- [x] Build a bot to keep scraping new tweets 
- [x] Get the data ready for ML 
- [x] Train a classifier to separate opinions that either support or are against this decision.
- [x] Check the necessary parameters required as important factors
- [x] Run the Model a few times 
- [x] Optimize it based on the results 
- [ ] Try different approaches in building the model 
- [x] Compare the different results 
- [ ] Prepare the visualization for all these models
- [x] Collaborate with Team and discuss approaches
- [ ] Locate entities/evidences to help explain the results.

IN-Progress:
- [x] NA

## FILES

### Runtime Files
- scraper.py - The twitter tweet scraper (run only for the first time)
- newDataBot.py - The bot that adds new unique tweets onto the existing dataset (After the first CSV is created)
- main.py - Takes the data files and stores in custom format for our NLP Model (in /data)
- train.py (Trains the model)(Uses CUDA GPU, if not available uses default CUDA CPU)
- Contrastive Learning.ipynb (Runs our trained model over some validation data in `/data`)


### Jupyter Notebooks
- DataVis Scraped Data.ipynb - Has visual info on the scraped dataset. Just for reference
- Contrastive Learning.ipynb -  The main file which will hold the our classifier.  

### How to Use:
 - Run the `scraper.py` first to get the raw tweets.
 Optional (run newDataBot to get new unique tweets and add them to the dataset).
 - Run `main.py` to generate our custom formatted dataset for our model.
 - Run `train.py` to train our contrastive learning NLP model.
 - Open `Contrastive Learning.ipynb` to test our model over some validation tweets.

### Presentation:
- [Presentation Link](https://github.com/prashanth-up/TwitterData/blob/master/ContrastiveLearningReport.pptx)
