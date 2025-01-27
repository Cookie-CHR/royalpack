import datetime
import random

import royalnet.engineer as engi

import royalpack.bolts as rb

# Tutte le fortunes qui devono essere positive :)
# O almeno neutrali...
_fortunes = [
    "😄 Oggi sarà una fantastica giornata!",
    "😌 Oggi sarà una giornata molto chill e rilassante.",
    "💰 Oggi sui tuoi alberi cresceranno più Stelline!",
    "🍎 Oggi un unicorno ti lascerà la sua Blessed Apple!",
    "📈 Oggi il tuo team in ranked sarà più amichevole e competente del solito!",
    "🏝 Oggi potrai raggiungere l'Isola Miraggio!",
    "🐱 Oggi vedrai più gatti del solito su Internet!",
    "🐶 Oggi vedrai più cani del solito su Internet!",
    "🐦 Oggi vedrai più uccelli del solito su Internet!",
    "🐌 Oggi incontrerai una chiocciola sperduta!",
    "🎁 Oggi i dispenser di regali in centro funzioneranno senza problemi!",
    "🥕 Oggi il tuo raccolto avrà qualità Iridium Star!",
    "🔴 Oggi troverai più oggetti di rarità rossa del solito!",
    "✨ Oggi farai molti più multicast!",
    "♦️ Oggi troverai una Leggendaria Dorata!",
    "⭐️ Oggi la stella della RYG ti sembrerà un pochino più dritta!",
    "⭐️ Oggi la stella della RYG ti sembrerà anche più storta del solito!",
    "💎 Oggi i tuoi avversari non riusciranno a deflettere i tuoi Emerald Splash!",
    "⬅️ Oggi le tue supercazzole prematureranno un po' più a sinistra!",
    "➡️ Oggi le tue supercazzole prematureranno un po' più a destra!",
    "🌅 Oggi sarà il giorno dopo ieri e il giorno prima di domani!",
    "🤖 Oggi il Royal Bot ti dirà qualcosa di molto utile!",
    "🏠 Oggi qualcuno si autoinviterà a casa tua!",
    "📵 Oggi passerai una bella giornata tranquilla senza che nessuno ti chiami!",
    "🕸 Oggi cadrai trappola di una ragnatela! \uE011O ti arriverà in faccia.\uE001",
    "🔮 Oggi chiederai a @royalgamesbot di dirti la tua /fortune!",
    "👽 Oggi incontrerai gli UFI!!!1!!uno!",
    "🦾 Oggi uno scienziato pazzo ti proporrà di sostituire il tuo braccio con un braccio-razzo meccanico!",
    "🕵️ Oggi una spia in incognito ti chiederà se hai mai visto the Emoji Movie!",
    "🍕 Oggi mangerai una margherita doppio pomodoro!",
    "🍰 Oggi mangerai una torta al gusto di torta!",
    "🥇 Oggi vincerai qualcosa!",
    "🏴‍☠️ Oggi salperai i sette mari con la tua ciurma pirata!",
    "🕒 Oggi sarà ieri, e domani sarà oggi!",
    "🔙 Oggi tornerai indietro nel tempo!",
    "🚨 Oggi suonerà l'allarme della Velvet Room!",
    "🏳️‍🌈 Oggi scoprirai l'esistenza di almeno un gender che non conoscevi!",
    "🥴 Oggi ti dimenticherai come ci si siede!",
    "👀 Oggi scoprirai di avere degli occhi!",
    "🏹 Oggi ti verrà voglia di installare Arch Linux, ma cambierai idea molto in fretta!",
    "🩲 Oggi annuncerai alla cv di essere in mutande!",
    "👟 Oggi tua madre ti regalerà delle scarpe da corsa!",
    "✨ Oggi troverai un Pokémon shiny!",
    "👏 Oggi sarai felice, lo saprai e batterai le mani!",
    "🦴 Oggi scoprirai di avere uno scheletro wholesome all'interno di te!",
    "💳 Oggi riuscirai a fornire i tre numerini della tua carta di credito a John Wick!",
    "🤔 Oggi smetterai finalmente di essere sus, in quanto sarai confermato dal villaggio!",
    "🔮 Oggi pondererai intensamente la tua sfera!",
    "🗳️ Oggi ci saranno le elezioni per un nuovo partito sul tuo pianeta!",
    "🥓 Oggi avrai bacon illimitato e niente videogiochi!",
    "🎮 Oggi avrai videogiochi, videogiochi illimitati e niente videogiochi!",
    "🔫 Oggi troverai una pistola pearlescent!",
    "🤖 Oggi ti chiederanno di pilotare un robot gigante!",
    "💣 Oggi dovrai continuare a parlare, o esploderai!",
    "🤌 Oggi ti sentirai particolarmente italiano, e gesticolerai più del solito!",
    "🪵 Oggi ti servirà legname!",
    "☄️ Oggi avvisterai una cometa, rischiando di inciampare!",
    "🥅 Oggi farai goal!",
    "🧿 Oggi sarai protetto dagli spiriti maligni che attraversano le pareti!",
    "💰 Oggi è una buona giornata per il capitalismo!",
    "⚒️ Oggi è una buona giornata per il comunismo!",
    "🐰 Oggi inizia la stagione di caccia dei Big Chungus!",
    "🐸 Oggi incontrerai una rana-cavaliere!",
    "⚔️ Oggi un cyborg-samurai ti cederà la sua katana RGB!",
    "🥪 Oggi mangerai un sandvich!",
    "👻 Oggi farai amicizia con Re Boo!",
    "🫀 Oggi un necromante ti ruberà il cuore, e lo farà battere a ritmo!",
    "🦊 Oggi volerai su un Arwing in compagnia di un rinomato mercenario!",
    "🦋 Oggi una tua particolare azione avrà conseguenze, ma potrai tornare indietro nel tempo e correggerla!",
    "🐳 Oggi una balena trasporterà un container per te!",
    "🔥 Oggi sarà una giornata di fuoco!",
    "🥕 Oggi sostituirai il naso a un pupazzo di neve!",
    "🍔 Oggi mangerai il tuo cibo preferito: il sushi!",
    "🍭 Oggi un lecca-lecca ti sbloccherà poteri inimmaginabili!",
    "🧩 Oggi andrai a caccia di Jiggy!",
    "🚜 Oggi piraterai un trattore!",
    "🧭 Oggi ti perderai nei Lost Woods!",
    "⚙️ Oggi aumenterai la produzione di Iron Gear!",
    "🔫 Oggi attiverai il tuo Devil Trigger!",
    "🍺 Oggi servirai un drink con più Karmotrine!",
    "🚽 Oggi sperimenterai la leggendaria Terra Toilet!",
    "🚰 Oggi sarai più idratato del solito!",
    "🔑 Oggi troverai la chiave di tutte le porte!",
    "📎 Oggi incontrerai Clippy!",
    "🌪 Oggi un tornado girerà in senso orario!",
    "🍄 Oggi diventerai Super grazie ad un fungo!",
    "👑 Oggi preparerai la colazione per Re Artù!",
    "🍌 Oggi metterai una banana in microonde!",
    "❤️‍🔥 Oggi scapperai dal Tartaro!",
    "♻️ Oggi, riciclando della Silt, troverai un dinosauro!",
    "🏧 Oggi piazzerai un jammer su un bancomat, estraendone i contenuti!",
    "🚼 Oggi ti chiederai il significato di questa emoji!",
    "🤡 Oggi dovrai interrogare il clown di un circo!",
    "👣 Oggi riceverai un marchio che ti proteggerà dai vampiri!",
    "🎊 Oggi dalle Sfere Festa non uscirà nessuna Bob-omba!",
    "🧲 Oggi piazzerai un magnete per attirare colpi di bazooka!",
    "㊗️ Oggi qualcuno ti farà le sue congratulazioni!",
    "⚛️ Oggi sfrutterai appieno l'energia dell'atomo!",
    "🈁 Oggi ti troverai qui!",
    "💮 Oggi i tuoi esami andranno alla perfezione!",
    "☕️ Oggi berrai un espresso d-d-doppio!?",
    "🐝 Oggi farai quello che fanno le api sulle foglie!",
    "🎰 Oggi vincerai il Jackpot di Francoforte 1!",
    "🧱 Oggi rifiuterai un en passant!",
    "🪓 Oggi perderai la tua ascia, ma la riuscirai facilmente a ritrovare, in quanto starà urlando il tuo nome!",
    "🕳 Oggi cadrai in una Trappola!",
    "⛏ Oggi scaverai degli smeraldi!",
    "🩹 Oggi rigenererai tutta la tua vita con un singolo cerotto!",
    "📈 Oggi i tuoi affari andranno alla grande!",
    "📉 Oggi avrai la possibilità di comprare qualche cosa a prezzo scontato!",
    "🅱️ Oggi la seconda lettera dell'alfabeto ti porterà più fortuna del solito!",
    "🧚 Oggi ti chiederai coraggiosamente dove vola la fatina!",
]


@rb.capture_errors
@engi.TeleportingConversation
async def fortune(*, _msg: engi.Message, **__):
    """
    Come sarà la giornata di oggi?
    """

    author = await _msg.sender

    r = random.Random(x=hash(author) + hash(datetime.date.today()))
    message = r.sample(_fortunes, 1)[0]

    await _msg.reply(text=message)


__all__ = ("fortune",)
