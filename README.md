<html>
<body>
<h2>Automatize fan control on RaspberryPi</h2>
<p>#Inspirited by: https://hackernoon.com/how-to-control-a-fan-to-cool-the-cpu-of-your-raspberrypi-3313b6e7f92c</p>

<p>I will use their images</p>
<p>I used NPN transistor for power fan</p>
<p>You can see schematic</p>
<img src="https://cdn-images-1.medium.com/max/1000/1*kD7Nv0KudnLL-9XKJe8t0w.png" width="350"/>

<img src="https://cdn-images-1.medium.com/max/800/1*l6cEydrQ4nQqauCKuhJi4w.png" width="350"/>

<h2>Install</h2>
<p>Step 1., clone repository and change path in sh script to start python script. </p>
<p>Step 2., make script executable with command:<br/><i> chmod 755 launcher.sh</i></p>
<p><b>OPTIONALY</b>
<p>Create logs directory, where cron table storage logs of crashes</p>
<p>Step 3., use these commands to start sh script on start raspberry</p>
<p><i>sudo crontab -e</p>
  <p>@reboot sh /home/pi/launcher.sh >/home/pi/logs/cronlog 2>&1</i></p>
  <p><b>if you don't use logs directory</b></p>
  <p><i>@reboot sh /home/pi/launcher.sh</i></p>
<p>Step 4., reboot your raspberry. If script don't start see log in logs directory.</p>

<p>Step 5., <b>DONE</b>


Pictures are not my assets.<br/>
This project was created just for fun and new experiences.
</body>
</html>
