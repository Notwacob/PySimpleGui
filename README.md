<style>

    .center {
        text-align: center;
    }

    #sideMenu {
        position: fixed; 
        color: #fff; 
        font-size: 14px; 
        font-weight: 600; 
        background: #0095ba; 
        padding: 10px 10px 10px 36px; 
        height: 100%; 
        width: 250px; 
        overflow: wrap; 
        top: 0; 
        left: 0; 
    }

    #sideMenu a {
        color: #fff;
        text-decoration: underline;
    }

    #sideMenu a:hover {
        color: darkblue;
    }

    #sideMenu h1 {
        text-align: center;
    }

    #mainContent {
        margin-left: 260px;
        padding: 20px;
        margin-top: 10px;
        overflow-y: scroll;
    }

    #mainContent h2 {
        margin-top: 20px;
    }

    /* Media query for mobile devices */
    @media (max-width: 768px) {
        #sideMenu {
            position: fixed;
            width: 100%;
            height: auto;
        }

        #sideMenu h1 {
            text-align: left;
        }

        #mainContent {
            margin-left: 0;
            margin-top: 310px;
        }
}

</style>

<div id="sideMenu"> 
	<h1>Table of Contents</h1>
    <ol>
        <li><a href="#Converter-App">Converter App</a></li>
        <li><a href="#Calculator-App">Calculator App</a></li>
        <li><a href="#Stopwatch-App">Stopwatch App</a></li>
        <li><a href="#Text-Editor-App">Text Editor App</a></li>
        <li><a href="#Snake-Game">Snake Game</a></li>
        <li><a href="#Graph-App">Graph App</a></li>
        <li><a href="#Image-Editor-App">Image Editor App</a></li>
        <li><a href="#Music-Player-App">Music Player App</a></li>
        <li><a href="#Weather-App">Weather App</a></li>
        <li><a href="#Face-Detector-App">Face Detector App</a></li>
    </ol>
</div> 
<div id="mainContent">
    <h1>PySimpleGui Tutorial Code</h1>
    <p>I have meticulously crafted this code by diligently following the comprehensive PySimpleGUI tutorial presented by <b>Clear Code</b> on YouTube (<a href="https://www.youtube.com/watch?v=kQ8DGP9p2LY&t=1" target="_blank">here</a>).</p>
    <p>Throughout this extensive tutorial, I have successfully developed an awe-inspiring collection of 10 diverse apps using PySimpleGui in Python. Each of these remarkable apps is thoughtfully organized within its dedicated folder, ensuring easy navigation and management. As you delve deeper into the project, you will discover a pivotal file named "app.py" residing in the root directory. This crucial file serves as the backbone of our PySimpleGui application, enabling the effortless launch of our exceptional array of apps.</p>
    <div align="center">
        <img src="https://cdn.discordapp.com/attachments/1081311787821043805/1109016405002690620/image.png" alt="launcher app">
    </div>
    <h2 id="#Converter-App">Converter App</h2>
    <p>This application serves as an intuitive converter, seamlessly transforming units for kilometers to miles, kilograms to pounds, and seconds to minutes. With a user-friendly interface, it effortlessly accepts input values and promptly generates accurate conversions. The design prioritizes simplicity, allowing for effortless expansion of the application's conversion capabilities in the future.</p>
    <div align="center">
	    <img src="https://cdn.discordapp.com/attachments/1081311787821043805/1109019269922050098/image.png" alt="Converter App Base">
	    <img src="https://media.discordapp.net/attachments/1081311787821043805/1109019568707473448/image.png" alt="Converter App with Output">
    </div>
    <h2 id="Calculator-App">Calculator App</h2>
    <p>This application offers a user-friendly calculator interface, designed to effortlessly handle basic mathematical calculations. With just a few clicks, you can perform operations such as addition, subtraction, multiplication, and division.</p>
    <p>Upon pressing any number button, the corresponding digit instantly appears in the output field at the top, ensuring swift and accurate input. When an operator button is selected, the output field is automatically cleared, while the previous number remains stored within the program. This convenient feature allows you to seamlessly enter a new number for further calculations. Finally, the application efficiently executes the desired operation and displays the accurate result in the output field.</p>
    <p>For an added touch of personalization, you can customize the visual appearance of the calculator by simply right-clicking within the output field. A variety of appealing themes are available for you to choose from, allowing you to tailor the calculator to your preferred style.</p>
    <div align="center">
	    <img src="https://media.discordapp.net/attachments/1081311787821043805/1109020017506402346/image.png" alt="Calculator App Base">
	    <img src="https://media.discordapp.net/attachments/1081311787821043805/1109026812262088714/image.png" alt="Calculator App with Output">
    </div>
    <h2 id="Stopwatch-App">Stopwatch App</h2>
    <p>This is a user-friendly stopwatch application that allows you to easily start, stop, and reset the stopwatch. You can record laps to keep track of different time intervals. The simple and intuitive interface makes it accessible and enjoyable to use, whether for timing events, workouts, or any other activities that require precise time measurements.</p>
    <div align="center">
	    <img src="https://media.discordapp.net/attachments/1081311787821043805/1109030510652575785/image.png" alt="Stopwatch App Base">
	    <img src="https://media.discordapp.net/attachments/1081311787821043805/1109030960391016458/image.png" alt="Stopwatch App Base with Outputs">
	    <img src="https://media.discordapp.net/attachments/1081311787821043805/1109031684411752530/image.png" alt="Stopwatch App Base After Hitting Stop button">
    </div>
    <h2 id="Text-Editor-App">Text Editor App</h2>
    <p>The Text Editor Application is a highly user-friendly program designed to empower users in creating, editing, and effectively managing their text documents. This comprehensive documentation aims to provide a detailed overview of the application's exceptional features, remarkable functionality, and clear usage instructions.</p>
    <p>With the Text Editor Application, users are presented with a seamless and intuitive user interface that enables effortless creation and efficient management of text documents. Boasting a rich set of features including file opening and saving, word counting, and even smiley insertion, users are equipped with all the essential tools to effortlessly edit their text files and elevate the quality of their content. The application's thoughtfully crafted design and cohesive theme contribute to a delightful and immersive user experience, ensuring a pleasant journey throughout the text editing process.</p>
    <div align="center">
	    <img src="https://media.discordapp.net/attachments/1081311787821043805/1109035388267409508/image.png" alt="Text Editor App Base">
	    <img src="https://cdn.discordapp.com/attachments/1081311787821043805/1109035852253892619/image.png" alt="Text Editor App Base with Text Input">
	    <br>
	    <img src="https://media.discordapp.net/attachments/1081311787821043805/1109036877400514622/image.png" alt="Text Editor App Word Counter">
    </div>
    <h2 id="Snake-Game">Snake Game</h2>
    <p>This code is a basic Snake game application. When you run it, a window titled "Snake" will appear with a black game field. You control a snake using the arrow keys on your keyboard. The objective is to guide the snake to eat red apples that randomly appear on the field. The snake moves continuously in the direction it's facing. Every 0.5 seconds, the game checks for your input and updates accordingly. If the snake's head touches an apple, it eats it and grows longer. The game ends if the snake hits the field boundaries or if its head collides with its own body. The window closes at that point. The snake's head is yellow, and the rest of its body is green. The apples are red.</p>
    <div align="center">
	    <img src="https://media.discordapp.net/attachments/1081311787821043805/1109037508773302383/image.png" alt="Snake Game">
    </div>
    <h2 id="Graph-App">Graph App</h2>
    <p>This application is designed to help users visualize numerical data in a simple and intuitive way. When you open the application, you'll see a window with a table and a graph. To use the application, all you need to do is enter numeric values into an input field and click "Submit." The application will add your data to the table and update the graph instantly. The graph will show a line connecting all the points you've entered. You can keep entering data and see how it affects the table and the graph. It's a great way to understand patterns and trends in your data. When you're done using the application, just close the window. Your data won't be saved. Overall, this application is a simple tool for visualizing numeric data. It's easy to use and provides real-time updates, allowing you to explore and analyze your data effortlessly.</p>
    <div align="center">
    	<img src="https://media.discordapp.net/attachments/1081311787821043805/1109041022446616607/image.png" alt="Graph App Base">
    	<img src="https://cdn.discordapp.com/attachments/1081311787821043805/1109041251359133696/image.png" alt="Graph App Base With Inputs">
    </div>
    <h2 id="Image-Editor-App">Image Editor App</h2>
    <p>The app has a user-friendly interface with two main sections. On the left side of the window, you'll see sliders and checkboxes. These sliders control the blur and contrast of the image, allowing you to make it more or less blurry and adjust the brightness. The checkboxes enable special effects like embossing, which creates a 3D effect, and contouring, which enhances object edges.</p>
    <p>On the right side of the window, the app displays the image you're editing. As you make changes using the sliders and checkboxes, the image updates in real-time, instantly showing you the effects. If you want to flip the image horizontally or vertically, simply check the corresponding boxes, and the image will flip accordingly, reflecting the changes immediately.</p>
    <p>When you're satisfied with the edits, you can click the "Save" button. The app will prompt you to choose a location on your computer to save the edited image as a PNG file. Give it a name, and it will be saved for you. If you're done editing or want to exit the app, simply close the window as you would with any other program.</p>
    <p>That's it! This user-friendly image editing app allows you to adjust blur, contrast, apply special effects, flip the image, and save your edits easily. It's a straightforward tool for editing images without any complex steps or confusing options.</p>
    <div align="center">
    	<img src="https://media.discordapp.net/attachments/1081311787821043805/1109042094745604177/image.png" alt="Image Editor App Base">
    	<img src="https://media.discordapp.net/attachments/1081311787821043805/1109042095014023239/image.png" alt="Image Editor With Inputs">
    </div>
    <h2 id="Music-Player-App">Music Player App</h2>
    <p>This music player application has a simple interface. When you open the program, a window appears with a play button and a pause button. You can select a song file from your computer, and its name will be displayed. Clicking the play button starts playing the song, and the pause button allows you to pause the playback. There is also a volume slider to adjust the volume level. The window can be closed when you're done using the application.</p>
    <div align="center">
    	<img src="https://media.discordapp.net/attachments/1081311787821043805/1109046028046446642/image.png" alt="Music Player App Play Tab">
    	<img src="https://media.discordapp.net/attachments/1081311787821043805/1109046028285513748/image.png" alt="Music Player App Volume Tab">
    </div>
    <h2 id="Weather-App">Weather App</h2>
    <p>The weather application is a user-friendly tool that allows you to check the weather for different locations. When you open the application, you'll see a window with an input field where you can enter the name of a city or town. Once you type in the location and press the "Enter" button, the application fetches the latest weather data for that location from the internet.</p>
    <p>The retrieved weather information, including the location name, current time, weather conditions, and temperature, is then displayed in the application window. Additionally, the application uses weather symbols to visually represent the current weather conditions, making it easier to understand at a glance.</p>
    <p>You can continue using the application by entering new locations and receiving their respective weather updates. Whenever you're done, simply close the application window to exit the program.</p>
    <p>Overall, this weather application provides a straightforward way to stay informed about the weather conditions in different places, with real-time data and a clean user interface.</p>
    <div align="center">
    	<img src="https://media.discordapp.net/attachments/1081311787821043805/1109055945172062249/image.png" alt="Weather App Base">
    	<img src="https://media.discordapp.net/attachments/1081311787821043805/1109055945448894494/image.png" alt="Weather App with London's Weather">
    </div>
    <h2 id="Face-Detector-App">Face Detector App</h2>
    <p>This face detector app has a window where you can see yourself through your computer's camera. As the app runs, it automatically recognizes and outlines any faces it detects in the video stream using green rectangles. Below the video, there's a number that shows how many faces are currently visible. For example, if there are three faces in the frame, it will display "3" next to "People in picture." You can move around or invite others to join the frame, and the app will instantly update the rectangles and the face count. When you're done using the app, you simply close the window, and it gracefully stops accessing the camera. Overall, it's a user-friendly app that uses your computer's camera to detect faces in real-time and provides a count of the number of faces it finds. It's a fun and convenient tool for various purposes, like knowing how many people are in the frame or exploring face detection technology.</p>
    <div align="center">
    	<img src="https://media.discordapp.net/attachments/1081311787821043805/1109055945813790730/image.png" alt="Face Detector App Base">
    </div>
</div>