from django.test import TestCase
from django.urls import reverse
from .models import Deck, Card, LanguageChoice, HierarchyItem


class CardsViewTest(TestCase):

    def setUp(self):
        """Create some test data"""

        # ensure there is a root hierarchy
        self.root = HierarchyItem.objects.create(
            name="My Spanish Source", type="SOURCE"
        )
        self.volume = HierarchyItem.objects.create(
            name="Test Volume", type="VOLUME", parent=self.root
        )
        self.unit = HierarchyItem.objects.create(
            name="Test Unit", type="UNIT", parent=self.volume
        )
        self.chapter = HierarchyItem.objects.create(
            name="Test Chapter", type="CHAPTER", parent=self.unit
        )
        self.section = HierarchyItem.objects.create(
            name="Test Section", type="SECTION", parent=self.chapter
        )
        self.subsection = HierarchyItem.objects.create(
            name="Test Subsection", type="SUBSECTION", parent=self.section
        )
        # deck1
        self.deck1 = Deck.objects.create(name="Test Deck1", parent=self.volume)
        self.card1 = Card.objects.create(
            native="Hello", foreign="Hola", foreign_language=LanguageChoice.SPANISH
        )
        self.card2 = Card.objects.create(
            native="Bye", foreign="Adiós", foreign_language=LanguageChoice.SPANISH
        )
        self.deck1.cards.add(self.card1, self.card2)

        # deck2
        self.deck2 = Deck.objects.create(name="Test Deck2", parent=self.unit)
        self.card3 = Card.objects.create(
            native="Yes", foreign="Sí", foreign_language=LanguageChoice.SPANISH
        )
        self.card4 = Card.objects.create(
            native="No", foreign="No", foreign_language=LanguageChoice.SPANISH
        )
        self.deck2.cards.add(self.card3, self.card4)

    def test_cards_view_status_code(self):
        response = self.client.get(reverse("cards:decks"))  # use your URL name
        self.assertEqual(response.status_code, 200)

    def test_cards_view_template_used(self):
        response = self.client.get(reverse("cards:decks"))
        self.assertTemplateUsed(response, "cards/decks.html")

    def test_tree_structure_in_context(self):
        response = self.client.get(reverse("cards:decks"))
        self.assertIn("tree", response.context)

        tree = response.context["tree"]
        # --- Check root ---
        self.assertEqual(len(tree), 1)
        root_node = tree[0]
        self.assertEqual(root_node["name"], "My Spanish Source")  # if you use title
        self.assertEqual(root_node["type"], "SOURCE")

        # --- Check top-level deck under volume ---
        decks = root_node["decks"]
        self.assertEqual(len(decks), 0)
        volume = root_node["children"][0]
        volume_decks = volume["decks"]
        self.assertEqual(volume_decks[0]["name"], "Test Deck1")
        self.assertEqual(len(volume_decks[0]["cards"]), 2)
        self.assertEqual(volume_decks[0]["cards"][0]["native"], "Hello")
        self.assertEqual(volume_decks[0]["cards"][1]["foreign"], "Adiós")

        # --- Check children hierarchies ---
        unit = volume["children"][0]
        unit_decks = unit["decks"]
        self.assertEqual(len(unit), 5)
        self.assertEqual(unit["name"], "Test Unit")
        self.assertEqual(unit["type"], "UNIT")

        # --- Check nested deck under child ---
        self.assertEqual(len(unit_decks), 1)
        self.assertEqual(unit_decks[0]["name"], "Test Deck2")
        self.assertEqual(len(unit_decks[0]["cards"]), 2)
        self.assertEqual(unit_decks[0]["cards"][0]["native"], "Yes")
        self.assertEqual(unit_decks[0]["cards"][1]["foreign"], "No")
