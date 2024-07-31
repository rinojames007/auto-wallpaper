# Automatic Wallpaper Changing Service

This service automatically fetches a fresh wallpaper from Unsplash and sets it as your current wallpaper. For demonstration purposes, it fetches and updates the wallpaper every minute.

### Features:
* Fetches high-quality wallpapers from Unsplash.
* Updates wallpaper at a configurable interval.

Currently for linux machines only, I don't have a windows machine so no idea how to do there.

## Installation

### Clone the Repository

```bash
git clone https://github.com/rinojames007/auto-wallpaper/
```

### Enter the Repository

```bash
cd auto-wallpaper
```

### Install Dependencies
Make sure you have Python installed. Then install the required packages:

```bash
pip install -r requirements.txt
```

I have used [Poetry](https://python-poetry.org/docs/), but the default pip would be enough I guess.

### Configure the Service
Firstly Generate an API key from [here](https://unsplash.com/developers).<br />

Create a file to store the unsplash API.
```bash
nvim secret.key
```
paste your secret and exit neovim `:wq` or from your text editor.

The unsplash api will give you access key and the secret key.<br/>
Figuring it out and implementing it onto the cryptography module is a mini task for you 😂

You may create a logging file where the cron job could return its status whenever it runs.
```bash
touch wall.log
```

### Setting up the cron job
```bash
crontab -e
```
open cron tab and paste the following snippet
```bash
* * * * * echo "Starting script at $(date)" >> /home/rinojames007/MyFiles/script/wall.log 2>&1 && export DISPLAY=:0 && cd /home/rinojames007/MyFiles/script && /usr/bin/python3 updateWall.py >> /home/rinojames007/MyFiles/script/wall.log 2>&1 && /usr/bin/feh --bg-fill pywall.jpg >> /home/rinojames007/MyFiles/script/wall.log 2>&1 && echo "Script completed at $(date)" >> /home/rinojames007/MyFiles/script/wall.log 2>&1
```
For the time interval, you can set it up [here](https://crontab.guru/#*_*_*_*_*).

It would look something like this<br />
![image](https://github.com/user-attachments/assets/307ab82e-18b3-4613-be26-4ab338a3daa8)

### Usage

Once running, the service will automatically fetch a new wallpaper from Unsplash and set it as your current wallpaper according to the specified interval.

https://github.com/user-attachments/assets/9211d08a-a00b-4a14-b8de-046f3b6ca723

### Contributing

Feel free to fork the repository and submit pull requests. Any suggestions or improvements are welcome!

### License

This project is licensed under the [MIT](https://opensource.org/license/mit) License. See the LICENSE file for details.
