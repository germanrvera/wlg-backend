from django.core.management.base import BaseCommand
from catalogo.models import Proyecto


PROYECTOS = {

    "La Rural": {
        "lead": (
            "La Rural es uno de los predios feriales y de eventos más representativos de Argentina. "
            "La intervención de World Leds Go se concentró en la recalificación lumínica de sus "
            "espacios de circulación principal y salas de reuniones VIP, donde la iluminación debía "
            "acompañar la escala arquitectónica sin competir con la identidad edilicia existente.\n\n"
            "El desafío central fue sostener una temperatura cromática cálida y envolvente en "
            "recintos de techos altos, manteniendo niveles de iluminancia técnicamente precisos "
            "para el uso corporativo y ferial. Se eligió un sistema de riel de bajo voltaje con "
            "luminarias orientables de 3000K y CRI superior a 90, que permite reconfigurar la "
            "distribución lumínica según el tipo de evento sin intervenir en la infraestructura fija.\n\n"
            "La propuesta prioriza la continuidad visual: sin cortes abruptos entre zonas, sin "
            "contrastes que fatiguen la circulación. La luz estructura el recorrido sin hacerse visible."
        ),
        "quote": "En espacios de esta envergadura, la luz no puede ser un elemento decorativo. Tiene que estructurar la percepción del espacio.",
        "quote_autor": "Equipo de Diseño WLG",
        "bloques": [
            {
                "num": "01",
                "title": "Escala y continuidad",
                "img": "",
                "text": (
                    "El predio demandaba coherencia lumínica entre sectores de uso muy distinto: "
                    "pasillos de alto tráfico, salas de reuniones y espacios de exposición. "
                    "La solución de riel permitió unificar el lenguaje sin uniformar la intensidad, "
                    "modulando cada zona según su función sin romper la continuidad del conjunto."
                )
            },
            {
                "num": "02",
                "title": "Flexibilidad operativa",
                "img": "",
                "text": (
                    "La instalación fue diseñada para trabajar sin intervención técnica entre "
                    "eventos. Los focos orientables sobre riel permiten al equipo de producción "
                    "reconfigurar la distribución de luz en minutos, adaptando el espacio a "
                    "ferias, congresos o ceremonias corporativas con la misma infraestructura."
                )
            },
            {
                "num": "03",
                "title": "Confort y eficiencia",
                "img": "",
                "text": (
                    "La temperatura de color de 3000K y el índice de reproducción cromática "
                    "superior a 90 garantizan un entorno visualmente confortable para jornadas "
                    "extensas de trabajo. La eficiencia del sistema LED reduce en más de un 60% "
                    "el consumo respecto a la instalación de halógenos preexistente."
                )
            },
        ],
        "ficha_tecnica": {
            "Tipo de espacio": "Institucional / Ferial",
            "Ubicación": "Buenos Aires",
            "Año": "2024",
            "Sistema principal": "Riel de bajo voltaje",
            "Temperatura de color": "3000K",
            "CRI": "≥ 90",
            "Eficiencia": "≥ 100 lm/W",
            "Dimming": "TRIAC / 1-10V",
        }
    },

    "Movistar Arena VIP": {
        "lead": (
            "El área VIP del Movistar Arena es un recinto de acceso diferenciado dentro de uno "
            "de los venues de entretenimiento de mayor capacidad del país. La propuesta lumínica "
            "de World Leds Go debía resolver una tensión inherente al espacio: la robustez técnica "
            "que exige un venue de entretenimiento masivo y la exclusividad que espera quien accede "
            "a una zona premium.\n\n"
            "Se instaló un sistema de riel de bajo voltaje que permite orientar cada luminaria de "
            "forma independiente, adaptando la distribución lumínica al tipo de evento sin necesidad "
            "de intervención en la infraestructura. La temperatura de color cálida —2700K— construye "
            "una atmósfera que contrasta deliberadamente con la intensidad del espectáculo, "
            "generando una zona de descanso visual dentro del mismo recinto.\n\n"
            "El resultado es un espacio que funciona como pausa: contenido, envolvente, "
            "reconocible como distinto."
        ),
        "quote": "La exclusividad no se construye con más luz. Se construye con la luz en el lugar exacto.",
        "quote_autor": "Equipo de Diseño WLG",
        "bloques": [
            {
                "num": "01",
                "title": "Un espacio dentro del espacio",
                "img": "",
                "text": (
                    "El área VIP opera como un contrapunto lumínico respecto al venue principal. "
                    "Mientras el show demanda intensidad y dinamismo, la zona premium requiere "
                    "contención y calidez. La elección de 2700K y niveles de iluminancia moderados "
                    "construye esa distinción sin necesidad de recursos arquitectónicos adicionales."
                )
            },
            {
                "num": "02",
                "title": "Flexibilidad para cada evento",
                "img": "",
                "text": (
                    "El sistema de riel permite reconfigurar la orientación de cada luminaria en "
                    "función del tipo de evento: conciertos, shows en vivo, eventos corporativos "
                    "o funciones especiales. La infraestructura se adapta sin modificaciones, "
                    "reduciendo los tiempos de puesta a punto entre producción y producción."
                )
            },
            {
                "num": "03",
                "title": "Confort en condiciones extremas",
                "img": "",
                "text": (
                    "Los recintos de entretenimiento de alta capacidad generan condiciones de "
                    "temperatura y humedad que exigen luminarias con tolerancias ampliadas. "
                    "Las unidades instaladas operan en un rango de hasta 45°C de temperatura "
                    "ambiente, manteniendo estabilidad de flujo y temperatura de color sin "
                    "degradación perceptible durante toda la función."
                )
            },
        ],
        "ficha_tecnica": {
            "Tipo de espacio": "Entretenimiento / VIP",
            "Ubicación": "Buenos Aires",
            "Año": "2024",
            "Sistema principal": "Riel bajo voltaje Track LV",
            "Temperatura de color": "2700K",
            "CRI": "≥ 92",
            "Eficiencia": "≥ 95 lm/W",
            "Dimming": "DALI / 1-10V",
        }
    },

    "Torre Bella": {
        "lead": (
            "Torre Bella es un desarrollo residencial de alta gama en Palermo. La iluminación "
            "fue incorporada al proceso de diseño desde la etapa de anteproyecto, lo que permitió "
            "integrar los sistemas de riel en el cielorraso sin condicionantes estructurales y "
            "definir la posición de los puntos de luz en función de la distribución de mobiliario "
            "y los ejes compositivos de cada planta.\n\n"
            "Los sistemas de riel empotrado en unidades tipo y amenities permiten al residente "
            "adaptar la distribución lumínica a sus necesidades cotidianas sin modificar la "
            "infraestructura. La temperatura de color de 2700K en espacios de permanencia y "
            "3000K en cocinas y baños define una jerarquía cromática que acompaña los ritmos "
            "diarios sin imponer una única atmósfera.\n\n"
            "El proyecto incluyó la especificación de dimming compatibe con los sistemas de "
            "automatización del edificio, permitiendo escenas programables por unidad."
        ),
        "quote": "Cuando la luminaria desaparece en el cielorraso, la arquitectura puede hablar por sí sola.",
        "quote_autor": "Equipo de Diseño WLG",
        "bloques": [
            {
                "num": "01",
                "title": "Integración desde el origen",
                "img": "",
                "text": (
                    "La participación de WLG desde la etapa de anteproyecto permitió resolver "
                    "la instalación del riel empotrado sin cortes ni remiendos en el cielorraso. "
                    "Las bandejas de distribución fueron coordinadas con los demás sistemas del "
                    "edificio —climatización, domótica, incendio— para lograr un techo limpio "
                    "en todas las unidades."
                )
            },
            {
                "num": "02",
                "title": "Jerarquía cromática por ambiente",
                "img": "",
                "text": (
                    "Las áreas de living y dormitorios trabajan con 2700K para generar ambientes "
                    "cálidos y envolventes. Las cocinas y baños utilizan 3000K, favoreciendo la "
                    "percepción de limpieza y contraste. El resultado es una temperatura de color "
                    "que acompaña el recorrido del residente sin generar saltos visuales abruptos."
                )
            },
            {
                "num": "03",
                "title": "Amenities y espacios comunes",
                "img": "",
                "text": (
                    "En el gym, sala de usos múltiples y lobby de acceso se utilizaron luminarias "
                    "de mayor potencia con ángulos de apertura amplios para garantizar uniformidad "
                    "en espacios de uso colectivo. La elección de 3000K-4000K en estos sectores "
                    "refuerza la distinción entre lo privado y lo común."
                )
            },
        ],
        "ficha_tecnica": {
            "Tipo de espacio": "Residencial de alta gama",
            "Ubicación": "Palermo, CABA",
            "Año": "2023",
            "Sistema principal": "Riel empotrado bajo voltaje",
            "Temperatura de color": "2700K / 3000K",
            "CRI": "≥ 92",
            "Dimming": "TRIAC — compatible domotica",
            "Automatización": "KNX / Lutron",
        }
    },

    "Parfumerie Recoleta": {
        "lead": (
            "En el retail de nicho, la iluminación no es un complemento: es parte constitutiva "
            "del producto. Para Parfumerie Recoleta, una perfumería de autor ubicada en el "
            "barrio más exigente de Buenos Aires, el desafío fue construir una atmósfera que "
            "potenciara la percepción de las fragancias en exhibición sin generar distorsión "
            "cromática sobre los frascos ni sobre la piel de quienes los prueba.\n\n"
            "Se especificaron luminarias Galuy de 3000K con índice de reproducción cromática "
            "superior a 95, montadas sobre sistema de riel de bajo voltaje para permitir "
            "reenfoque en función de los cambios estacionales en la exhibición. El nivel de "
            "iluminancia general es deliberadamente moderado —entre 200 y 300 lux— con "
            "focos de acento de hasta 800 lux sobre las piezas seleccionadas.\n\n"
            "La luz no homogeniza el espacio. Lo edita."
        ),
        "quote": "En un espacio de 80 m², la diferencia entre un buen producto y uno irresistible puede ser la temperatura de color.",
        "quote_autor": "Equipo de Diseño WLG",
        "bloques": [
            {
                "num": "01",
                "title": "CRI 95+ como especificación no negociable",
                "img": "",
                "text": (
                    "La reproducción cromática fue el criterio de selección central. Las fragancias "
                    "de autor se comercializan en frascos de vidrio, metal y materiales que "
                    "reaccionan de forma muy distinta según el espectro de la fuente lumínica. "
                    "Con CRI ≥ 95, los colores se muestran sin distorsión y el producto ocupa "
                    "el centro de la percepción del comprador."
                )
            },
            {
                "num": "02",
                "title": "Estrategia de acento y fondo",
                "img": "",
                "text": (
                    "El nivel general de iluminancia baja al mínimo funcional para circulación "
                    "segura. Sobre cada pieza en exhibición, un foco de acento preciso multiplica "
                    "por tres o cuatro la intensidad puntual. Este contraste dirigido crea una "
                    "jerarquía visual que el comprador sigue de forma intuitiva, sin señalética "
                    "adicional."
                )
            },
            {
                "num": "03",
                "title": "Adaptabilidad estacional",
                "img": "",
                "text": (
                    "La colección se actualiza con cada temporada. El sistema de riel permite "
                    "reposicionar y reorientar cada luminaria en menos de veinte minutos, "
                    "adaptando la distribución lumínica a los cambios en la disposición de "
                    "los productos sin intervención técnica especializada."
                )
            },
        ],
        "ficha_tecnica": {
            "Tipo de espacio": "Retail de nicho",
            "Ubicación": "Recoleta, CABA",
            "Año": "2023",
            "Sistema principal": "Galuy sobre riel Track LV",
            "Temperatura de color": "3000K",
            "CRI": "≥ 95",
            "Iluminancia general": "200–300 lux",
            "Iluminancia de acento": "hasta 800 lux",
            "Dimming": "TRIAC",
        }
    },

    "La Rando": {
        "lead": (
            "La Rando es un bar de coctelería de autor en el corazón del casco histórico de "
            "San Telmo. La propuesta de iluminación de World Leds Go partió de una premisa "
            "que el cliente definió con claridad desde el inicio: la oscuridad es parte del "
            "producto. No una limitación a compensar, sino una decisión estética que debía "
            "quedar sostenida por la instalación.\n\n"
            "El sistema resultante trabaja por contraste: puntos de luz precisos y de alta "
            "intensidad sobre la barra y las mesas de trabajo, envueltos en una penumbra "
            "cálida que acompaña sin interrumpir. Las luminarias Gilam y Micro Cinor, "
            "montadas sobre riel, permiten orientar cada foco con precisión milimétrica "
            "para que la copa, no la luminaria, sea lo que el cliente ve primero.\n\n"
            "La atmósfera nocturna que La Rando propone funciona porque la luz sabe exactamente "
            "adónde mirar."
        ),
        "quote": "La oscuridad controlada no es ausencia de luz. Es la forma más precisa de usarla.",
        "quote_autor": "Equipo de Diseño WLG",
        "bloques": [
            {
                "num": "01",
                "title": "La penumbra como decisión de diseño",
                "img": "",
                "text": (
                    "En un bar de coctelería, el ambiente nocturno es parte de la oferta. "
                    "La iluminación fue calibrada para operar en niveles muy bajos de "
                    "iluminancia general —menos de 50 lux en zona de mesas— sin generar "
                    "incomodidad visual. Los puntos de acento sobre la barra y los focos "
                    "dirigidos a cada mesa crean una jerarquía que orienta sin saturar."
                )
            },
            {
                "num": "02",
                "title": "Precisión sobre la barra",
                "img": "",
                "text": (
                    "El área de trabajo del bartender requería condiciones lumínicas distintas "
                    "al resto del local: visibilidad técnica precisa sin perder la calidez "
                    "del conjunto. La temperatura de 2700K con alta reproducción cromática "
                    "permite al bartender distinguir colores y texturas de los ingredientes "
                    "mientras el cliente percibe un ambiente coherente y sin quiebres."
                )
            },
            {
                "num": "03",
                "title": "Integración en la arquitectura existente",
                "img": "",
                "text": (
                    "El local ocupa una planta baja en un edificio de principios del siglo XX "
                    "con techos altos y detalles ornamentales. La instalación se resolvió sin "
                    "intervenir los cielorrasos originales: el sistema de riel aparente, pintado "
                    "en negro mate, se integra visualmente con el contexto arquitectónico y "
                    "refuerza la estética industrial del proyecto."
                )
            },
        ],
        "ficha_tecnica": {
            "Tipo de espacio": "Hospitality / Bar de autor",
            "Ubicación": "San Telmo, CABA",
            "Año": "2022",
            "Sistema principal": "Gilam + Micro Cinor sobre riel",
            "Temperatura de color": "2700K",
            "CRI": "≥ 92",
            "Iluminancia general": "< 50 lux",
            "Iluminancia de barra": "200–350 lux",
            "Acabado riel": "Negro mate",
        }
    },
}


class Command(BaseCommand):
    help = 'Populate lead, quote, bloques y ficha_tecnica para todos los proyectos'

    def handle(self, *args, **options):
        updated = 0
        skipped = 0
        for nombre, data in PROYECTOS.items():
            try:
                proyecto = Proyecto.objects.get(nombre=nombre)
                for field, value in data.items():
                    setattr(proyecto, field, value)
                proyecto.save(update_fields=list(data.keys()))
                self.stdout.write(self.style.SUCCESS(
                    f'  {nombre}: actualizado'
                ))
                updated += 1
            except Proyecto.DoesNotExist:
                self.stdout.write(self.style.WARNING(
                    f'  {nombre}: proyecto no encontrado en DB — omitido'
                ))
                skipped += 1

        self.stdout.write(self.style.SUCCESS(
            f'\nListo: {updated} proyectos actualizados, {skipped} omitidos.'
        ))
