from gra.game import Location, Monster

locations = [
    Location(1, "Obóz Wojowników", "Idź do obozu wojowników", None,
             "Jesteś w Obozie wojowników. Wokół siebie widzisz ludzi uzbrojonych po zęby rozmawiających na różne "
             "tematy. Możesz tutaj spokojnie odpocząć przed następną wyprawą w nieznane.",
             [2, 3]),
    Location(2, "Las tysiącletni", "Idź do tysiącletniego lasu", None,
             "Jesteś w tysiącletnim lesie. Wokół Ciebie są tylko gigantyczne drzewa, większe od niektórych wieży."
             "Słyszysz dalekie odgłosy życia w lesie, znasz to miejsce, jednak łatwo się tutaj zgubić. Trzymaj się "
             "drogi jeśli Ci życie miłe. Schodzenie z drogi może Cię zaprowadzić w miejsca nigdy niewidziane przez "
             "ludzi.",
             [2, 3, 6, 7, 8, 10]),
    Location(3, "Miasto Kupne", "Idź do miasta kupnego", None,
             "Jesteś w mieście. Otaczają Cię ulice tętniące życiem, wydaje się niemal idealne. Kupce targują się, "
             "rodziny spacerują i życie się toczy. Jednak szybko widzisz że jest to tak piękne jak Ci się wydawało. "
             "Widzisz jak odbywa się sprzedaż niewolników, jakiś głośny Sir Tomash właśnie kogoś kupił. Próbujesz to "
             "ignorować i iść dalej. Plotki kręcą się po całym mieście. Wpada Ci w ucho plotka o tak zwanym "
             "bazyliszku. Nigdy o czymś takim nie słyszałeś.",
             [1, 2, 4, 5]),
    Location(4, "Dom Rzeźbiarza", "Wejdź do domu Rzeźbiarza", None,
             "Wychodzisz do pustego domu rzeźbiarza, podobno tutaj znajduje się leże bazyliszka. Widzisz rzeźby ludzi "
             "i stworzeń, są one przerażająco realistyczne.",
             [3]),
    Location(5, "Arena", "Wejdź na Arenę", None,
             "Jesteś na arenie. Tutaj każdy może się zapisać i walczyć o śmierć i życie za chwałę i pieniądze. "
             "Widzowie krzyczą z podekscytowania z każdym ciosem, wiedząc że jeden z nich będzie śmiertelny. "
             "Niektórzy krzyczą z bólu, hazardziści którzy właśnie przegrali duże sumy pieniędzy.",
             [3]),
    Location(6, "Karczma 'Na Pasach'", None, None,
             "Wchodzisz do pobliskiej karczmy, niedaleko miasta. Jest tu dość pusto, jedynie trio wieśniaków pijących "
             "w kącie oraz rolnik zapijający smutki przy ladie. W samym tyle znajdują się drzwi które wydają się "
             "jakby nie pasowały tutaj.",
             [3, 2]),
    Location(17, "Lochy pod karczmą", None, None,
             "Wchodzisz do tajemniczych drzwi. Schodzy prowadzą Cię do podziemnego lochu, wydają się o wiele starsze "
             "od samej karczmy. Zimne, szare ściany sprawiają że cały loch czuje sie klaustrofobicznie. Czujesz jak "
             "oczy patrzą na Ciebie z każdej strony: Podłogi, ścian, nawet sufitu.",
             [6]),
    Location(7, "Ruiny starej wieży", None, None,
             "W głebi lasu znajdujesz starą wieże. Słyszałeś o niej w legendach i plotkach od ludzi z obozu. Mówi się "
             "że spaliła ją chimera, ale to było setki lat temu. Wieża nie jest wysoka, górne poziomy są zawalone, "
             "jednak kilka poziomów nadal można zwiedzić. Dolne poziomy są nadal stabilne, nie wiadomo jak głeboko "
             "idą. Uważaj na szkielety dawnych rycerzy.",
             [2, 8, 9]),
    Location(8, "Labirynt", None, None,
             "Idąc głębiej w dolne poziomy wierzy spadasz przez podłogę. Jak widać nie były na tyle stabilne jak "
             "myślałeś. Jesteś w labiryncie, cały podziemny kompleks jest w kompletnej ciemności więc zapalasz "
             "pochodnię. Sciany wokół Ciebie wydają się masywne, niezniszczalne. Na każdym rogu widzisz szczątki "
             "poprzednich nieszczęśników którzy tutaj trafili. Ciarki Cię przechodzą gdy myślisz co może grasować w "
             "labiryntach. Legendy głoszą o minotaurze. Mówi się że minotaur jest niepokonany, gdy Cię zobaczy, "
             "jesteś martwy. Znajdź wyjście i przygotuj się na cokolwiek możesz tutaj napotkać.",
             [7, 19, 18]),
    Location(19, "Ślepa uliczka", None, None,
             "Przechodząc przez labirynt, trafiasz na ślepą uliczkę. Nie podoba Ci się to, słyszysz kroki zbliżające "
             "się coraz szybciej, musisz znaleźć wyjście.",
             [1, 18]),
    Location(18, "Wyjście z labiryntu", None, None,
             "Biegniesz w stronę światła, dochodząc do wyjścia. Ledwo co uszedłeś z życiem. Nigdy nie byłeś tak "
             "szczęśliwy by zobaczyć znowu gigantyczne drzewa tysiącletniego lasu.",
             [2, 7, 8]),
    Location(9, "Studnia bez końca", None, None,
             "Niedalego wieży widzisz dużą studnie. Musiała dostarczać strażnikom wody. Widać że od dawna nie była "
             "używana. Patrząc na nią bliżej, zauważasz wajchę. Ciągnąc za nią, pokazują się schody prowadzące w "
             "głębię studni. Mówi się że prowadzi do środka ziemi, ludzie którzy wędrowali w głebi wracają z "
             "poparzeniami gorszymi niż od smoka. Przygotuj się.",
             [2, 8]),
    Location(10, "Bagna", None, None,
             "Jesteś na bagnach. Gęsta mgła sprawia że trudno cokolwiek zobaczyć, a błoto spowalnia każdy Twój ruch. "
             "Bagna to niebezpieczne miejsce, uważaj na czające się w wodzie gady. Gdzieś w głebi tych terenów "
             "mieszka wiedźma o której wieśniacy mówią. Mapa Ci mówi że niedalego stąd jest też karczma.", []),
    Location(20, "Przed chatą wiedźmy", None, None,
             "Idąc głębiej w bagna widzisz małą drewnianą chatę. Jest dość porośnięta przez rośliny, jednak nie "
             "wygląda na opuszczoną. Podejrzewasz że to musi być chata wiedźmy o której mówili wieśniacy, jednak nie "
             "możesz być pewien. Nie wiele jest wiadomo o wiedźmach, ludzie do nich chodzą z chorobami jednak "
             "większość się ich boi. Mowią że zabija tych co uzna za nic nie wartych darmozjadów. Uważaj co mówisz.",
             [10, 21]),
    Location(21, "Chata wiedźmy", None, None, "hehe baba z nosem dugiiii", [20]),
    Location(13, "Karczma '7.5 Drala'", None, None,
             "Po wyjściu z bagien widzisz górski krajobraz. Smocze góry są niedaleko stąd. Po drodze widzisz karczmę. "
             "Karczma tętni życiem, ludzie się bawią i piją. Jednak czujesz na sobie wzrok nienawiści. Karczmasz Cię "
             "ostrzega że ludzie tutaj nie są zbyt przyjaźni dla obcych.",
             [10, 11, 14]),
    Location(11, "Smocze góry", None, None,
             "Droga w góry jest długa i trudna, ciężki wiatr ze śniegiem ograniczają Twoją wizję. W tych górach żyją "
             "potężne stwory czychające w jaskiniach. Najbezpieczniejszą opcją jest trzymanie się ścieżki. Mówi się "
             "że na samym szczycie znajduje się gniazdo smoków. Nawet jedno jajo można sprzedać za fortunę a smocze "
             "szczątki można przerobić na potężne przedmioty.",
             [12, 13, 22, 23]),
    Location(23, "Smoczy szczyt", None, None,
             "Legedny mówią o smokach, sile na tyle potężnej by zniszczyć zamek. Nie wiesz co Cię tu czeka, uważaj.",
             [11]),
    Location(12, "Ruiny zamku Karad", None, None,
             "U stóp szmoczych gór stoją ruiny zamku Karad. Legenda głosi że Karad był potężnym królestwem, "
             "nikt nie był mu równy. Pewnej nocy jedno stworzenie zniszczyło wszystko co nosiło nazwę Karad. Do dziś "
             "nikt nie smiał postawić nogi w tych ruinach. Nie wiadomo co tutaj może grasować.",
             [11]),
    Location(14, "Wieś przybłędów", None, None,
             "Wchodzisz do małej wsi. Rolnicy wydają się przysmutni i widać że coś jest nie tak. Pytasz się jednego z "
             "nich czy coś jest nie tak. \"Coś jest nie tak? Wszystko jest nie tak! To cholerne coś nie daje nam "
             "spokoju! Bydło ginie każdego dnia, w tym tępie na następny miesiąc to my będziemy porywani! Widać że "
             "masz oręż, przydaj się na coś i wybij to coś.\"",
             [13, 15, 24])
]
monsters = [
    Monster(0.3,
            20,
            80,
            34,
            "Drzewiec",
            "Będąc zmęczonym siadasz na leżącym drzewie  i wbijasz w nie miecz . Czujesz że twoja prowizoryczne "
            "siedzenie zaczyna się podnosić. Odskakujesz od niego jak oparzony by ujrzeć starego drzewca ",
            "Nie udało ci się pokonać rozgniewanego drzewca ten jednak postanowił zostawić twój osąd naturze po czym "
            "znika zostawiając ciebie rannego . Będąc na skraju przytomności widzisz zbliżające się do ciebie wilki i "
            "niedźwiedzie ",
            "Udaje ci się wywalczyć  wolność u strażnika lasu .",
            "Próbujesz przekonać go że jest  ci przykro ,.drzewiec wierzy ci i wypuszcza cię wolno ale pozostawia ci "
            "blizną na plecach."),
    Monster(0.9,
            35,
            60,
            12,
            "Minotaur",
            "Czujesz odgłos kroków z korytarza przed tobą wychodzi humanoidalna postać z głową byka oraz wściekłymi "
            "czerwonymi oczami. trzyma on topór którym zaczyna wymachiwać  w każdą stronę w celu zastraszenia",
            "Walka była długim pokazem siły między wami i żaden nie chciał się poddać lecz po długiej walce nie "
            "miałeś już sił więc potwór zadał ci szybką i bez bolesną śmierć na znak szacunku.",
            "Walka była długim pokazem siły między wami i żaden nie chciał się poddać lecz po długiej walce potwór w "
            "końcu padł.",
            ("Podczas próby ucieczki minotaur cię dogonił i zdjął ci głowę z ramion ",)),

    Monster(1,
            28,
            100,
            40,
            "Hydra",
            "Czujesz drżenie ziemi jak by było wywoływane prze ruch ogromnej istoty . Po woli przed tobą zaczynają "
            "się pojawiać wężowate głowy jedna po drugiej.",
            "Walka skończyła się szybko przez swoją ignorancje i nie wiedzę dorobiłeś  potworowi kilka dodatkowych "
            "głów a sam skończyłeś rozszarpany i pożarty.",
            "Po ciężkiej walce udało ci się wygrać a potwór leż martwy trawiony przez jedyną broń skuteczną przeciw "
            "niemu - ogień. ",
            "Ucieczka nie była zbyt trudna ze względu na masę i szybkość stwora, jedynym problemem był zasięg jego "
            "ataku."),
    # Oj tak +1 dla ciebie byq
    Monster(0.5,
            15,
            75,
            25,
            "Czerwony duch",
            "Widzisz biegnącego mężczyznę gonionego przez średniej wielkości potwora przypominającego prześwitującego "
            "czerwonego byka z ogniem buchającym z nozdrzy",
            "Próbujesz odciągnąć byka jednak w momencie gdy próbujesz go złapiać za rogi przechodzi przez ciebie prąd.",
            "Postanowiłeś pomóc kiedy  byk miał już zabić mężczyznę oblewasz go  za pomocą wiadra wody stojącego obok "
            "zmoczony duch zaczyna uciekać.",
            "Ignorujesz potwora wiedząc iż nie atakuje ludzi z byle jakich powodów , ten człowiek musiał sobie na to "
            "zasłużyć"),

    Monster(0.7,
            35,
            78,
            40,
            "Mantikora",
            "Zaglądasz do jaskini w jej wnętrzu jest słychać lwi ryk kiedy próbujesz wyostrzyć wzrok obok twojej "
            "głowy przelatuje ogon skorpiona ",
            "Walka była długa jesteś zmęczony  potwór dostrzega twoją słabość i wykorzystuje lecąc i przygniatająca "
            "twoje ciała po czym odgryza ci głowę.",
            "Walka była długa jesteś zmęczony ale tego nie pokazujesz , widząc swój koniec mantikora wbija swój ogon "
            "w kark i po umiera",
            "zacząłeś uciekać  , jesteś już przy samym wyjściu nagle czujesz bul w okolicy żołądka patrzysz w dół a "
            "tam wystaje z ciebie kolec skorpiona."),

    Monster(1.5,
            14,
            30,
            5,
            "Szkielet",
            "Idziesz sobie spokojnie kiedy nagle zaczął wiać wiatr który zaczął ujawniać ludzkie kości . Zaczynasz "
            "się im przyglądać ,próbujesz podnosisz jedną z czaszek jak tylko zbliżasz rękę ta próbuję cię ugryźć "
            "cofasz się o krok po czym  czujesz coś na swoim ramieniu ,pomału się odwracasz a tam stoi armia "
            "szkieletów.",
            " Nie mogąc wygrać z ich liczebnością zaczynasz uciekać będąc gonionym przez armię szkieletów .",
            "Walka nie trwała długo ze względu na kruchość szkieletów szybko je rozpraszasz po czym miażdżysz ich "
            "czaszki by już nigdy nie wstali",
            "Widząc liczbę nie umarłych próbujesz się wycofać , widząc lukę w ich ustawieniu biegniesz przed siebie "
            "ale niestety gubisz kilka przedmiotów."),
    # Monster(0.9,
    #         45,
    #         25,
    #         30,
    #         "Bazyliszek",
    #
    #         )
]
