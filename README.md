<img src='https://pixabay.com/get/gbe189f56779ab10240126176a18155db13f5f4210b2fa46c2b89f078c136c0a03188ebf03bacfa53e9e8f1653e2cf4c7.jpg'></img>
<figcaption style="text-align: center;">
    <strong>
        Image by <a href="https://pixabay.com/users/alexas_fotos-686414/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1557240">Alexa</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1557240">Pixabay</a>
    </strong>
</figcaption>

# Video Game Ratings Analysis

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/anudeepvanjavakam1/video_games_rating_analysis?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/anudeepvanjavakam1/video_games_rating_analysis)
![GitHub issues](https://img.shields.io/github/issues-raw/navendu-pottekkat/awesome-readme)
![GitHub pull requests](https://img.shields.io/github/issues-pr/navendu-pottekkat/awesome-readme)
![GitHub](https://img.shields.io/github/license/anudeepvanjavakam1/video_games_rating_analysis)
![Tweet](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fanudeepvanjavakam1%2Fvideo_games_rating_analysis)

IGDB.com is a video game database (acquired by Amazon-owned Twitch), intended for both game consumers and video game professionals alike. IGDB stands for Internet Game Database and consists of 2 primary parts, an online website consisting of a website and 3 mobile apps that provide game consumers with structured and up to date information about games and the gaming world.

This dataset of more than 200K games is collected from [IGDB API](https://api-docs.igdb.com/#about) using [igdb-api-v4 for python](https://github.com/twitchtv/igdb-api-python) but only about 30K+ games have ratings.
This notebook explores any common trends for games that have ratings from igdb and external critics.

Most importantly, we will try to answer these questions:
1) What's the proportion of games in each gaming platform?
2) How do game ratings look for different platforms, genres, themes, age ratings and player perspectives and discuss why?
3) Do Multi player games get higher rating than single player games regardless of platforms, genres, themes, age ratings and player perspectives?
4) Which gaming platform sees more rating success for each genre?
5) Which groups contribute most to great games (games that have a rating of higher than 75)

# Demo-Preview

![GIF](<div style="width:100%;height:0;padding-bottom:84%;position:relative;"><iframe src="https://giphy.com/embed/dO89WY0P8u1CNw7U55" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/dO89WY0P8u1CNw7U55">via GIPHY</a></p>) -->

# Table of contents

- [Project Title](#project-title)
- [Demo-Preview](#demo-preview)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [File Descriptions](#file-descriptions)
- [Licensing and Acknowledgements](#license)
- [Results](#results)

# Installation
[(Back to top)](#table-of-contents)

To use this project, first clone the repo on your device using the command below:

```git init```

```git clone https://github.com/anudeepvanjavakam1/video_games_rating_analysis.git``` -->

This was developed using Python 3.10.4 and the following libraries:
numpy
pandas
empericaldist
matplotlib
seaborn
missingno
plotly
tqdm
colorama



# File Descriptions
[(Back to top)](#table-of-contents)

exploring_igdb_games_decluttered.ipynb is the jupyter notebook with shortened (only a bit) code and visualizations.
exploring_igdb_games_data.ipynb is the jupyter notebook that includes extra code and visualization content.


# Licensing and Acknowledgements
[(Back to top)](#table-of-contents)

[The MIT License | Open Source Initiative](https://opensource.org/licenses/MIT)

Some of the plot ideas/code are adapted from:
https://github.com/miykael/miykael.github.io/blob/master/assets/nb/03_advanced_eda/nb_advanced_eda.ipynb and
https://towardsdatascience.com/my-6-part-powerful-eda-template-that-speaks-of-ultimate-skill-6bdde3c91431


# Results
[(Back to top)](#table-of-contents)


What are the results? Key takeaways, what worked and what didn't? How this project can be improved?
1) Most of the data was either missing or structured in a way that cannot be easily analyzed. Work around: Cleaning and simplifying the data with some assumptions.
2) Majority of the ratings are between 50 and 80 with peaking at 70.
3) Proportion of games in dataset: Windows ~28%, Mac ~9%, PS4 ~7%, Linux ~6.5%, Xbox One ~6%, Nintendo Switch ~6%. Rest of them have less than 6%.
4) Several unique values in each categorical feature make it harder to gain meaningful insights. Had to consider top 10 most frequently occuring values for most of the analysis.
5) With great moderation comes great quality! iOS had better rating distribution than other platforms.
6) 7th Generation consoles (PS3 and Xbox 360) had better ratings than their next gen counterparts. This might be because of bigger library of great games with backward compatibility.
7) Linux and Mac have better ratings than Windows BUT only successful or well known frachise games are made compatible with Linux and Mac. This makes it look like they have better ratings. Thus they have an obvious advantage over Windows which has a plethora of bad and good games.
8) No. of follows for a game doesn't affect the rating but it affects how many people rate the game.
9) Multi player games received higher ratings than single player games. This is expected as these are games that receive (atleast in majority of the cases) the bigger budgets, better development teams, and relatively lenient time schedules. These are the games that publishers want to be the biggest of the year, and they do everything they can up to launch to ensure those results. They are more profitable (in-game purchases) and have higher bar to deliver and cater to thousands if not millions of gamers where as most single player games are a one time purchase and fall a little short in generating recurring profits.
10) Although they are less than 5% of the proportion, Mature age rated games received higher ratings than Teen or Everyone rated games. Mature games grab away all the awards as well. They have more freedom in story-telling/character and level design/gameplay and have more attention to detail. Thus, they clearly have more chance to deliver better impact and experience to a gamer.
11) Best platform for each genre  -- expand here
12) Which groups conribute most to great games (games that have >75 rating) -- expand here



<!-- Add the footer here -->

<!-- ![Footer](https://github.com/navendu-pottekkat/awesome-readme/blob/master/fooooooter.png) -->
