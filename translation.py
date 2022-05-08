class Translation(object):
    START_TEXT = """Здравствуйте {},
Я All URL Uploader!
Вы можете загрузить файл|видео в Telegram с прямой ссылкой, используя этого бота!
Сайты поддержки <a href="https://t.me/Muharibun07">HERE</a>
/help для более подробной информации!"""
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | filename | username | password"""
    DOWNLOAD_START = "📥Загрузка..."
    UPLOAD_START = "📤Uploading..."
    RCHD_TG_API_LIMIT = "Загружается {} за несколько секунд.\nРазмер обнаруженного файла: {}\nИзвините. Но я не могу загружать файлы размером более 2 ГБ из-за ограничений API Telegram."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Спасибо, что используете меня \n\n<b>Присоединяйтесь к @Muharibun07 </b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Загружено за {} секунд.\nЗагружено за {} секунд.\n\n@Muharibun07"
    SAVED_CUSTOM_THUMB_NAIL = "Сохранение пользовательской миниатюры видео / файла. Это изображение будет использоваться в видеоролике / файле."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Пользовательские миниатюры успешно очищены."
    CUSTOM_CAPTION_UL_FILE = "{}"
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    ABOUT_MSG = """ Кое-что обо мне :
    
   ☞My Name  : All Url Uploader Bot

   ☞Updates  : @Muharibun07    

   ☞Language : Python3

   ☞Library  : <a href="https://docs.pyrogram.org/">Pyrogram 1.0.7</a>"""
    HELP_USER = """Пожалуйста, выполните следующие действия!
    
1. Отправьте url (example.domain/File.mp4 | New Filename.mp4).
2. Отправить изображение как пользовательскую миниатюру (необязательно).
3. Выберите кнопку.
   SVideo - Передать файл как видео со скриншотами
   DFile - Передать файл (видео) как файл со скриншотами
   Видео - Передать файл как видео без скриншотов
   Файл - Передать файл без скриншотов

Если бот не ответил, спросите здесь @isIam07"""
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Передайте /generatecustomthumbnail медиаальбому, чтобы создать пользовательскую миниатюру"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = """Медиаальбом должен содержать только две фотографии. Пожалуйста, отправьте медиаальбом повторно, а затем повторите попытку, или отправьте только две фотографии в альбоме."
Вы можете использовать команду /rename после получения файла, чтобы переименовать его с поддержкой пользовательских миниатюр.
"""
    CANCEL_STR = "Процесс отменен"
    ZIP_UPLOADED_STR = "Загрузил {} файлов за {} секунд"
    SLOW_URL_DECED = "Боже, похоже, это очень медленный URL. С тех пор, как вы испортили мой дом, у меня нет настроения загружать этот файл."
