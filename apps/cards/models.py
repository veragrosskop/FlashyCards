from django.db import models

# from django.contrib.auth.models import User

NUM_BOXES = 5

BOXES = range(1, NUM_BOXES + 1)


class LanguageChoice(models.TextChoices):
    AFRIKAANS = "AF", "Afrikaans"
    ALBANIAN = "SQ", "Albanian"
    AMHARIC = "AM", "Amharic"
    ARABIC = "AR", "Arabic"
    ARMENIAN = "HY", "Armenian"
    AZERBAIJANI = "AZ", "Azerbaijani"
    BASQUE = "EU", "Basque"
    BELARUSIAN = "BE", "Belarusian"
    BENGALI = "BN", "Bengali"
    BOSNIAN = "BS", "Bosnian"
    BULGARIAN = "BG", "Bulgarian"
    CATALAN = "CA", "Catalan"
    CEBUANO = "CEB", "Cebuano"
    CHINESE = "ZH", "Chinese"
    CROATIAN = "HR", "Croatian"
    CZECH = "CS", "Czech"
    DANISH = "DA", "Danish"
    DUTCH = "NL", "Dutch"
    ENGLISH = "EN", "English"
    ESPERANTO = "EO", "Esperanto"
    ESTONIAN = "ET", "Estonian"
    FINNISH = "FI", "Finnish"
    FRENCH = "FR", "French"
    GALICIAN = "GL", "Galician"
    GEORGIAN = "KA", "Georgian"
    GERMAN = "DE", "German"
    GREEK = "EL", "Greek"
    GUJARATI = "GU", "Gujarati"
    HAITIAN_CREOLE = "HT", "Haitian Creole"
    HAUSA = "HA", "Hausa"
    HAWAIIAN = "HAW", "Hawaiian"
    HEBREW = "HE", "Hebrew"
    HINDI = "HI", "Hindi"
    HMONG = "HMN", "Hmong"
    HUNGARIAN = "HU", "Hungarian"
    ICELANDIC = "IS", "Icelandic"
    IGBO = "IG", "Igbo"
    INDONESIAN = "ID", "Indonesian"
    IRISH = "GA", "Irish"
    ITALIAN = "IT", "Italian"
    JAPANESE = "JA", "Japanese"
    JAVANESE = "JW", "Javanese"
    KANNADA = "KN", "Kannada"
    KAZAKH = "KK", "Kazakh"
    KHMER = "KM", "Khmer"
    KOREAN = "KO", "Korean"
    KURDISH = "KU", "Kurdish (Kurmanji)"
    KYRGYZ = "KY", "Kyrgyz"
    LAO = "LO", "Lao"
    LATIN = "LA", "Latin"
    LATVIAN = "LV", "Latvian"
    LITHUANIAN = "LT", "Lithuanian"
    LUXEMBOURGISH = "LB", "Luxembourgish"
    MACEDONIAN = "MK", "Macedonian"
    MALAGASY = "MG", "Malagasy"
    MALAY = "MS", "Malay"
    MALAYALAM = "ML", "Malayalam"
    MALTESE = "MT", "Maltese"
    MAORI = "MI", "Maori"
    MARATHI = "MR", "Marathi"
    MONGOLIAN = "MN", "Mongolian"
    MYANMAR = "MY", "Myanmar (Burmese)"
    NEPALI = "NE", "Nepali"
    NORWEGIAN = "NO", "Norwegian"
    CHICHEWA = "NY", "Chichewa"
    PASHTO = "PS", "Pashto"
    PERSIAN = "FA", "Persian"
    POLISH = "PL", "Polish"
    PORTUGUESE = "PT", "Portuguese"
    PUNJABI = "PA", "Punjabi"
    ROMANIAN = "RO", "Romanian"
    RUSSIAN = "RU", "Russian"
    SAMOAN = "SM", "Samoan"
    SCOTS_GAELIC = "GD", "Scots Gaelic"
    SERBIAN = "SR", "Serbian"
    SESOTHO = "ST", "Sesotho"
    SHONA = "SN", "Shona"
    SINDHI = "SD", "Sindhi"
    SINHALA = "SI", "Sinhala"
    SLOVAK = "SK", "Slovak"
    SLOVENIAN = "SL", "Slovenian"
    SOMALI = "SO", "Somali"
    SPANISH = "ES", "Spanish"
    SUNDANESE = "SU", "Sundanese"
    SWAHILI = "SW", "Swahili"
    SWEDISH = "SV", "Swedish"
    TAJIK = "TG", "Tajik"
    TAMIL = "TA", "Tamil"
    TELUGU = "TE", "Telugu"
    THAI = "TH", "Thai"
    TURKISH = "TR", "Turkish"
    UKRAINIAN = "UK", "Ukrainian"
    URDU = "UR", "Urdu"
    UZBEK = "UZ", "Uzbek"
    VIETNAMESE = "VI", "Vietnamese"
    WELSH = "CY", "Welsh"
    XHOSA = "XH", "Xhosa"
    YIDDISH = "YI", "Yiddish"
    YORUBA = "YO", "Yoruba"
    ZULU = "ZU", "Zulu"


class HierarchyType(models.TextChoices):
    """Similar to an Enumerator this defines the type of Hierarchy of a Source."""

    SOURCE = "SOURCE", "Source"
    VOLUME = "VOLUME", "Volume"
    UNIT = "UNIT", "Unit"
    CHAPTER = "CHAPTER", "Chapter"
    SECTION = "SECTION", "Section"
    SUBSECTION = "SUBSECTION", "Subsection"


class HierarchyItem(models.Model):
    """A class which can be defined as any of the HierarchyTypes."""

    title = models.CharField(max_length=255)
    type = models.CharField(
        max_length=20, choices=HierarchyType.choices, default=HierarchyType.SOURCE
    )
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE, related_name="children"
    )

    def __str__(self):
        return f"{self.title} ({self.type})"


class Source(HierarchyItem):
    type = "SOURCE"


class Volume(HierarchyItem):
    type = "VOLUME"


class Unit(HierarchyItem):
    type = "UNIT"


class Chapter(HierarchyItem):
    type = "CHAPTER"


class Section(HierarchyItem):
    type = "SECTION"


class Subsection(HierarchyItem):
    type = "SUBSECTION"


class Deck(models.Model):
    """A deck holds cards and can belong to any Hierarchy level."""

    title = models.CharField(max_length=200)
    parent = models.ForeignKey(
        HierarchyItem,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="decks",
    )
    cards = models.ManyToManyField("Card", blank=True)
    # owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # shared_with = models.ManyToManyField(CustomUser, related_name='shared_decks', blank=True)
    native_language = models.CharField(
        max_length=3, choices=LanguageChoice.choices, default=LanguageChoice.ENGLISH
    )
    foreign_language = models.CharField(
        max_length=3, choices=LanguageChoice.choices, default=LanguageChoice.SPANISH
    )

    def __str__(self):
        return f"{self.title} (Deck under {self.parent})"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "parent"], name="unique_deck_per_parent"
            )
        ]


class DirectionChoice(models.TextChoices):
    """
    Similar to an Enumerator this defines the direction of a flashcard.
    This could be native to foreign or the other way around.
    """

    NATIVE_TO_FOREIGN = "NTF", "Native to Foreign"
    FOREIGN_TO_NATIVE = "FTN", "Foreign to Native"


class Card(models.Model):
    # One Flashcard model storing front/back text card gets flipped in views/templates based on direction.

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    native = models.CharField(max_length=100)
    foreign = models.CharField(max_length=100)
    native_language = models.CharField(
        max_length=3, choices=LanguageChoice.choices, default=LanguageChoice.ENGLISH
    )
    foreign_language = models.CharField(max_length=3, choices=LanguageChoice.choices)

    # Track progress boxes separately per direction
    box_ntf = models.IntegerField(choices=zip(BOXES, BOXES), default=BOXES[0])
    box_ftn = models.IntegerField(choices=zip(BOXES, BOXES), default=BOXES[0])

    sources = models.ManyToManyField(Source, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    # deck = models.ForeignKey('decks.Deck', on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return f"{self.native} -> {self.foreign}"

    def move(self, direction: DirectionChoice, solved: bool) -> None:
        """
        Moves a card to a study box depending on whether it was solved.
        Solved? -> yes -> move a box over
        Solved? -> No -> move back to box 0

        :param direction:
        :param solved:
        :return:
        """
        if direction == DirectionChoice.NATIVE_TO_FOREIGN:
            curr_box = self.box_ntf
        elif direction == DirectionChoice.FOREIGN_TO_NATIVE:
            curr_box = self.box_ftn
        else:
            raise ValueError(f"Could not find direction: {direction}.")

        new_box = curr_box + 1 if solved else BOXES[0]

        if new_box in BOXES:
            if direction == DirectionChoice.NATIVE_TO_FOREIGN:
                self.box_ntf = new_box
            if direction == DirectionChoice.FOREIGN_TO_NATIVE:
                self.box_ftn = new_box
            self.save()

    def get_text(self, direction: DirectionChoice) -> str:
        """
        Dynamically return the card text in the correct direction (native, foreign) or (foreign, native)
        """
        if direction == DirectionChoice.NATIVE_TO_FOREIGN:
            return self.native, self.foreign
        elif direction == DirectionChoice.FOREIGN_TO_NATIVE:
            return self.foreign, self.native
        else:
            raise ValueError(f"Could not find direction: {direction}.")

    def supports_language_pair(
        self, lang1: LanguageChoice, lang2: LanguageChoice
    ) -> bool:
        return {self.native_language, self.foreign_language} == {lang1, lang2}
