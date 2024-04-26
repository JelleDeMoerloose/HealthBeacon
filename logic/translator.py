from abc import ABC, abstractmethod
import requests


class ITranslator(ABC):
    @abstractmethod
    def all_languages(self) -> dict[str, str]:
        pass

    @abstractmethod
    def translate(self, input: str, language: str) -> str:
        pass


class TranslatorV1(ITranslator):

    def translate(self, input: str, language: str) -> str:
        url = f"https://api.mymemory.translated.net/get?q={input}&langpair={language}"
        try:
            # Make a GET request
            response = requests.get(url)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response into a Python dictionary
                data = response.json()
                print(data["responseData"]["translatedText"])
                return data["responseData"]["translatedText"]
            else:
                # Return None if the request was unsuccessful
                raise NameError(f"Translate API responded with:{response.status_code}")
        except Exception as e:
            # Print any exception that occurs
            print("Error:", e)
            raise

    def all_languages(self) -> dict[str, str]:
        countries = {
            "am-ET": "Amharic",
            "ar-SA": "Arabic",
            "be-BY": "Bielarus",
            "bem-ZM": "Bemba",
            "bi-VU": "Bislama",
            "bjs-BB": "Bajan",
            "bn-IN": "Bengali",
            "bo-CN": "Tibetan",
            "br-FR": "Breton",
            "bs-BA": "Bosnian",
            "ca-ES": "Catalan",
            "cop-EG": "Coptic",
            "cs-CZ": "Czech",
            "cy-GB": "Welsh",
            "da-DK": "Danish",
            "dz-BT": "Dzongkha",
            "de-DE": "German",
            "dv-MV": "Maldivian",
            "el-GR": "Greek",
            "en-GB": "English",
            "es-ES": "Spanish",
            "et-EE": "Estonian",
            "eu-ES": "Basque",
            "fa-IR": "Persian",
            "fi-FI": "Finnish",
            "fn-FNG": "Fanagalo",
            "fo-FO": "Faroese",
            "fr-FR": "French",
            "gl-ES": "Galician",
            "gu-IN": "Gujarati",
            "ha-NE": "Hausa",
            "he-IL": "Hebrew",
            "hi-IN": "Hindi",
            "hr-HR": "Croatian",
            "hu-HU": "Hungarian",
            "id-ID": "Indonesian",
            "is-IS": "Icelandic",
            "it-IT": "Italian",
            "ja-JP": "Japanese",
            "kk-KZ": "Kazakh",
            "km-KM": "Khmer",
            "kn-IN": "Kannada",
            "ko-KR": "Korean",
            "ku-TR": "Kurdish",
            "ky-KG": "Kyrgyz",
            "la-VA": "Latin",
            "lo-LA": "Lao",
            "lv-LV": "Latvian",
            "men-SL": "Mende",
            "mg-MG": "Malagasy",
            "mi-NZ": "Maori",
            "ms-MY": "Malay",
            "mt-MT": "Maltese",
            "my-MM": "Burmese",
            "ne-NP": "Nepali",
            "niu-NU": "Niuean",
            "nl-NL": "Dutch",
            "no-NO": "Norwegian",
            "ny-MW": "Nyanja",
            "ur-PK": "Pakistani",
            "pau-PW": "Palauan",
            "pa-IN": "Panjabi",
            "ps-PK": "Pashto",
            "pis-SB": "Pijin",
            "pl-PL": "Polish",
            "pt-PT": "Portuguese",
            "rn-BI": "Kirundi",
            "ro-RO": "Romanian",
            "ru-RU": "Russian",
            "sg-CF": "Sango",
            "si-LK": "Sinhala",
            "sk-SK": "Slovak",
            "sm-WS": "Samoan",
            "sn-ZW": "Shona",
            "so-SO": "Somali",
            "sq-AL": "Albanian",
            "sr-RS": "Serbian",
            "sv-SE": "Swedish",
            "sw-SZ": "Swahili",
            "ta-LK": "Tamil",
            "te-IN": "Telugu",
            "tet-TL": "Tetum",
            "tg-TJ": "Tajik",
            "th-TH": "Thai",
            "ti-TI": "Tigrinya",
            "tk-TM": "Turkmen",
            "tl-PH": "Tagalog",
            "tn-BW": "Tswana",
            "to-TO": "Tongan",
            "tr-TR": "Turkish",
            "uk-UA": "Ukrainian",
            "uz-UZ": "Uzbek",
            "vi-VN": "Vietnamese",
            "wo-SN": "Wolof",
            "xh-ZA": "Xhosa",
            "yi-YD": "Yiddish",
            "zu-ZA": "Zulu",
        }
        return countries
