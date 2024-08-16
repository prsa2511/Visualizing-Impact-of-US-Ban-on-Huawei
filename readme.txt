Running with WAMP Server:

This guide explains how to run the provided HTML file which utilizes d3v7.js library with a WAMP server.

Prerequisites:

- WAMP server installed on your system.
- Basic understanding of WAMP server configuration.
- Basic knowledge of HTML, CSS, and JavaScript.

Instructions:

1. Download the Required Files:
   - Download the HTML files (index.html, mix.html, time_series.html and wordcloud.html) and tweets_finalv4.csv
2. Place Files in WAMP Server Directory:
   - Move all downloaded files to the root directory of your WAMP server. Typically, this directory is www or htdocs.
3. Start WAMP Server:
   - Start the WAMP server from its control panel or through the command line.
4. Access the HTML File:
   - Open a web browser and navigate to http://localhost/index.html or http://127.0.0.1/index.html.
5. View SVG Visualizations:
   - Once the HTML file loads, you should see the SVG visualizations rendered on the page.
6. Interact with SVG Visualizations:
   - Explore each visualization by interacting with them as desired.

Notes:

- Ensure that all file paths within the HTML file are correctly set based on their location in the WAMP server directory.
- Make sure that the WAMP server is properly configured and running to serve the HTML file and associated resources.



Additional Visualization Interactivity and Animation Overview

Sentiment Map:

    Hover Interactivity: When hovering over a sentiment point, it enlarges and changes opacity, providing visual feedback to the user.
    Color Coded Points: Tweets are represented as points colored according to their sentiment (positive, negative, neutral).
    Legend: Provides a legend indicating the colors corresponding to different sentiments.

Dot Map:

    Hover Interactivity: When hovering over a dot, it enlarges and changes opacity, similar to the sentiment map.

Additional Features (mix.html):

    Toggle Switch: Allows users to switch between the sentiment map and the dot map, providing flexibility in visualization.
    Display Setup: Initially hides one map and displays the other, ensuring only one map is visible at a time.
    File Loading: Loads GeoJSON data for world countries and CSV data for tweet sentiments and geocoded locations.
    Projection Setup: Sets up the projection for both maps, ensuring consistency in visualization.

Time Series Sentiment Analysis:

    Line Animation: Each sentiment line is drawn sequentially with a delay between each line, providing a visually appealing animation effect.
					The lines are drawn with a dash pattern, and the dash-offset property is animated to reveal the lines progressively.
    Hover Interactivity: When hovering over a legend item (sentiment), other lines fade out while the hovered sentiment's line remains fully visible, aiding in 	visual comparison.
    Legend: A legend is provided below the chart, indicating the colors associated with each sentiment (positive, negative, neutral).
            Legends are interactive, as hovering over a legend item highlights the corresponding sentiment line on the chart.
    Axes Labels: X-axis label ("Time") and Y-axis label ("No. of Tweets") are provided for clarity, aiding users in understanding the chart.
	
Word Cloud Generator:

    Font Loading: Custom font ('TheMixHair') is loaded using @font-face to ensure consistent rendering of text in the word cloud.
    Font Size Scaling: Font size of each word in the word cloud is scaled dynamically based on its frequency, ensuring that more frequent words appear larger.
    Styling: Box shadow and border styles are applied directly to the SVG element, enhancing the visual appeal of the word cloud.
    Hover Interactivity: When hovering over a word in the word cloud, its color changes to red, providing visual feedback to the user.
						 On mouseout, the color reverts back to its original color.						 
	Start Animation: When the word cloud loads, each word appears with a bouncy animation, gradually increasing in size and settling into its final position within the cloud.