# GooglePlayMusic_to_Spotify
Script which helps transfer liked songs from Google Play Music to Spotify.

This scripet based on two libraries - gmusicapi and spotipy.

*****

Before running the script:
- register the app in [spotify] (https://developer.spotify.com/dashboard/applications)
- substitute your fields client_id = '<FILL_ME>' and client_secret = '<FILL_ME> into the script
- copy the link http://example.com/ to the Redirect URIs of the Spotify settings.

After running the script, follow the instruction in console. 

After successful authentication on both music services myMusic.csv file will be created in script directory.
This file will be filled with the following data: Artist, Track, Album, Year and Spotify track ID (if the track is found in the spotify library).
While the script is running, the console will display the names of the tracks that are being copied at the moment.

*****

Перед запуском скрипта:
- зарегистрировать приложение в [spotify](https://developer.spotify.com/dashboard/applications) 
- подставить свои поля client_id='<FILL_ME>' и client_secret='<FILL_ME> в скрипт
- скопировать ссылку http://example.com/ в Redirect URIs настроек Spotify.

Запустив скрипт появится надпись:

Visit the following url:
 https://accounts.google.com/o/oauth2/v2/auth?client_id=222...

И попросит ввести код, который будет доступен по ссылке.

При успешной аутентификации на обоих музыкальных сервисах в папке со скриптом будет созадн файл myMusic.csv, в который по ходу сканироварния каталога понравившихся треков в GPM будут передваться поля: Исполнитель, Трек, Альбом, Год и Spotify track ID (если трек будет найден в библиотеке  spotify). В процессе работы скрипта в консоли будут выведены названия треков, которые копируются в текущий момент.


PS: Я не программист и не пишу комерческий код, но этот скрипт работает. С его помощью я перенес все свои 500 треков из GPM в Spotify, в то время как онлайн сервисы предлагали перенести только 100 треков бесплатно.
