![banner](images_for_readme_gif/mario-1557240.jpg)
<figcaption style="text-align: center;">
    <strong>
        Image by <a href="https://pixabay.com/users/alexas_fotos-686414/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1557240">Alexa</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=1557240">Pixabay</a>
    </strong>
</figcaption>

# Video Game Ratings Analysis

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/anudeepvanjavakam1/video_games_rating_analysis?include_prereleases)
![GitHub last commit](https://img.shields.io/github/last-commit/anudeepvanjavakam1/video_games_rating_analysis)
![GitHub](https://img.shields.io/github/license/anudeepvanjavakam1/video_games_rating_analysis)
![Tweet](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fanudeepvanjavakam1%2Fvideo_games_rating_analysis)

IGDB.com is a video game database (acquired by Amazon-owned Twitch), intended for both game consumers and video game professionals alike. IGDB stands for Internet Game Database and consists of 2 primary parts, an online website consisting of a website and 3 mobile apps that provide game consumers with structured and up to date information about games and the gaming world.

This dataset of more than 200K games is collected from [IGDB API](https://api-docs.igdb.com/#about) using [igdb-api-v4 for python](https://github.com/twitchtv/igdb-api-python) but only about 30K+ games have ratings.
This notebook explores any common trends for games that have ratings from igdb and external critics.

**Most importantly, we will try to answer these questions:**
1) What's the proportion of games in each gaming platform?
2) How do game ratings look for different platforms, genres, themes, age ratings and player perspectives and discuss why?
3) Do Multi player games get higher rating than single player games regardless of platforms, genres, themes, age ratings and player perspectives?
4) Which gaming platform sees more rating success for each genre?
5) Which groups contribute most to great games (games that have a rating of higher than 75)

# Demo-Preview

![GIF](https://media.giphy.com/media/dO89WY0P8u1CNw7U55/giphy.gif)


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

**exploring_igdb_games_decluttered.ipynb** -- decluttered jupyter notebook with fewer code cells and visualizations.
**exploring_igdb_games_data.ipynb** -- jupyter notebook that includes extra code and visualization content.


# Licensing and Acknowledgements
[(Back to top)](#table-of-contents)

[The MIT License | Open Source Initiative](https://opensource.org/licenses/MIT)

**Some of the plot ideas/code are adapted from:**
- https://github.com/miykael/miykael.github.io/blob/master/assets/nb/03_advanced_eda/nb_advanced_eda.ipynb
- https://towardsdatascience.com/my-6-part-powerful-eda-template-that-speaks-of-ultimate-skill-6bdde3c91431


# Results
[(Back to top)](#table-of-contents)


**Key Takeaways:**
1) Most of the data was either missing or structured in a way that cannot be easily analyzed. Data is pre-processed and simplified with some assumptions.

2) Majority of the ratings are between 50 and 80 with peaking at 70.

3) Proportion of games in dataset: Windows ~28%, Mac ~9%, PS4 ~7%, Linux ~6.5%, Xbox One ~6%, Nintendo Switch ~6%. Rest of them have less than 6%.

4) Several unique values in each categorical feature make it harder to gain meaningful insights. Had to consider top 10 most frequently occuring values for most of the analysis.

5) With great moderation comes great quality! iOS had better rating distribution than other platforms.

6) 7th Generation consoles (PS3 and Xbox 360) had better ratings than their next gen counterparts. This might be because of bigger library of great games with backward compatibility and longer time in market.

7) Linux and Mac have better ratings than Windows BUT only successful or well known frachise games are made compatible with Linux and Mac. This makes it look like they have better ratings. Thus they have an obvious 
advantage over Windows which has a plethora of bad and good games.
8) No. of follows for a game doesn't affect the rating but it affects how many people rate the game.

9) Multi player games received higher ratings than single player games. This is expected as these are games that receive (atleast in majority of the cases) the bigger budgets, better development teams, and 
relatively lenient time schedules. These are the games that publishers want to be the biggest of the year, and they do everything they can up to launch to ensure those results. They are more profitable (in-game 
purchases) and have higher bar to deliver and cater to thousands if not millions of gamers where as most single player games are a one time purchase and fall a little short in generating recurring profits.

10) Although they are less than 5% of the proportion, Mature age rated games received higher ratings than Teen or Everyone rated games. Mature games grab away all the awards as well. They have more freedom in story-telling/character and level design/gameplay and have more attention to detail. Thus, they clearly have more chance to deliver better impact and experience to a gamer.

11) Platform with the highest median rating in each genre:

-   Simulator: Linux followed by Mac and Xbox 360.
-   Point and Click: PS3 followed by Xbox 360. Windows and Linux have the worst ratings. I wasn't expecting this at all for point and click games. 
-   Adventure: Linux followed by PS4. Linux has unusually high ratings here but that may be because only successful Windows games (most of the time) are made compatible for Linux and hence we see higher rating here.
-   Shooter: Android followed Mac. This is surprising that Android has higher ratings than other platforms as they offer better shooter game experience. Windows has the lowest median rating.
-   Platform: PS3 followed by Nintendo Switch
-   RPG: PS3 followed by Xbox 360
-   Fighting: PS3 followed by Xbox 360
-   Puzzle: iOS followed by Android
-   Strategy: Android
-   Racing: PS3 followed by Mac

12) 

Group |% of games that are great given a category group
-----|-----
Mature|49%. In other words, in age limit category, 49% of the games will be great given they belong to Mature group.
Mac|44%. This is only 4% higher than PC Windows and 2% higher than other platforms. May be platform doesn't matter?
Fantasy|48%
RPG|46%
Text View|49% (There are very few text games but their rating seems to be high). If we only consider popular views, then first person and side view have great games (43%).

13) Last but not least, we should accept that the results here are based on several assumptions (example - genres and themes are tagged correctly for games), one of which is that this dataset is a representative sample of the games released in the world and is not already biased for any particular group. For example, If PS3 had only well known games added to IGDB database, it would invalidate our results.

**Expansion Ideas**
- Publishers and Developers data can be analyzed to see how they do in terms of rating.
- If there are separate ratings for gameplay, controls, level design, challenge, characters, etc. it would give more insight into what role they actually play in making a game great.
- It would be interesting to see to what extent higher rating influences game sales.
- Do games that do not have similar games associated with them receive higher rating when compared to games that have many similar games?
- Would be interesting to see if games with websites associated with them have higher hype or rating?
- Assigning more weightage to rating based on how many people have rated a game.

![Footer](images_for_readme_gif/gamer-6022003_1280.png)
Image by <a href="https://pixabay.com/users/cromaconceptovisual-4595909/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6022003">cromaconceptovisual</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6022003">Pixabay</a>