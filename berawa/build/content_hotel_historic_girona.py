# Contenido de la demo Hotel Històric (Girona) (es/en/fr/de). Hechos de hotelhistoric.com leidos el 30/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma; sin valoraciones ni opiniones de clientes; sin precios.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hotel real.','en':' Images are illustrations and do not show the actual hotel.','fr':' Les images sont des illustrations et ne montrent pas l’hôtel réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hotel.'}
H={'es':['Dobles y medievales','Suites'],'en':['Doubles and medieval rooms','Suites'],'fr':['Doubles et médiévales','Suites'],'de':['Doppelzimmer und mittelalterliche Zimmer','Suiten']}
RD={
'es':['Habitación doble, doble con 2 camas individuales, habitación medieval, Loft y Red Room: piedra, madera y confort moderno.','Junior Suite, Suite Familiar, Suite Deluxe y la Suite, el espacio más amplio, con 45 m².'],
'en':['Double room, twin room with 2 single beds, medieval room, Loft and Red Room: stone, wood and modern comfort.','Junior Suite, Family Suite, Deluxe Suite and the Suite, the largest space, at 45 m².'],
'fr':['Chambre double, double avec 2 lits simples, chambre médiévale, Loft et Red Room : pierre, bois et confort moderne.','Junior Suite, Suite Familiale, Suite Deluxe et la Suite, l’espace le plus vaste, avec 45 m².'],
'de':['Doppelzimmer, Doppelzimmer mit 2 Einzelbetten, mittelalterliches Zimmer, Loft und Red Room: Stein, Holz und moderner Komfort.','Junior Suite, Familiensuite, Deluxe-Suite und die Suite, der größte Raum mit 45 m².']}
ART={
'hero':('arches',9951,['#2a1f1a','#d9a35a','#f1d29a','#7a4a32','#5e3826','#331e14']),
'intro':('columns',9952,['#f1ebe4','#faf6f0','#7a4a32','#5e3826','#331e14']),
'r1':('arches',9961,['#efe8e0','#c99350','#7a4a32','#5e3826','#331e14']),
'r2':('columns',9962,['#2a1f1a','#e0aa64','#f4d7a6','#8a5a40','#6e4630','#3a261a']),
'g1':('skyline',9971,['#2a1f1a','#e0aa64','#f4d7a6','#8a5a40','#6e4630','#3a261a']),
'g2':('arches',9972,['#f0ece4','#f9f5ee','#9c6a36','#6a4a2a','#3a2a18']),
'g3':('hills',9973,['#ece7da','#f1e2c3','#d6a160','#a8a07e','#7c7458','#55503c']),
'g4':('columns',9974,['#2a1f1a','#d9a35a','#f1d29a','#7a4a32','#5e3826','#331e14'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel Històric · Hotel en el Barri Vell de Girona',see_rooms='Ver las habitaciones',hero_k='Girona · Carrer de Bellmirall 4A',hero_t='Historia y modernidad en el corazón del Barri Vell',hero_s='A pocos pasos de la Catedral y de la plaza de Sant Domènec.',
 intro_t='Cimientos romanos, confort de hoy',intro_p1='Sus cimientos romanos y sus muros de los siglos VIII y IX conservan la esencia del pasado, y cada rincón se ha renovado para ofrecer el máximo confort.',
 intro_p2='Un alojamiento pensado también para familias, donde los más pequeños son bienvenidos. Cada habitación se inspira en un hecho, leyenda o lugar emblemático de Girona.',
 stats=['Barri Vell','Muros de los siglos VIII y IX','Aire acondicionado','Wifi gratuito'],nav_rooms='Habitaciones',rooms_t='Nuestras habitaciones',rooms_s='Piedra y madera, vigas a la vista y comodidades modernas.',
 svcs=['Aire acondicionado','Wifi gratuito','Habitaciones familiares','Bonos regalo','Muros de piedra originales','Vigas de madera a la vista'],
 around_s='El Call Jueu, la Catedral de Santa María, las murallas y los puentes sobre el Onyar, a pocos pasos.',
 loc_p='Carrer de Bellmirall 4A · 17004 Girona. Sin aparcamiento propio: parking gratuito en la Plaça Josep Ferrater i Mora, a 4 minutos a pie, si hay sitio.',
 chips=['¿Qué habitaciones tenéis?','¿Dónde aparco?','¿Es para familias?','¿Cómo reservo?']),
'en':dict(title='Hotel Històric · Hotel in Girona’s Barri Vell',see_rooms='See the rooms',hero_k='Girona · Carrer de Bellmirall 4A',hero_t='History and modernity in the heart of the Barri Vell',hero_s='A few steps from the Cathedral and the plaça de Sant Domènec.',
 intro_t='Roman foundations, today’s comfort',intro_p1='Its Roman foundations and 8th- and 9th-century walls keep the essence of the past, and every corner has been renovated for maximum comfort.',
 intro_p2='A place also designed for families, where children are welcome. Each room is inspired by an event, legend or landmark of Girona.',
 stats=['Barri Vell','8th–9th-century walls','Air conditioning','Free wifi'],nav_rooms='Rooms',rooms_t='Our rooms',rooms_s='Stone and wood, exposed beams and modern comforts.',
 svcs=['Air conditioning','Free wifi','Family rooms','Gift vouchers','Original stone walls','Exposed wooden beams'],
 around_s='The Call Jueu, the Cathedral of Santa María, the city walls and the bridges over the Onyar, a few steps away.',
 loc_p='Carrer de Bellmirall 4A · 17004 Girona. No on-site parking: free parking at Plaça Josep Ferrater i Mora, a 4-minute walk, if spaces are available.',
 chips=['Which rooms do you have?','Where can I park?','Is it family-friendly?','How do I book?']),
'fr':dict(title='Hotel Històric · Hôtel dans le Barri Vell de Gérone',see_rooms='Voir les chambres',hero_k='Gérone · Carrer de Bellmirall 4A',hero_t='Histoire et modernité au cœur du Barri Vell',hero_s='À quelques pas de la cathédrale et de la place de Sant Domènec.',
 intro_t='Fondations romaines, confort d’aujourd’hui',intro_p1='Ses fondations romaines et ses murs des VIIIe et IXe siècles conservent l’essence du passé, et chaque recoin a été rénové pour un confort maximal.',
 intro_p2='Un lieu pensé aussi pour les familles, où les enfants sont les bienvenus. Chaque chambre s’inspire d’un fait, d’une légende ou d’un lieu emblématique de Gérone.',
 stats=['Barri Vell','Murs des VIIIe–IXe siècles','Climatisation','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Nos chambres',rooms_s='Pierre et bois, poutres apparentes et confort moderne.',
 svcs=['Climatisation','Wifi gratuit','Chambres familiales','Bons cadeaux','Murs en pierre d’origine','Poutres en bois apparentes'],
 around_s='Le Call Jueu, la cathédrale Santa María, les remparts et les ponts sur l’Onyar, à quelques pas.',
 loc_p='Carrer de Bellmirall 4A · 17004 Gérone. Pas de parking sur place : parking gratuit Plaça Josep Ferrater i Mora, à 4 minutes à pied, selon disponibilité.',
 chips=['Quelles chambres avez-vous ?','Où me garer ?','Est-ce adapté aux familles ?','Comment réserver ?']),
'de':dict(title='Hotel Històric · Hotel im Barri Vell von Girona',see_rooms='Zimmer ansehen',hero_k='Girona · Carrer de Bellmirall 4A',hero_t='Geschichte und Moderne im Herzen des Barri Vell',hero_s='Wenige Schritte von der Kathedrale und der Plaça de Sant Domènec.',
 intro_t='Römische Fundamente, heutiger Komfort',intro_p1='Die römischen Fundamente und die Mauern aus dem 8. und 9. Jahrhundert bewahren das Wesen der Vergangenheit, und jeder Winkel wurde für höchsten Komfort renoviert.',
 intro_p2='Ein Haus auch für Familien, in dem Kinder willkommen sind. Jedes Zimmer ist von einem Ereignis, einer Legende oder einem Wahrzeichen Gironas inspiriert.',
 stats=['Barri Vell','Mauern aus dem 8.–9. Jh.','Klimaanlage','Kostenloses WLAN'],nav_rooms='Zimmer',rooms_t='Unsere Zimmer',rooms_s='Stein und Holz, sichtbare Balken und moderner Komfort.',
 svcs=['Klimaanlage','Kostenloses WLAN','Familienzimmer','Geschenkgutscheine','Originale Steinmauern','Sichtbare Holzbalken'],
 around_s='Das Call Jueu, die Kathedrale Santa María, die Stadtmauern und die Brücken über den Onyar, nur wenige Schritte entfernt.',
 loc_p='Carrer de Bellmirall 4A · 17004 Girona. Kein eigener Parkplatz: kostenloser Parkplatz an der Plaça Josep Ferrater i Mora, 4 Gehminuten, sofern frei.',
 chips=['Welche Zimmer gibt es?','Wo kann ich parken?','Ist es familienfreundlich?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
RB='https://booking.avirato.com/?code=95424272'
BOOK=dict(mode='engine',url={l:RB+'&lang='+l for l in ('es','en','fr','de')})
D=dict(name='Hotel Històric',ac='#2a1f1a',ac2='#7a4a32',ac2_a11y='#5e3826',book=BOOK,around=['Catedral de Girona','Call Jueu de Girona'],foot=FOOT,
 address='Carrer de Bellmirall 4A · 17004 Girona',phones=['+34 972 22 35 83'],emails=['info@hotelhistoric.com'],maps='Hotel Històric, Carrer de Bellmirall 4A, 17004 Girona',t=T)
META=dict(repo='demo-hotel-historic-girona',name='Hotel Històric',legal_name='Allotjaments Call de Girona SL (aviso legal de su web)',registry_ids=['B55295729'],
 url='https://hotelhistoric.com/',domain='hotelhistoric.com',municipality='Girona',province='Girona',sector='hotel con encanto en el Barri Vell de Girona',
 read_at='2026-10-30T11:00:00+01:00',created_at='2026-10-30T10:59:00+01:00',built_at='2026-10-30T11:20:00+01:00',audit_date='2026-10-30T10:53:21+01:00',
 rating=dict(value=4.4,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Hotel+Historic/@41.9862637,2.8264929,17z/data=!4m9!3m8!1s0x12bae6e77f995555:0x70d9f02b67ae1022!5m2!4m1!1i2!8m2!3d41.9862637!4d2.8264929!16s%2Fg%2F1vsmv303'),
 book=dict(mode='engine',url=RB,note='motor de reservas real de su web (Avirato, code 95424272, un solo establecimiento en su selector), HTTP 200 comprobado el 30/10/2026 con lang es/en/fr/de.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Hay aire acondicionado?','K02'),('¿Hay wifi?','K03'),('¿Dónde aparco?','K04'),('¿Es para familias?','K05'),('¿Dónde está el hotel?','K06'),('¿A qué distancia está la estación de tren?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Qué historia tiene el edificio?','K09'),('¿Qué visitar en Girona?','K10'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('Is there air conditioning?','K02'),('Is there wifi?','K03'),('Where can I park?','K04'),('Is it family-friendly?','K05'),('Where is the hotel?','K06'),('How far is the train station?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('What is the history of the building?','K09'),('What to visit in Girona?','K10'),('How much is a night?',None),('Do you have a swimming pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Y a-t-il la climatisation ?','K02'),('Y a-t-il le wifi ?','K03'),('Où me garer ?','K04'),('Est-ce adapté aux familles ?','K05'),('Où se trouve l’hôtel ?','K06'),('À quelle distance est la gare ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Quelle est l’histoire du bâtiment ?','K09'),('Que visiter à Gérone ?','K10'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Gibt es eine Klimaanlage?','K02'),('Gibt es WLAN?','K03'),('Wo kann ich parken?','K04'),('Ist es familienfreundlich?','K05'),('Wo liegt das Hotel?','K06'),('Wie weit ist der Bahnhof?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Welche Geschichte hat das Gebäude?','K09'),('Was kann man in Girona besichtigen?','K10'),('Was kostet eine Nacht?',None),('Haben Sie ein Schwimmbad?',None)]}
