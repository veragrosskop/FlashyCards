console.log("JS LOADED");
//document.addEventListener("DOMContentLoaded", function () {
//
//    // 🔥 TEMP: HARDCODED DATA (no Django needed)
//    const treeData = [
//        {
//            name: "Spanish",
//            cards: [
//                { native: "Hello", foreign: "Hola" },
//                { native: "Goodbye", foreign: "Adiós" }
//            ],
//            children: [
//                {
//                    name: "Food",
//                    cards: [
//                        { native: "Apple", foreign: "Manzana" }
//                    ],
//                    children: []
//                }
//            ]
//        },
//        {
//            name: "German",
//            cards: [
//                { native: "Hello", foreign: "Hallo" }
//            ],
//            children: []
//        }
//    ];
//
//    const treeContainer = document.getElementById("tree");
//    const details = document.getElementById("tree-details");
//
//    function buildTree(nodes, parent) {
//        nodes.forEach(node => {
//            const wrapper = document.createElement("div");
//            wrapper.className = "tree-node";
//
//            const header = document.createElement("div");
//            header.className = "tree-header";
//            header.innerHTML = `
//                <span class="toggle-icon">▶</span>
//                <span>${node.name}</span>
//            `;
//
//            const content = document.createElement("div");
//            content.className = "tree-content";
//
//            header.addEventListener("click", () => {
//                header.classList.toggle("expanded");
//
//                document.querySelectorAll(".tree-header")
//                    .forEach(h => h.classList.remove("active"));
//                header.classList.add("active");
//
//                showCards(node);
//            });
//
//            wrapper.appendChild(header);
//            wrapper.appendChild(content);
//            parent.appendChild(wrapper);
//
//            buildTree(node.children, content);
//        });
//    }
//
//    function showCards(node) {
//        let html = `<h2>${node.name}</h2>`;
//
//        if (node.cards.length === 0) {
//            html += "<p>No cards</p>";
//        } else {
//            node.cards.forEach(card => {
//                html += `<div>${card.native} ↔ ${card.foreign}</div>`;
//            });
//        }
//
//        details.innerHTML = html;
//    }
//
//    buildTree(treeData, treeContainer);
//});


document.addEventListener("DOMContentLoaded", function () {
    const treeData = JSON.parse(
        document.getElementById("tree-data").textContent
    );

    const treeContainer = document.getElementById("tree");
    const details = document.getElementById("tree-details");

    // Build tree recursively
    function buildTree(nodes, parent) {
        nodes.forEach(node => {
            const wrapper = document.createElement("div");
            wrapper.className = "tree-node";

            const header = document.createElement("div");
            header.className = "tree-header";
            header.innerHTML = `
                <span class="toggle-icon">▶</span>
                <span>${node.name}</span>
            `;

            const content = document.createElement("div");
            content.className = "tree-content";

            header.addEventListener("click", () => {
                header.classList.toggle("expanded");

                document.querySelectorAll(".tree-header")
                    .forEach(h => h.classList.remove("active"));
                header.classList.add("active");

                showCards(node);
            });

            wrapper.appendChild(header);
            wrapper.appendChild(content);
            parent.appendChild(wrapper);

            buildTree(node.children, content);
        });
    }

    // Show cards in right panel
    function showCards(node) {
        let html = `<h2>${node.name}</h2>`;

        if (!node.decks || node.decks.length === 0) {
            html += "<p>No cards in this node.</p>";
            document.getElementById("tree-details").innerHTML = html;
            return;
        }

        node.decks.forEach(deck => {
            html += `<h3>${deck.name}</h3>`;

            if (!deck.cards || deck.cards.length === 0) {
                html += "<p>No cards in this deck.</p>";
            } else {
                // Get the template
                const template = document.getElementById("cards-table-template");
                const tableClone = template.content.cloneNode(true);
                const tbody = tableClone.querySelector("tbody");

                // Populate table rows
                deck.cards.forEach(card => {
                    const tr = document.createElement("tr");
                    tr.innerHTML = `<td>${card.native}</td><td>${card.foreign}</td>`;
                    tbody.appendChild(tr);
                });

                // Append the table to html
                html += tableClone.firstElementChild.outerHTML;
            }
        });
    document.getElementById("tree-details").innerHTML = html;
}

    // Init
    buildTree(treeData, treeContainer);
});