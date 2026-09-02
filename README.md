# Hygroelectric-Harvesting-Toolbox

> The package includes an arduino assembly for measuring the ambient temperature and humidity via a DHT-22 sensor and a reader to record the mass from a balance from a USB Type-B port.<br>
> These are some simple programs I made for data collection during my last research project.<br>
> Just trying to put stuffs up here and just in case if anyone needs these ;)

## DHT-22 Sensor Set-up

> The set-up was built for an Arduino UNO board, connecting the middle pin of DHT-22 to "D2" and the remaining 2 being GND and 5V. <br>


> As I was carrying out the measurement on the borrowed laptop from another lab, which did not install python and not to mention the corresponding libraries, I assembled DHT-22_Data_logger.exe with pyinstall. >_> <br>
> However a problem that comes with this is that I cannot access the code easily anymore. TAT <br>
> I hard-coded SERIAL_PORT at "COM4" but just use DHT-22 Data logger.py if things goes wrong and change port number there...

> Anyways good luck w these ;D <br> -Edward
### The DHT-22 Data logger.py requires pyserial in the environment. My installed version was 3.5.

