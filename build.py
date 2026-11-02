# Génère le site légal d'Orion Cadets (GitHub Pages) en 4 langues : fr, en, es, pt.
#
#   python build.py
#
# Modifier un texte : changer le bloc de la langue dans LANGS, relancer le script, puis publier
# (git add/commit/push). Ne pas modifier les .html à la main : ils sont réécrits à chaque génération.
import html
import os
import shutil
from urllib.parse import quote

HERE = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "https://oliv66001.github.io/orion-cadets-legal/"
GAME = "Orion Cadets"
EMAIL = "developpement.solution@gmail.com"
PUBLISHER = "Développement-Solution — Olivier Pagé"
ADDRESS = "20 rue Condorcet, 66330 Cabestany, France"
PAGES = ["index", "privacy", "delete-account", "contact"]


def mail(subject, body=""):
    url = f"mailto:{EMAIL}?subject={quote(subject)}"
    if body:
        url += f"&body={quote(body)}"
    return html.escape(url, quote=True)


def delete_mail(subject, hello, ask, used):
    return mail(GAME + " - " + subject, hello + chr(10) + chr(10) + ask + chr(10) + used + chr(10))


LANGS = {
    # ------------------------------------------------------------------ FRANÇAIS
    "fr": {
        "name": "Français",
        "date": "2 novembre 2026",
        "updated": "Dernière mise à jour",
        "nav": {"index": "Accueil", "privacy": "Confidentialité",
                "delete-account": "Suppression du compte et des données", "contact": "Contact et éditeur"},
        "titles": {"index": "Informations légales et assistance", "privacy": "Politique de confidentialité",
                   "delete-account": "Suppression du compte et des données",
                   "contact": "Contact et informations sur l’éditeur"},
        "index": lambda: f"""
<p>{GAME} est un jeu de tir spatial : vous incarnez un élève pilote de l’Académie d’Orion qui défend les colonies
humaines contre la Nuée, à travers 50 niveaux, des missions variées et des boss géants qui se transforment.</p>
<p>Éditeur : {PUBLISHER}, France.</p>
<p>Le jeu enregistre la progression, les cristaux, les vaisseaux débloqués et les réglages <strong>sur l’appareil</strong>.
Le compte joueur est le compte Google Play Jeux (sauvegarde cloud, réussites, classements). Il peut afficher des publicités Google AdMob et proposer des achats intégrés
via Google Play. S’il est connecté à Google Play Jeux, la progression, les réussites et les scores peuvent être
enregistrés chez Google (voir la politique de confidentialité).</p>
""",
        "privacy": lambda: f"""
<h2>Responsable et contact</h2>
<p>Le responsable du traitement est {PUBLISHER}, {ADDRESS}.</p>
<p>Pour toute question relative aux données :
<a href="{mail(GAME + ' - Données personnelles')}">{EMAIL}</a>.</p>

<h2>Données enregistrées par le jeu</h2>
<p>Le jeu conserve sur l’appareil : la progression (niveaux débloqués et réussis, meilleurs scores, temps du
simulateur), les cristaux, les vaisseaux et éléments débloqués, le vaisseau choisi, et les réglages (langue, volumes de
la musique, des voix et des bruitages, histoire déjà vue). Ces données ne sont pas transmises à l’éditeur.</p>
<p>Le jeu ne demande ni nom, ni adresse e-mail, ni âge, ni localisation, et n’accède ni aux contacts, ni au micro, ni à
l’appareil photo, ni aux fichiers. Il ne contient ni messagerie ni échange entre joueurs. Les voix et la musique sont
intégrées au jeu : aucun enregistrement de votre voix n’est réalisé.</p>

<h2>Google Play Jeux (sauvegarde, réussites, classements)</h2>
<p>Si vous vous connectez à <strong>Google Play Jeux</strong>, le jeu peut envoyer à Google votre progression
(sauvegarde dans le cloud), les réussites débloquées et vos meilleurs scores ; Google les associe à votre profil Play Jeux
(pseudo et avatar) et peut afficher les classements aux autres joueurs selon vos paramètres de visibilité. L’éditeur ne
reçoit pas votre adresse e-mail et ne stocke pas ces données sur ses propres serveurs.</p>
<p>Ce traitement est réalisé par Google LLC / Google Ireland Limited selon sa
<a href="https://policies.google.com/privacy">politique de confidentialité</a>. La connexion est facultative : le jeu
fonctionne entièrement sans elle.</p>

<h2>Publicité, achats et statistiques</h2>
<p><strong>Publicités.</strong> Le jeu peut afficher des publicités fournies par <strong>Google AdMob</strong>
(Google LLC / Google Ireland Limited) : des vidéos récompensées que vous choisissez de regarder (continuer une partie,
doubler les cristaux gagnés, obtenir un bonus au départ) et, au plus une fois toutes les quelques parties, une publicité
plein écran entre deux niveaux. Pour afficher et mesurer ces publicités, AdMob traite des données de l’appareil :
identifiant publicitaire, adresse IP, informations techniques et interactions avec les annonces, selon la
<a href="https://policies.google.com/technologies/ads">politique de Google sur la publicité</a>.</p>
<p><strong>Consentement.</strong> Dans l’Espace économique européen, au Royaume-Uni et en Suisse, un formulaire de
consentement certifié (Google UMP) s’affiche avant toute publicité. Vous pouvez refuser les publicités personnalisées et
modifier votre choix à tout moment dans le jeu : <strong>Options → Choix publicités (RGPD)</strong>. Vous pouvez aussi
réinitialiser ou supprimer l’identifiant publicitaire dans les paramètres de votre téléphone (Google → Annonces).</p>
<p><strong>Achats intégrés.</strong> Les achats (pack sans publicité, cristaux, vaisseaux, apparences) sont traités par
Google Play. L’éditeur ne reçoit ni vos coordonnées bancaires ni votre adresse e-mail ; le jeu enregistre seulement ce
que vous avez acheté.</p>
<p>Le jeu n’intègre aucun autre outil de statistiques ou de suivi.</p>

<h2>Liens externes</h2>
<p>Les liens du jeu vers ces pages s’ouvrent dans votre navigateur. GitHub Pages, qui héberge ces pages, peut
enregistrer des informations techniques (adresse IP, type de navigateur) dans ses journaux de sécurité, selon sa propre
politique de confidentialité.</p>

<h2>Enfants</h2>
<p>{GAME} n’est pas destiné aux enfants de moins de 13 ans et ne collecte pas sciemment de données personnelles auprès
d’eux. Si vous pensez qu’un enfant nous a transmis des données (par exemple par e-mail), contactez-nous afin que nous
les supprimions.</p>

<h2>Assistance par e-mail</h2>
<p>Lorsque vous contactez l’éditeur, votre adresse e-mail, le contenu de votre message et les éventuelles pièces jointes
sont traités pour répondre à votre demande, traiter un incident ou exercer vos droits. La base juridique est l’intérêt
légitime de l’éditeur à assurer l’assistance. Ces données sont accessibles à l’éditeur et au fournisseur de messagerie
utilisé, et conservées le temps nécessaire, puis au plus trois ans après le dernier échange, sauf obligation légale ou
litige. N’envoyez ni mot de passe ni coordonnées bancaires par e-mail.</p>

<h2>Conservation, suppression et droits</h2>
<p>Les données de jeu restent sur l’appareil jusqu’à ce que vous les effaciez (dans le jeu ou dans les paramètres du
téléphone) ou que vous désinstalliez le jeu : voir <a href="delete-account.html">la page de suppression du compte et des
données</a>. Vous pouvez demander l’accès, la rectification, l’effacement, la limitation, l’opposition ou la portabilité
lorsque le droit applicable le prévoit, à l’adresse ci-dessus, et introduire une réclamation auprès de la
<a href="https://www.cnil.fr/fr/plaintes">CNIL</a>.</p>

<h2>Sécurité</h2>
<p>Le jeu limite ses données à celles décrites ci-dessus. Les messages d’assistance ne sont accessibles qu’à l’éditeur.
Aucun système n’est totalement exempt de risque ; ne transmettez pas de données sensibles inutiles.</p>

<h2>Modifications</h2>
<p>Cette politique peut évoluer, notamment en cas d’ajout d’un compte joueur ou d’un mode en ligne. La date de mise à
jour en haut de page sera modifiée et, si le changement est important, il sera signalé dans le jeu ou sur la fiche
Google Play.</p>
""",
        "delete-account": lambda: f"""
<p>Cette page explique comment supprimer les données de <strong>{GAME}</strong>, édité par
<strong>{PUBLISHER}</strong>.</p>

<h2>Compte joueur (Google Play Jeux)</h2>
<p>Dans {GAME}, votre compte joueur est votre compte <strong>Google Play Jeux</strong> : il sert à sauvegarder votre
progression dans le cloud (histoire, cristaux, vaisseaux), à la retrouver sur un autre téléphone, et à afficher vos
réussites et classements. L’éditeur ne crée pas d’identifiant ni de mot de passe et n’a pas de serveur de comptes : ces
données sont gérées par Google.</p>
<p><strong>Supprimer le compte et ses données :</strong></p>
<ul>
<li><strong>Dans le jeu :</strong> écran d’accueil → <strong>Options</strong> → <strong>Effacer mes données</strong> →
confirmez. Cela efface la sauvegarde du téléphone <strong>et</strong> la sauvegarde cloud du jeu associée à votre
compte Play Jeux, puis vous déconnecte.</li>
<li><strong>Chez Google :</strong> application <strong>Google Play Jeux</strong> → <strong>Paramètres</strong> →
<strong>Supprimer le compte et les données Play Jeux</strong> (ou seulement les données de {GAME}), ou depuis
<a href="https://myaccount.google.com/data-and-privacy">les paramètres de votre compte Google</a>.</li>
<li><strong>Par e-mail :</strong> si vous ne pouvez plus ouvrir le jeu, utilisez le bouton ci-dessous ; nous vous
indiquerons la marche à suivre et supprimerons toute donnée que nous détiendrions.</li>
</ul>

<h2>Supprimer les données de jeu</h2>
<p>La progression, les cristaux, les vaisseaux débloqués et les réglages sont enregistrés sur l’appareil. Pour les effacer :</p>
<ul>
<li><strong>Dans le jeu :</strong> écran d’accueil → <strong>Options</strong> → <strong>Effacer mes données</strong>,
puis confirmez.</li>
<li><strong>Sur Android :</strong> <strong>Paramètres</strong> du téléphone → <strong>Applications</strong> →
<strong>{GAME}</strong> → <strong>Stockage</strong> → <strong>Effacer les données</strong>.</li>
</ul>
<p>Désinstaller le jeu supprime aussi ces données. Les intitulés peuvent varier selon le téléphone ; pensez également aux
éventuelles sauvegardes automatiques du système (sauvegarde Google). Les achats faits sur Google Play restent liés à
votre compte Google et peuvent être restaurés.</p>

<h2>Demander la suppression des données détenues par l’éditeur</h2>
<p>Si vous avez écrit à l’assistance, vous pouvez demander la suppression de vos échanges et de votre adresse e-mail :</p>
<p><a class="button" href="{delete_mail('Suppression de données', 'Bonjour,', 'Je demande la suppression de mes données liées à ' + GAME + '.', 'Adresse e-mail utilisée pour contacter l’assistance :')}">Demander la suppression de mes données</a></p>
<ul>
<li><strong>Données supprimées :</strong> vos messages, pièces jointes et votre adresse e-mail.</li>
<li><strong>Délai :</strong> au plus 30 jours après la réception de votre demande. Une confirmation vous est envoyée.</li>
<li><strong>Conservation éventuelle :</strong> uniquement ce qu’une obligation légale ou un litige en cours impose de
garder, et seulement pendant la durée nécessaire.</li>
</ul>

<p>Plus d’informations : <a href="privacy.html">politique de confidentialité</a>.</p>
""",
        "contact": lambda: f"""
<ul>
<li>Éditeur : {PUBLISHER}.</li>
<li>Adresse : {ADDRESS}.</li>
<li>E-mail : <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
</ul>
<p><a class="button" href="{mail(GAME + ' - Assistance')}">Contacter l’assistance</a></p>
<p>Musiques : Pixabay (licence Pixabay). Hébergement des présentes pages : GitHub Pages, fourni par GitHub, Inc.,
88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</p>
""",
    },

    # ------------------------------------------------------------------ ENGLISH
    "en": {
        "name": "English",
        "date": "November 2, 2026",
        "updated": "Last updated",
        "nav": {"index": "Home", "privacy": "Privacy",
                "delete-account": "Account and data deletion", "contact": "Contact and publisher"},
        "titles": {"index": "Legal information and support", "privacy": "Privacy policy",
                   "delete-account": "Account and data deletion", "contact": "Contact and publisher information"},
        "index": lambda: f"""
<p>{GAME} is a space shooter: you play a student pilot of the Orion Academy defending the human colonies against the
Swarm, across 50 levels, varied missions and giant transforming bosses.</p>
<p>Publisher: {PUBLISHER}, France.</p>
<p>The game stores progress, crystals, unlocked ships and settings <strong>on the device</strong>. The player account is the Google Play Games account (cloud save,
achievements, leaderboards). It may show Google AdMob ads and offer in-app purchases through Google Play. If connected to Google
Play Games, progress, achievements and scores may be saved by Google (see the privacy policy).</p>
""",
        "privacy": lambda: f"""
<h2>Controller and contact</h2>
<p>The data controller is {PUBLISHER}, {ADDRESS}.</p>
<p>For any question about data: <a href="{mail(GAME + ' - Personal data')}">{EMAIL}</a>.</p>

<h2>Data stored by the game</h2>
<p>The game keeps on the device: progress (unlocked and completed levels, best scores, simulator times), crystals,
unlocked ships and items, the selected ship, and settings (language, music, voice and sound effect volumes, story
already seen). This data is not sent to the publisher.</p>
<p>The game does not ask for your name, email address, age or location, and does not access contacts, microphone,
camera or files. It has no chat or player-to-player exchange. Voices and music are built into the game: your voice is
never recorded.</p>

<h2>Google Play Games (cloud save, achievements, leaderboards)</h2>
<p>If you sign in to <strong>Google Play Games</strong>, the game may send Google your progress (cloud save), unlocked
achievements and best scores; Google links them to your Play Games profile (gamer name and avatar) and may show
leaderboards to other players according to your visibility settings. The publisher does not receive your email address
and does not store this data on its own servers.</p>
<p>This processing is carried out by Google LLC / Google Ireland Limited under its
<a href="https://policies.google.com/privacy">privacy policy</a>. Signing in is optional: the game works fully without it.</p>

<h2>Advertising, purchases and analytics</h2>
<p><strong>Ads.</strong> The game may show ads provided by <strong>Google AdMob</strong> (Google LLC / Google Ireland
Limited): rewarded videos you choose to watch (continue a game, double earned crystals, start with a bonus) and, at most
once every few games, a full-screen ad between two levels. To serve and measure these ads, AdMob processes device data:
advertising ID, IP address, technical information and ad interactions, under
<a href="https://policies.google.com/technologies/ads">Google’s advertising policy</a>.</p>
<p><strong>Consent.</strong> In the European Economic Area, the United Kingdom and Switzerland, a certified consent form
(Google UMP) is shown before any ad. You can refuse personalized ads and change your choice at any time in the game:
<strong>Options → Ad choices (GDPR)</strong>. You can also reset or delete the advertising ID in your phone settings
(Google → Ads).</p>
<p><strong>In-app purchases.</strong> Purchases (no-ads pack, crystals, ships, skins) are processed by Google Play. The
publisher receives neither your payment details nor your email address; the game only stores what you bought.</p>
<p>The game includes no other analytics or tracking tool.</p>

<h2>External links</h2>
<p>Links from the game to these pages open in your browser. GitHub Pages, which hosts these pages, may log technical
information (IP address, browser type) in its security logs, under its own privacy policy.</p>

<h2>Children</h2>
<p>{GAME} is not directed at children under 13 and does not knowingly collect personal data from them. If you believe a
child has sent us data (for example by email), contact us and we will delete it.</p>

<h2>Email support</h2>
<p>When you contact the publisher, your email address, the content of your message and any attachments are processed to
answer your request, handle an issue or exercise your rights. The legal basis is the publisher’s legitimate interest in
providing support. This data is accessible to the publisher and the email provider used, and kept as long as needed,
then at most three years after the last exchange, unless required by law or a dispute. Do not send passwords or bank
details by email.</p>

<h2>Retention, deletion and rights</h2>
<p>Game data stays on the device until you erase it (in the game or in the phone settings) or uninstall the game: see
<a href="delete-account.html">the account and data deletion page</a>. You may request access, rectification, erasure,
restriction, objection or portability where applicable law provides, at the address above, and lodge a complaint with
your data protection authority (in France, the <a href="https://www.cnil.fr/fr/plaintes">CNIL</a>).</p>

<h2>Security</h2>
<p>The game limits its data to what is described above. Support messages are only accessible to the publisher. No system
is completely risk-free; do not send unnecessary sensitive data.</p>

<h2>Changes</h2>
<p>This policy may change, especially if a player account or online mode is added. The date at the top of the page will
be updated and, for significant changes, it will be announced in the game or on the Google Play listing.</p>
""",
        "delete-account": lambda: f"""
<p>This page explains how to delete the data of <strong>{GAME}</strong>, published by <strong>{PUBLISHER}</strong>.</p>

<h2>Player account (Google Play Games)</h2>
<p>In {GAME}, your player account is your <strong>Google Play Games</strong> account: it saves your progress in the cloud
(story, crystals, ships), restores it on another phone, and shows your achievements and leaderboards. The publisher
creates no username or password and runs no account server: this data is managed by Google.</p>
<p><strong>Delete the account and its data:</strong></p>
<ul>
<li><strong>In the game:</strong> home screen → <strong>Options</strong> → <strong>Erase my data</strong> → confirm. This
erases the save on the phone <strong>and</strong> the game’s cloud save linked to your Play Games account, then signs you
out.</li>
<li><strong>At Google:</strong> <strong>Google Play Games</strong> app → <strong>Settings</strong> → <strong>Delete Play
Games account and data</strong> (or only the data of {GAME}), or from
<a href="https://myaccount.google.com/data-and-privacy">your Google Account settings</a>.</li>
<li><strong>By email:</strong> if you can no longer open the game, use the button below; we will guide you and delete any
data we may hold.</li>
</ul>

<h2>Delete game data</h2>
<p>Progress, crystals, unlocked ships and settings are stored on the device. To erase them:</p>
<ul>
<li><strong>In the game:</strong> home screen → <strong>Options</strong> → <strong>Erase my data</strong>, then confirm.</li>
<li><strong>On Android:</strong> phone <strong>Settings</strong> → <strong>Apps</strong> → <strong>{GAME}</strong> →
<strong>Storage</strong> → <strong>Clear data</strong>.</li>
</ul>
<p>Uninstalling the game also deletes this data. Labels may vary by phone; also consider automatic system backups
(Google backup). Purchases made on Google Play remain linked to your Google account and can be restored.</p>

<h2>Request deletion of data held by the publisher</h2>
<p>If you have written to support, you can request the deletion of your messages and email address:</p>
<p><a class="button" href="{delete_mail('Data deletion', 'Hello,', 'I request the deletion of my data related to ' + GAME + '.', 'Email address used to contact support:')}">Request deletion of my data</a></p>
<ul>
<li><strong>Data deleted:</strong> your messages, attachments and email address.</li>
<li><strong>Timeframe:</strong> within 30 days of receiving your request. A confirmation is sent to you.</li>
<li><strong>Possible retention:</strong> only what a legal obligation or ongoing dispute requires, and only for as long
as necessary.</li>
</ul>

<p>More information: <a href="privacy.html">privacy policy</a>.</p>
""",
        "contact": lambda: f"""
<ul>
<li>Publisher: {PUBLISHER}.</li>
<li>Address: {ADDRESS}.</li>
<li>Email: <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
</ul>
<p><a class="button" href="{mail(GAME + ' - Support')}">Contact support</a></p>
<p>Music: Pixabay (Pixabay license). These pages are hosted by GitHub Pages, provided by GitHub, Inc.,
88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, United States.</p>
""",
    },

    # ------------------------------------------------------------------ ESPAÑOL
    "es": {
        "name": "Español",
        "date": "2 de noviembre de 2026",
        "updated": "Última actualización",
        "nav": {"index": "Inicio", "privacy": "Privacidad",
                "delete-account": "Eliminación de la cuenta y de los datos", "contact": "Contacto y editor"},
        "titles": {"index": "Información legal y asistencia", "privacy": "Política de privacidad",
                   "delete-account": "Eliminación de la cuenta y de los datos",
                   "contact": "Contacto e información del editor"},
        "index": lambda: f"""
<p>{GAME} es un juego de disparos espacial: eres un piloto en formación de la Academia de Orión que defiende las
colonias humanas contra el Enjambre, a lo largo de 50 niveles, misiones variadas y jefes gigantes que se transforman.</p>
<p>Editor: {PUBLISHER}, Francia.</p>
<p>El juego guarda el progreso, los cristales, las naves desbloqueadas y los ajustes <strong>en el dispositivo</strong>.
La cuenta de jugador es la de Google Play Juegos (guardado en la nube, logros, clasificaciones). Puede mostrar anuncios de Google AdMob y ofrecer compras integradas a través de Google
Play. Si está conectado a Google Play Juegos, el progreso, los logros y las puntuaciones pueden guardarse en Google
(ver la política de privacidad).</p>
""",
        "privacy": lambda: f"""
<h2>Responsable y contacto</h2>
<p>El responsable del tratamiento es {PUBLISHER}, {ADDRESS}.</p>
<p>Para cualquier pregunta sobre los datos: <a href="{mail(GAME + ' - Datos personales')}">{EMAIL}</a>.</p>

<h2>Datos guardados por el juego</h2>
<p>El juego conserva en el dispositivo: el progreso (niveles desbloqueados y superados, mejores puntuaciones, tiempos
del simulador), los cristales, las naves y elementos desbloqueados, la nave elegida y los ajustes (idioma, volumen de la
música, las voces y los efectos, historia ya vista). Estos datos no se envían al editor.</p>
<p>El juego no pide nombre, correo electrónico, edad ni ubicación, y no accede a los contactos, al micrófono, a la cámara
ni a los archivos. No tiene chat ni intercambios entre jugadores. Las voces y la música están integradas en el juego:
nunca se graba tu voz.</p>

<h2>Google Play Juegos (guardado en la nube, logros, clasificaciones)</h2>
<p>Si inicias sesión en <strong>Google Play Juegos</strong>, el juego puede enviar a Google tu progreso (guardado en la
nube), los logros desbloqueados y tus mejores puntuaciones; Google los asocia a tu perfil de Play Juegos (nombre de
jugador y avatar) y puede mostrar las clasificaciones a otros jugadores según tu configuración de visibilidad. El editor
no recibe tu correo electrónico y no almacena estos datos en sus propios servidores.</p>
<p>Este tratamiento lo realiza Google LLC / Google Ireland Limited según su
<a href="https://policies.google.com/privacy">política de privacidad</a>. Iniciar sesión es opcional: el juego funciona
por completo sin ello.</p>

<h2>Publicidad, compras y estadísticas</h2>
<p><strong>Anuncios.</strong> El juego puede mostrar anuncios de <strong>Google AdMob</strong> (Google LLC / Google
Ireland Limited): vídeos con recompensa que eliges ver (continuar una partida, duplicar los cristales ganados, empezar con
una mejora) y, como máximo una vez cada pocas partidas, un anuncio a pantalla completa entre dos niveles. Para mostrar y
medir estos anuncios, AdMob trata datos del dispositivo: identificador de publicidad, dirección IP, información técnica e
interacciones con los anuncios, según la <a href="https://policies.google.com/technologies/ads">política de publicidad
de Google</a>.</p>
<p><strong>Consentimiento.</strong> En el Espacio Económico Europeo, el Reino Unido y Suiza se muestra un formulario de
consentimiento certificado (Google UMP) antes de cualquier anuncio. Puedes rechazar los anuncios personalizados y
cambiar tu elección en cualquier momento en el juego: <strong>Opciones → Preferencias de anuncios (RGPD)</strong>.
También puedes restablecer o eliminar el identificador de publicidad en los ajustes del teléfono (Google → Anuncios).</p>
<p><strong>Compras integradas.</strong> Las compras (pack sin anuncios, cristales, naves, aspectos) las procesa Google
Play. El editor no recibe tus datos bancarios ni tu correo electrónico; el juego solo guarda lo que has comprado.</p>
<p>El juego no incluye ninguna otra herramienta de estadísticas o seguimiento.</p>

<h2>Enlaces externos</h2>
<p>Los enlaces del juego a estas páginas se abren en tu navegador. GitHub Pages, que aloja estas páginas, puede
registrar información técnica (dirección IP, tipo de navegador) en sus registros de seguridad, según su propia política
de privacidad.</p>

<h2>Menores</h2>
<p>{GAME} no está dirigido a menores de 13 años y no recopila a sabiendas datos personales de ellos. Si crees que un menor
nos ha enviado datos (por ejemplo por correo electrónico), contáctanos para que los eliminemos.</p>

<h2>Asistencia por correo electrónico</h2>
<p>Cuando contactas con el editor, tu correo electrónico, el contenido de tu mensaje y los posibles archivos adjuntos se
tratan para responder a tu solicitud, resolver una incidencia o ejercer tus derechos. La base jurídica es el interés
legítimo del editor en prestar asistencia. Estos datos son accesibles para el editor y el proveedor de correo utilizado,
y se conservan el tiempo necesario y, como máximo, tres años después del último intercambio, salvo obligación legal o
litigio. No envíes contraseñas ni datos bancarios por correo.</p>

<h2>Conservación, eliminación y derechos</h2>
<p>Los datos del juego permanecen en el dispositivo hasta que los borres (en el juego o en los ajustes del teléfono) o
desinstales el juego: consulta <a href="delete-account.html">la página de eliminación de la cuenta y de los datos</a>.
Puedes solicitar el acceso, la rectificación, la supresión, la limitación, la oposición o la portabilidad cuando la ley
aplicable lo prevea, en la dirección indicada, y presentar una reclamación ante tu autoridad de protección de datos.</p>

<h2>Seguridad</h2>
<p>El juego limita sus datos a los descritos arriba. Los mensajes de asistencia solo son accesibles para el editor.
Ningún sistema está totalmente libre de riesgos; no envíes datos sensibles innecesarios.</p>

<h2>Cambios</h2>
<p>Esta política puede cambiar, sobre todo si se añade una cuenta de jugador o un modo en línea. La fecha de la parte
superior se actualizará y, si el cambio es importante, se anunciará en el juego o en la ficha de Google Play.</p>
""",
        "delete-account": lambda: f"""
<p>Esta página explica cómo eliminar los datos de <strong>{GAME}</strong>, publicado por <strong>{PUBLISHER}</strong>.</p>

<h2>Cuenta de jugador (Google Play Juegos)</h2>
<p>En {GAME}, tu cuenta de jugador es tu cuenta de <strong>Google Play Juegos</strong>: guarda tu progreso en la nube
(historia, cristales, naves), lo recupera en otro teléfono y muestra tus logros y clasificaciones. El editor no crea
usuario ni contraseña y no tiene servidor de cuentas: estos datos los gestiona Google.</p>
<p><strong>Eliminar la cuenta y sus datos:</strong></p>
<ul>
<li><strong>En el juego:</strong> pantalla de inicio → <strong>Opciones</strong> → <strong>Borrar mis datos</strong> →
confirma. Esto borra el guardado del teléfono <strong>y</strong> el guardado en la nube del juego vinculado a tu cuenta
de Play Juegos, y cierra la sesión.</li>
<li><strong>En Google:</strong> aplicación <strong>Google Play Juegos</strong> → <strong>Ajustes</strong> →
<strong>Eliminar la cuenta y los datos de Play Juegos</strong> (o solo los datos de {GAME}), o desde
<a href="https://myaccount.google.com/data-and-privacy">la configuración de tu cuenta de Google</a>.</li>
<li><strong>Por correo:</strong> si ya no puedes abrir el juego, usa el botón de abajo; te indicaremos los pasos y
eliminaremos cualquier dato que tengamos.</li>
</ul>

<h2>Eliminar los datos del juego</h2>
<p>El progreso, los cristales, las naves desbloqueadas y los ajustes se guardan en el dispositivo. Para borrarlos:</p>
<ul>
<li><strong>En el juego:</strong> pantalla de inicio → <strong>Opciones</strong> → <strong>Borrar mis datos</strong> y
confirma.</li>
<li><strong>En Android:</strong> <strong>Ajustes</strong> del teléfono → <strong>Aplicaciones</strong> →
<strong>{GAME}</strong> → <strong>Almacenamiento</strong> → <strong>Borrar datos</strong>.</li>
</ul>
<p>Desinstalar el juego también elimina estos datos. Los nombres pueden variar según el teléfono; ten en cuenta también
las copias de seguridad automáticas del sistema (copia de seguridad de Google). Las compras realizadas en Google Play
siguen vinculadas a tu cuenta de Google y pueden restaurarse.</p>

<h2>Solicitar la eliminación de los datos que conserva el editor</h2>
<p>Si has escrito a la asistencia, puedes solicitar la eliminación de tus mensajes y de tu correo electrónico:</p>
<p><a class="button" href="{delete_mail('Eliminación de datos', 'Hola,', 'Solicito la eliminación de mis datos relacionados con ' + GAME + '.', 'Correo electrónico usado para contactar con la asistencia:')}">Solicitar la eliminación de mis datos</a></p>
<ul>
<li><strong>Datos eliminados:</strong> tus mensajes, archivos adjuntos y correo electrónico.</li>
<li><strong>Plazo:</strong> como máximo 30 días desde la recepción de tu solicitud. Recibirás una confirmación.</li>
<li><strong>Conservación eventual:</strong> solo lo que una obligación legal o un litigio en curso exija conservar, y
únicamente durante el tiempo necesario.</li>
</ul>

<p>Más información: <a href="privacy.html">política de privacidad</a>.</p>
""",
        "contact": lambda: f"""
<ul>
<li>Editor: {PUBLISHER}.</li>
<li>Dirección: {ADDRESS}.</li>
<li>Correo electrónico: <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
</ul>
<p><a class="button" href="{mail(GAME + ' - Asistencia')}">Contactar con la asistencia</a></p>
<p>Música: Pixabay (licencia de Pixabay). Estas páginas están alojadas en GitHub Pages, proporcionado por GitHub, Inc.,
88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, Estados Unidos.</p>
""",
    },

    # ------------------------------------------------------------------ PORTUGUÊS
    "pt": {
        "name": "Português",
        "date": "2 de novembro de 2026",
        "updated": "Última atualização",
        "nav": {"index": "Início", "privacy": "Privacidade",
                "delete-account": "Exclusão da conta e dos dados", "contact": "Contato e editor"},
        "titles": {"index": "Informações legais e suporte", "privacy": "Política de privacidade",
                   "delete-account": "Exclusão da conta e dos dados", "contact": "Contato e informações do editor"},
        "index": lambda: f"""
<p>{GAME} é um jogo de tiro espacial: você é um piloto em formação da Academia de Órion que defende as colônias humanas
contra o Enxame, ao longo de 50 níveis, missões variadas e chefões gigantes que se transformam.</p>
<p>Editor: {PUBLISHER}, França.</p>
<p>O jogo salva o progresso, os cristais, as naves desbloqueadas e as configurações <strong>no dispositivo</strong>. A
conta de jogador é a do Google Play Games (salvamento na nuvem, conquistas, placares). Pode exibir anúncios do Google AdMob e oferecer compras no app pelo Google Play. Se
estiver conectado ao Google Play Games, o progresso, as conquistas e as pontuações podem ser salvos pelo Google (veja a
política de privacidade).</p>
""",
        "privacy": lambda: f"""
<h2>Controlador e contato</h2>
<p>O controlador dos dados é {PUBLISHER}, {ADDRESS}.</p>
<p>Para qualquer dúvida sobre dados: <a href="{mail(GAME + ' - Dados pessoais')}">{EMAIL}</a>.</p>

<h2>Dados salvos pelo jogo</h2>
<p>O jogo mantém no dispositivo: o progresso (níveis desbloqueados e concluídos, melhores pontuações, tempos do
simulador), os cristais, as naves e itens desbloqueados, a nave escolhida e as configurações (idioma, volume da música,
das vozes e dos efeitos, história já vista). Esses dados não são enviados ao editor.</p>
<p>O jogo não pede nome, e-mail, idade nem localização, e não acessa contatos, microfone, câmera nem arquivos. Não tem
chat nem troca entre jogadores. As vozes e a música fazem parte do jogo: sua voz nunca é gravada.</p>

<h2>Google Play Games (salvamento na nuvem, conquistas, placares)</h2>
<p>Se você entrar no <strong>Google Play Games</strong>, o jogo pode enviar ao Google seu progresso (salvamento na
nuvem), as conquistas desbloqueadas e suas melhores pontuações; o Google as associa ao seu perfil do Play Games (nome de
jogador e avatar) e pode mostrar os placares a outros jogadores de acordo com suas configurações de visibilidade. O
editor não recebe seu e-mail e não armazena esses dados em seus próprios servidores.</p>
<p>Esse tratamento é feito pela Google LLC / Google Ireland Limited conforme a
<a href="https://policies.google.com/privacy">política de privacidade</a> do Google. Entrar é opcional: o jogo funciona
totalmente sem isso.</p>

<h2>Publicidade, compras e estatísticas</h2>
<p><strong>Anúncios.</strong> O jogo pode exibir anúncios do <strong>Google AdMob</strong> (Google LLC / Google Ireland
Limited): vídeos premiados que você escolhe assistir (continuar uma partida, dobrar os cristais ganhos, começar com um
bônus) e, no máximo uma vez a cada algumas partidas, um anúncio em tela cheia entre dois níveis. Para exibir e medir
esses anúncios, o AdMob trata dados do dispositivo: ID de publicidade, endereço IP, informações técnicas e interações
com os anúncios, conforme a <a href="https://policies.google.com/technologies/ads">política de publicidade do
Google</a>.</p>
<p><strong>Consentimento.</strong> No Espaço Econômico Europeu, no Reino Unido e na Suíça, um formulário de consentimento
certificado (Google UMP) é exibido antes de qualquer anúncio. Você pode recusar anúncios personalizados e mudar sua
escolha a qualquer momento no jogo: <strong>Opções → Preferências de anúncios (RGPD)</strong>. Você também pode redefinir
ou excluir o ID de publicidade nas configurações do telefone (Google → Anúncios).</p>
<p><strong>Compras no app.</strong> As compras (pacote sem anúncios, cristais, naves, visuais) são processadas pelo
Google Play. O editor não recebe seus dados bancários nem seu e-mail; o jogo guarda apenas o que você comprou.</p>
<p>O jogo não inclui nenhuma outra ferramenta de estatísticas ou rastreamento.</p>

<h2>Links externos</h2>
<p>Os links do jogo para estas páginas abrem no seu navegador. O GitHub Pages, que hospeda estas páginas, pode registrar
informações técnicas (endereço IP, tipo de navegador) em seus registros de segurança, conforme sua própria política de
privacidade.</p>

<h2>Crianças</h2>
<p>{GAME} não é destinado a crianças menores de 13 anos e não coleta intencionalmente dados pessoais delas. Se você
acredita que uma criança nos enviou dados (por exemplo por e-mail), entre em contato para que possamos excluí-los.</p>

<h2>Suporte por e-mail</h2>
<p>Quando você entra em contato com o editor, seu e-mail, o conteúdo da mensagem e eventuais anexos são tratados para
responder ao seu pedido, resolver um problema ou exercer seus direitos. A base legal é o interesse legítimo do editor em
prestar suporte. Esses dados ficam acessíveis ao editor e ao provedor de e-mail utilizado, e são mantidos pelo tempo
necessário e, no máximo, três anos após o último contato, salvo obrigação legal ou litígio. Não envie senhas nem dados
bancários por e-mail.</p>

<h2>Conservação, exclusão e direitos</h2>
<p>Os dados do jogo ficam no dispositivo até que você os apague (no jogo ou nas configurações do telefone) ou desinstale
o jogo: veja <a href="delete-account.html">a página de exclusão da conta e dos dados</a>. Você pode solicitar acesso,
correção, exclusão, limitação, oposição ou portabilidade quando a lei aplicável permitir, no endereço acima, e apresentar
uma reclamação à autoridade de proteção de dados do seu país.</p>

<h2>Segurança</h2>
<p>O jogo limita seus dados aos descritos acima. As mensagens de suporte só são acessíveis ao editor. Nenhum sistema é
totalmente livre de riscos; não envie dados sensíveis desnecessários.</p>

<h2>Alterações</h2>
<p>Esta política pode mudar, principalmente se uma conta de jogador ou um modo online for adicionado. A data no topo da
página será atualizada e, se a mudança for importante, ela será anunciada no jogo ou na página do Google Play.</p>
""",
        "delete-account": lambda: f"""
<p>Esta página explica como excluir os dados de <strong>{GAME}</strong>, publicado por <strong>{PUBLISHER}</strong>.</p>

<h2>Conta de jogador (Google Play Games)</h2>
<p>Em {GAME}, sua conta de jogador é sua conta do <strong>Google Play Games</strong>: ela salva seu progresso na nuvem
(história, cristais, naves), recupera-o em outro telefone e mostra suas conquistas e placares. O editor não cria usuário
nem senha e não tem servidor de contas: esses dados são gerenciados pelo Google.</p>
<p><strong>Excluir a conta e seus dados:</strong></p>
<ul>
<li><strong>No jogo:</strong> tela inicial → <strong>Opções</strong> → <strong>Apagar meus dados</strong> → confirme.
Isso apaga o salvamento do telefone <strong>e</strong> o salvamento na nuvem do jogo ligado à sua conta do Play Games, e
encerra a sessão.</li>
<li><strong>No Google:</strong> app <strong>Google Play Games</strong> → <strong>Configurações</strong> → <strong>Excluir
conta e dados do Play Games</strong> (ou só os dados de {GAME}), ou nas
<a href="https://myaccount.google.com/data-and-privacy">configurações da sua Conta do Google</a>.</li>
<li><strong>Por e-mail:</strong> se você não consegue mais abrir o jogo, use o botão abaixo; vamos orientar você e excluir
qualquer dado que tivermos.</li>
</ul>

<h2>Excluir os dados do jogo</h2>
<p>O progresso, os cristais, as naves desbloqueadas e as configurações ficam salvos no dispositivo. Para apagá-los:</p>
<ul>
<li><strong>No jogo:</strong> tela inicial → <strong>Opções</strong> → <strong>Apagar meus dados</strong> e confirme.</li>
<li><strong>No Android:</strong> <strong>Configurações</strong> do telefone → <strong>Apps</strong> →
<strong>{GAME}</strong> → <strong>Armazenamento</strong> → <strong>Limpar dados</strong>.</li>
</ul>
<p>Desinstalar o jogo também exclui esses dados. Os nomes podem variar conforme o telefone; considere também os backups
automáticos do sistema (backup do Google). As compras feitas no Google Play continuam vinculadas à sua Conta do Google e
podem ser restauradas.</p>

<h2>Solicitar a exclusão dos dados mantidos pelo editor</h2>
<p>Se você escreveu para o suporte, pode solicitar a exclusão das suas mensagens e do seu e-mail:</p>
<p><a class="button" href="{delete_mail('Exclusão de dados', 'Olá,', 'Solicito a exclusão dos meus dados relacionados a ' + GAME + '.', 'E-mail usado para contatar o suporte:')}">Solicitar a exclusão dos meus dados</a></p>
<ul>
<li><strong>Dados excluídos:</strong> suas mensagens, anexos e e-mail.</li>
<li><strong>Prazo:</strong> no máximo 30 dias após o recebimento do pedido. Você receberá uma confirmação.</li>
<li><strong>Conservação eventual:</strong> apenas o que uma obrigação legal ou um litígio em andamento exigir, e somente
pelo tempo necessário.</li>
</ul>

<p>Mais informações: <a href="privacy.html">política de privacidade</a>.</p>
""",
        "contact": lambda: f"""
<ul>
<li>Editor: {PUBLISHER}.</li>
<li>Endereço: {ADDRESS}.</li>
<li>E-mail: <a href="mailto:{EMAIL}">{EMAIL}</a>.</li>
</ul>
<p><a class="button" href="{mail(GAME + ' - Suporte')}">Contatar o suporte</a></p>
<p>Música: Pixabay (licença Pixabay). Estas páginas são hospedadas pelo GitHub Pages, fornecido pela GitHub, Inc.,
88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, Estados Unidos.</p>
""",
    },
}

DEFAULT_LANG = "en"


def lang_switcher(current, page):
    items = []
    for code, L in LANGS.items():
        cls = ' class="current" aria-current="true"' if code == current else ""
        items.append(f'<a href="../{code}/{page}.html" hreflang="{code}" lang="{code}"{cls}>{code.upper()}</a>')
    return '<nav class="langs" aria-label="Language">' + "".join(items) + "</nav>"


def page_html(code, page):
    L = LANGS[code]
    title = L["titles"][page]
    nav = " · ".join(
        f'<a href="{p}.html"{" aria-current=\"page\"" if p == page else ""}>{html.escape(L["nav"][p])}</a>' for p in PAGES)
    alternates = "\n".join(
        f'<link rel="alternate" hreflang="{c}" href="{BASE_URL}{c}/{page}.html">' for c in LANGS)
    links = ""
    if page == "index":
        links = "<ul class=\"cards\">" + "".join(
            f'<li><a href="{p}.html">{html.escape(L["nav"][p])}</a></li>' for p in PAGES if p != "index") + "</ul>"
    return f"""<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — {GAME}</title>
<meta name="description" content="{html.escape(GAME + ' — ' + title)}">
<link rel="icon" type="image/png" href="../assets/icon.png">
<link rel="apple-touch-icon" href="../assets/icon.png">
<link rel="stylesheet" href="../assets/style.css">
{alternates}
</head>
<body>
<header class="hero">
  {lang_switcher(code, page)}
  <a class="brand" href="index.html"><img src="../assets/icon.png" alt="" width="64" height="64"><span>{GAME}</span></a>
  <h1>{html.escape(title)}</h1>
  <p class="date">{L["updated"]}{" :" if code == "fr" else ":"} {L["date"]}</p>
</header>
<main>
{L[page]()}
{links}
</main>
<footer><nav>{nav}</nav></footer>
</body>
</html>
"""


def redirect_html(page):
    """Page racine : envoie vers la langue du navigateur, avec des liens si le script est bloqué."""
    codes = list(LANGS)
    links = "".join(
        f'<li><a href="{c}/{page}.html" hreflang="{c}" lang="{c}">{LANGS[c]["name"]} — '
        f'{html.escape(LANGS[c]["titles"][page] if page != "index" else LANGS[c]["titles"]["index"])}</a></li>'
        for c in codes)
    return f"""<!doctype html>
<html lang="{DEFAULT_LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{GAME}</title>
<link rel="icon" type="image/png" href="assets/icon.png">
<link rel="stylesheet" href="assets/style.css">
<script>
(function () {{
  var supported = {codes!r};
  var prefs = navigator.languages || [navigator.language || "{DEFAULT_LANG}"];
  var lang = "{DEFAULT_LANG}";
  for (var i = 0; i < prefs.length; i++) {{
    var c = String(prefs[i]).slice(0, 2).toLowerCase();
    if (supported.indexOf(c) >= 0) {{ lang = c; break; }}
  }}
  location.replace(lang + "/{page}.html");
}})();
</script>
</head>
<body>
<header class="hero">
  <a class="brand" href="index.html"><img src="assets/icon.png" alt="" width="64" height="64"><span>{GAME}</span></a>
  <h1>Choose your language</h1>
</header>
<main><ul class="cards">{links}</ul></main>
</body>
</html>
"""


CSS = """
:root { --bg: #060a18; --panel: #0e1630; --text: #e6eeff; --muted: #9fb0d6; --accent: #ff7a45; --link: #6fd3ff; }
* { box-sizing: border-box; }
body { margin: 0; background: var(--bg); color: var(--text);
       font: 17px/1.6 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }
.hero { background: linear-gradient(135deg, #07163a, #2a0d4d); padding: 20px 16px 28px; text-align: center; }
.brand { display: inline-flex; align-items: center; gap: 12px; color: #fff; text-decoration: none;
         font-weight: 800; font-size: 1.5rem; margin-top: 8px; }
.brand img { border-radius: 14px; box-shadow: 0 6px 18px rgba(0,0,0,.4); }
h1 { margin: 16px 0 4px; font-size: 1.6rem; line-height: 1.25; }
.date { margin: 0; color: var(--muted); font-size: .95rem; }
.langs { display: flex; justify-content: flex-end; gap: 6px; flex-wrap: wrap; }
.langs a { color: var(--muted); text-decoration: none; padding: 2px 8px; border-radius: 8px;
           border: 1px solid rgba(255,255,255,.15); font-size: .85rem; font-weight: 700; }
.langs a.current { color: #07163a; background: var(--accent); border-color: var(--accent); }
main { max-width: 760px; margin: 0 auto; padding: 8px 16px 32px; }
h2 { margin-top: 2rem; font-size: 1.2rem; color: var(--accent); }
a { color: var(--link); }
.button { display: inline-block; background: var(--accent); color: #07163a; font-weight: 700;
          padding: 10px 18px; border-radius: 12px; text-decoration: none; }
.cards { list-style: none; padding: 0; display: grid; gap: 10px; margin-top: 1.5rem; }
.cards a { display: block; background: var(--panel); padding: 14px 18px; border-radius: 12px;
           text-decoration: none; color: var(--text); font-weight: 600; border: 1px solid rgba(255,255,255,.08); }
.cards a:hover { border-color: var(--accent); }
footer { border-top: 1px solid rgba(255,255,255,.08); padding: 16px; text-align: center; font-size: .9rem; }
footer a { color: var(--muted); }
footer a[aria-current] { color: var(--text); font-weight: 700; }
"""


def main():
    os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
    with open(os.path.join(HERE, "assets", "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS.lstrip())
    icon_src = os.path.join(HERE, "..", "PlayStore", "icone_512.png")
    if os.path.exists(icon_src):
        shutil.copyfile(icon_src, os.path.join(HERE, "assets", "icon.png"))

    for code in LANGS:
        os.makedirs(os.path.join(HERE, code), exist_ok=True)
        for page in PAGES:
            with open(os.path.join(HERE, code, page + ".html"), "w", encoding="utf-8") as f:
                f.write(page_html(code, page))

    for page in PAGES:
        with open(os.path.join(HERE, page + ".html"), "w", encoding="utf-8") as f:
            f.write(redirect_html(page))

    open(os.path.join(HERE, ".nojekyll"), "w").close()
    print("Site généré :", ", ".join(LANGS))


if __name__ == "__main__":
    main()
