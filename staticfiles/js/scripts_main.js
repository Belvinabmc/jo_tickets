document.addEventListener("DOMContentLoaded", function () {
    fetch("/api/events/")
        .then(response => {
            if (!response.ok) {
                throw new Error("Erreur lors de la récupération des événements.");
            }
            return response.json();
        })
        .then(data => {
            const container = document.getElementById("events");
            container.innerHTML = "";

            if (data.length === 0) {
                container.innerHTML = "<p>Aucun match disponible pour le moment.</p>";
                return;
            }

            data.forEach(event => {
                const match = document.createElement("div");
                match.innerHTML = `
                    <h3>${event.team_home.name} vs ${event.team_away.name}</h3>
                    <p><strong>Stade :</strong> ${event.stadium.name}</p>
                    <p><strong>Date :</strong> ${event.date}</p>
                    <button onclick="acheterBillet(${event.id})">Acheter un billet</button>
                    <hr>
                `;
                container.appendChild(match);
            });
        })
        .catch(error => {
            document.getElementById("events").innerText = "Erreur lors du chargement des matchs.";
            console.error("Erreur de chargement :", error);
        });
});

function acheterBillet(eventId) {
    fetch("/api/tickets/buy/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ event: eventId })
    })
        .then(response => response.json())
        .then(data => {
            alert('Billet généré avec le QR code : ${data.qr_code}');
        })
        .catch(error => {
            alert("Erreur lors de l'achat du billet.");
            console.error("Erreur :", error);
        });
}
console.log("script.js chargé !");