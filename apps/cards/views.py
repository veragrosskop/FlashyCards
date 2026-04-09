from typing import List

from django.shortcuts import render
from .models import Deck, HierarchyItem
from django.http import HttpResponse


# --- Views ---
def decks(request):
    """
    Shows a tree view of all decks.
    :param request:
    :return:
    """
    hierarchy = HierarchyItem.objects.prefetch_related("children", "decks__cards")
    tree = build_tree(all_items=hierarchy)

    return render(request, "cards/decks.html", {"tree": tree})


# --- Helper Functions ----


def build_tree(parent=None, all_items=None) -> List[dict]:
    """Given a deck of cards, builds a tree view of all the cards in the deck, under the correct parent."""
    nodes = []
    for item in all_items.filter(parent=parent):
        nodes.append(
            {
                "id": item.id,
                "name": item.name,
                "type": item.type,  # this can be source, volume, chapter etc
                # iterate over the decks
                "decks": [
                    {
                        "id": deck.id,
                        "name": deck.name,
                        "cards": [
                            {"native": card.native, "foreign": card.foreign}
                            for card in deck.cards.all()
                        ],
                    }
                    for deck in item.decks.all()
                ],
                # recursive children of hierarchy item
                "children": build_tree(parent=item, all_items=all_items),
            }
        )
    return nodes
