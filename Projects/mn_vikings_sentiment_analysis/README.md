# Minnesota Vikings Subreddit Sentiment Analysis

## Overview

This project analyzes the sentiment and themes of discussions on the Minnesota Vikings subreddit. The analysis aims to uncover key themes, narratives, and the impact of the team's performance on fan discussions. The project employs various text mining techniques, including LDA topic modeling and sentiment analysis, to provide insights into the community's discourse.

## Table of Contents

- [Introduction](#introduction)
- [Data Description](#data-description)
- [Methodology](#methodology)
- [Results](#results)
- [Conclusion](#conclusion)
- [How to Run](#how-to-run)
- [Citation](#citation)

## Introduction

Vikings fandom has a unique character formed by years of storylines, memes, and shared experiences. This report delves into the vibrant and passionate conversations among Vikings fans, aiming to uncover the key themes and narratives that shape their community.

Key questions addressed:

- What are Vikings fans talking about every year?
- What themes exist in every year of the data?
- What effect does the team’s record have on these discussions?

## Data Description

The data was gathered from the [Pushshift Reddit dataset](https://www.reddit.com/r/pushshift/comments/1akrhg3/separate_dump_files_for_the_top_40k_subreddits/). There are three datasets used in this analysis:

-**MN Vikings Subreddit Posts**: Contains posts made on the Minnesota Vikings subreddit.

-**MN Vikings Subreddit Comments**: Contains comments made on the Minnesota Vikings subreddit.

-**MN Vikings Records**: Contains historical performance data of the Minnesota Vikings team.

## Methodology

The analysis involves several steps:

1.**Data Loading**: Load the raw datasets using R libraries.

2.**Data Cleaning**: Remove outliers and add useful columns like the football season.

3.**Exploratory Data Analysis (EDA)**: Summarize and visualize the data to understand its structure and key characteristics.

4.**Text Mining**: Perform sentiment analysis and topic modeling to uncover themes and sentiments in the posts and comments.

## Results

The analysis reveals the following insights:

- Positive sentiments outweigh negative sentiments in subreddit posts, reflecting the optimistic view of fans.
- The number of posts and comments has generally increased over the years, with peaks during successful seasons.
- Common themes in discussions are centered around players, coaches, and general managers.

## Conclusion

The analysis provides valuable insights into the discussions among Vikings fans. The discourse is predominantly centered around key figures in the team, and the sentiment is generally positive. Future analyses could focus on refining the stop words list, isolating player-specific discussions, and analyzing game-specific threads.

## How to Run

To run the analysis, follow these steps:

1.**Install Required Libraries**: Ensure you have the necessary R libraries installed.

    ```r

    install.packages(c("tidyverse", "tidytext", "scales", "lubridate", "skimr", "topicmodels", "lsa", "rvest", "topicdoc", "future", "furrr"))

    ```

2.**Load the Data**: Place the datasets in the `data/processed/` directory.

    -`minnesotavikings_submissions.csv`

    -`minnesotavikings_comments.csv`

    -`vikings_records.csv`

3.**Run the R Markdown File**: Open the `soltau_blog.Rmd` file in RStudio and knit it to generate the HTML report.

## Citation

Data prior to April 2023 was collected by Pushshift, data after that was collected by u/raiderbdev [here](https://www.reddit.com/user/raiderbdev). Extracted, split, and re-packaged by u/Watchful1. Hosted on [academictorrents.com](https://academictorrents.com).
