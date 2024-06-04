import pickle 
import streamlit as st 

#model= pickle.load(open ('emisi.sav'), 'rb')

# Membuka file dengan mode 'rb' (read binary)
with open('emisi.sav', 'rb') as file:
    # Memuat model dari file menggunakan pickle.load()
    model = pickle.load(file)

st.title('Prediksi Gas Emisi yang dikeluarkan Mobil')

make_to_code = {'FORD': 577,'CHEVROLET': 515,'BMW': 501,'MERCEDES-BENZ': 365,'PORSCHE': 296,'GMC': 289,'TOYOTA': 276,'AUDI': 263,'NISSAN': 213,'MINI': 200,'JEEP': 200,
    'KIA': 192,'VOLKSWAGEN': 187,'HYUNDAI': 184,'DODGE': 180,'HONDA': 164,'CADILLAC': 141,'LEXUS': 129,'MAZDA': 127,'SUBARU': 119,'JAGUAR': 118,'VOLVO': 118,'BUICK': 92,
    'INFINITI': 87,'LINCOLN': 81,'LAND ROVER': 76,'MITSUBISHI': 73,'RAM': 72,'CHRYSLER': 64,'FIAT': 56,'MASERATI': 52,'ACURA': 51,'ROLLS-ROYCE': 48,'ASTON MARTIN': 39,
    'LAMBORGHINI': 37,'BENTLEY': 35,'SCION': 21,'ALFA ROMEO': 19,'GENESIS': 14,'SMART': 7,'SRT': 2,'BUGATTI': 2}

car_models= {'F-150 FFV': 32, 'F-150 FFV 4X4': 31, 'MUSTANG': 27, 'FOCUS FFV': 24, 'F-150 4X4': 20, 'F-150': 19, 'SONIC 5': 18, 'ATS': 18, 'JETTA': 18, 'COMPASS': 18, 
    'CAMARO': 17, 'SONIC': 17, 'SIERRA': 16, 'COROLLA': 16, 'ACCORD': 16, 'PATRIOT': 16, 'SILVERADO': 16, 'SILVERADO 4WD': 16, 'TACOMA 4WD': 16, 'SIERRA 4WD': 16, 
    'PASSAT': 15, 'CHARGER FFV': 15, 'FUSION': 15, 'FORTE 5': 15, 'FORTE KOUP': 15, 'CANYON': 14, 'COLORADO': 14, 'BEETLE': 14, 'ELANTRA': 13, 'CRUZE': 13, 'FORTE': 13, 
    'EDGE AWD': 13, 'FIT': 13, 'LEGACY AWD': 13, 'OUTBACK AWD': 13, 'ELANTRA GT': 12, 'FORESTER AWD': 12, '200 FFV': 12, 'MUSTANG CONVERTIBLE': 12, 'FRONTIER': 12, 
    'LANCER': 12, 'SOUL': 12, 'BRZ': 11, 'Sierra 4WD': 11, 'COLORADO 4WD': 11, 'CANYON 4WD': 11, 'A8L': 11, 'FOCUS': 10, 'SILVERADO FFV': 10, 'BEETLE CONVERTIBLE': 10, 
    'SENTRA': 10, 'EQUINOX AWD': 10, 'EQUINOX': 10, 'R8': 10, 'R8 SPYDER': 10, 'COMPASS 4X4': 10, 'SIERRA 4WD FFV': 10, 'ESCAPE': 10, 'TERRAIN': 10, 'TERRAIN AWD': 10, 
    'F-150 (LT Tire Pkg)': 10, 'SIERRA FFV': 10, 'F-150 FFV (Payload Pkg)': 10, 'SILVERADO 4WD FFV': 10, 'EXPLORER FFV AWD': 10, 'COOPER S CONVERTIBLE': 10, 'Q50 AWD': 10, 
    'VERANO': 10, 'CAMRY': 10, 'A5 QUATTRO': 10, 'A4 QUATTRO': 10, 'SONATA': 10, 'ACCENT': 10, 'COOPER CONVERTIBLE': 10, 'Silverado 4WD': 10, 'RIO': 9, 'CTS AWD': 9, 
    'MAZDA3 5-DOOR': 9, 'Q70 AWD': 9, 'CTS': 9, 'FIESTA': 9, 'S5': 9, 'ATS AWD': 9, 'ESCAPE AWD': 9, 'F-150 FFV (LT Tire Pkg)': 9, 'A6 QUATTRO': 9, 'F-150 (Payload Pkg)': 9,
 'FRONTIER 4WD': 9, 'CIVIC COUPE': 9, 'MALIBU': 9, 'CHALLENGER': 9, 'OUTLANDER 4WD': 9, 'CX-5': 9, 'CHARGER (MDS)': 9, 'F-150 4X4 (LT Tire Pkg)': 9, 'SPARK': 9, 
 'RVR': 9, 'TUNDRA 4WD': 9, 'TUNDRA': 9, 'CT6 AWD': 9, 'TUCSON': 9, 'TACOMA': 9, 'OPTIMA': 9, 'MKC AWD': 9, 'TRAX': 8, 'Q5': 8, 'Silverado': 8, 'M4 COUPE': 8, 
 'MKZ AWD': 8, 'EXPLORER FFV': 8, 'M4 CABRIOLET': 8, 'PATRIOT 4X4': 8, 'F-150 FFV 4X4 (LT Tire Pkg)': 8, 'IMPREZA WAGON AWD': 8, 'Sierra': 8, 'CAMARO ZL1': 8, 
 'IMPREZA AWD': 8, 'CORVETTE': 8, 'IMPALA': 8, 'EDGE': 8, 'TIGUAN': 8, 'F-150 4X4 (Payload Pkg)': 8, 'Elantra': 8, '911 CARRERA CABRIOLET': 8, 
 'COOPER S COUNTRYMAN ALL4': 8, 'MIRAGE': 8, 'A8': 8, 'MICRA': 8, 'COOPER S 5 DOOR': 8, 'COOPER S 3 DOOR': 8, 'COOPER 5 DOOR': 8, 'SORENTO AWD': 8, 
 'GOLF': 8, 'JUKE': 8, 'GOLF GTI': 8, 'M6 CABRIOLET': 8, 'JOHN COOPER WORKS COUNTRYMAN ALL4': 8, 'M6 GRAN COUPE': 8, 'YUKON XL 4WD': 8, 'TAURUS FFV AWD': 8, 
 '911 CARRERA': 8, '911 CARRERA 4S': 8, 'CHEROKEE 4X4 ACTIVE DRIVE II': 8, '911 CARRERA S CABRIOLET': 8, '911 CARRERA S': 8, 'REGAL': 8, 'MX-5': 8, 
 '911 CARRERA 4S CABRIOLET': 8, '911 CARRERA 4': 8, 'SPORTAGE': 8, 'MAZDA3 4-DOOR': 8, 'VELOSTER TURBO': 8, '911 CARRERA 4 CABRIOLET': 8, 'SPORTAGE AWD': 8,
  'CHALLENGER (MDS)': 7, 'MAZDA5': 7, 'CHARGER': 7, 'VELOSTER': 7, 'JOHN COOPER WORKS CONVERTIBLE': 7, 'RVR 4WD': 7, 'CX-5 4WD': 7, '370Z ROADSTER': 7, 'YUKON 4WD': 7,
   'SAVANA 3500 PASSENGER': 7, 'SAVANA 2500 PASSENGER': 7, 'ALTIMA': 7, 'Camaro': 7, 'JOURNEY FFV': 7, 'SORENTO': 7, 'VERSA': 7, 'TAURUS FFV': 7, 'CHEROKEE': 7, 
   'FUSION AWD': 7, 'MAZDA3 5-DOOR (SIL)': 7, 'ILX': 7, 'COOPER 3 DOOR': 7, 'EXPRESS 3500 PASSENGER': 7, '500L': 7, 'F-150 FFV 4X4 (Payload Pkg)': 7, 'HR-V AWD': 7, 
   'EXPRESS 2500 PASSENGER': 7, 'HR-V': 7, 'S4': 7, 'Corolla': 7, 'WRANGLER UNLIMITED 4X4': 6, '911 TARGA 4S': 6, 'YUKON XL': 6, '370Z': 6, '911 TARGA 4': 6, 
   '911 CARRERA GTS CABRIOLET': 6, 'YUKON': 6, '911 CARRERA GTS': 6, '911 CARRERA 4 GTS CABRIOLET': 6, '911 CARRERA 4 GTS': 6, 'JOHN COOPER WORKS': 6, 
   'HIGHLANDER': 6, 'LX 570': 6, 'K900': 6, 'Colorado': 6, 'CLA 250': 6, 'GT-R': 6, 'RENEGADE 4X4': 6, 'ACADIA AWD': 6, 'ACADIA': 6, 'M6': 6, 'RENEGADE FFV': 6,
    'CHEROKEE FFV': 6, 'GS 350 AWD': 6, 'ES 350': 6, 'MAZDA3 4-DOOR (SIL)': 6, 'TUCSON AWD': 6, 'SANTA FE SPORT AWD': 6, 'BOXSTER GTS': 6, 'MKZ': 6, 
    '435i xDRIVE COUPE': 6, '435i COUPE': 6, 'M3': 6, 'FLYING SPUR': 6, 'E 300 4MATIC': 6, '340i xDRIVE': 6, 'G 550': 6, 'SL 550': 6, '320i': 6,
     'COOPER CLUBMAN': 6, '340i': 6, 'COOPER COUNTRYMAN': 6, 'Q7': 6, 'IMPALA FFV': 6, 'COOPER S CLUBMAN': 6, 'XC60 T6 AWD': 6, 'XC60 T5 AWD': 6, 
     'V60 T6 AWD': 6, 'MKX AWD': 6, 'COOPER S PACEMAN ALL4': 6, 'S60 T6 AWD': 6, 'WRX AWD': 6, 'SQ5': 6, 'JOHN COOPER WORKS PACEMAN ALL4': 6, 'WRX': 6,
      '428i COUPE': 6, 'LANCER SPORTBACK': 6, 'TERRAIN FFV': 6, 'MKS AWD': 6, 'CAYMAN GTS': 6, 'Z4 sDRIVE28i': 6, 'T-150 WAGON FFV': 6, '1500 4X4 (MDS)': 6,
       '1500 FFV': 6, 'CIVIC SEDAN': 6, '500 CABRIO': 6, '500 ABARTH HATCHBACK': 6, '500 ABARTH CABRIO': 6, 'Canyon': 6, 'GRAND CARAVAN FFV': 6, 
       'Mustang Convertible': 6, 'RONDO': 6, 'tC': 6, 'DART': 6, 'CHARGER AWD FFV': 6, 'YARIS': 6, 'VENZA 4WD': 6, 'VENZA': 6, 'SUBURBAN': 6, 'SUBURBAN 4WD': 6,
        'TAHOE': 6, 'TAHOE 4WD': 6, 'TRAVERSE': 6, 'XV CROSSTREK AWD': 6, 'CX-3': 6, '300 FFV': 6, '300 AWD FFV': 6, 'RAV4 AWD': 6, '1500 4X4 FFV': 6,
         '500 HATCHBACK': 6, 'Mustang': 6, 'EXPLORER AWD': 6, 'LACROSSE': 6, 'LACROSSE AWD': 6, 'REGAL AWD': 6, '200 AWD FFV': 6, 'FIESTA SFE': 6, 
         'EQUINOX AWD FFV': 6, 'BOXSTER': 6, 'CORVETTE Z06': 6, 'Sierra 4WD AT4': 6, 'EQUINOX FFV': 6, 'CAMARO SS': 6, 'CAYMAN': 6, 'CAYMAN S': 6, 
         'TRANSIT CONNECT WAGON LWB FFV': 6, 'QX50 AWD': 6, 'BOXSTER S': 6, 'RANGE ROVER EVOQUE': 5, 'MUSTANG (Performance Pkg)': 5, 'CONTINENTAL AWD': 5,
          'QUATTROPORTE SQ4': 5, 'YUKON XL FFV': 5, 'GX 460': 5, 'QUATTROPORTE GTS': 5, '500X': 5, 'Impala': 5, 'G80 AWD': 5, 'CIVIC HATCHBACK': 5, 'ES 300h': 5,
           'GRAND CHEROKEE 4X4': 5, 'Colorado 4WD': 5, 'YUKON FFV': 5, 'OPTIMA HYBRID': 5, 'IS 350 AWD': 5, 'TRANSIT CONNECT VAN FFV': 5, 'YUKON XL 4WD FFV': 5,
            'AVENTADOR COUPE': 5, 'RAV4': 5, 'TAHOE FFV': 5, 'PHANTOM': 5, 'A3': 5, 'TLX': 5, 'MDX SH-AWD': 5, 'TIGUAN 4MOTION': 5, '1500 (MDS)': 5, 'GHOST': 5,
             'GHOST EWB': 5, 'PHANTOM EWB': 5, 'SUBURBAN 4WD FFV': 5, 'WRAITH': 5, 'FR-S': 5, 'CC': 5, '4RUNNER 4WD': 5, 'SIENNA': 5, 'CAMRY HYBRID LE': 5,
              'CAMRY HYBRID XLE/SE': 5, 'CTS Vsport': 5, 'ESCALADE 4WD': 5, '911 GT3': 5, 'CHALLENGER SRT HELLCAT': 5, 'SUBURBAN FFV': 5, 'MAZDA6': 5, 'ATS-V': 5, 
              'B 250': 5, 'X4 M40i': 5, 'V60 T5': 5, '1500 4X4': 5, 'GLA 250 4MATIC': 5, 'WRANGLER 4X4': 5, 'NV200 CARGO VAN': 5, 'ROGUE AWD': 5, 'F-TYPE S COUPE': 5,
               'F-TYPE COUPE': 5, 'Q60 AWD': 5, 'T-150 WAGON': 5, 'PRIUS': 5, 'XC90 T6 AWD': 5, '328d xDRIVE TOURING': 5, 'Accord': 5, 'A7 QUATTRO': 5, 'Canyon 4WD': 5
               , 'XTS': 5, 'Elantra GT': 5, 'PILOT AWD': 5, 'X1 xDRIVE28i': 5, 'M5': 5, 'S6': 5, 'S7': 5, 'S8': 5, 'CONTINENTAL GT': 5, 'Soul': 5, 'MULSANNE': 5, 
               'XTS Vsport AWD': 5, 'SONATA HYBRID': 5, 'CRUZE DIESEL': 5, 'SONIC 5 RS': 5, 'SONIC RS': 5, 'Acadia': 5, 'F-TYPE S CONVERTIBLE': 5, 
               '640i xDRIVE GRAN COUPE': 5, 'QX60 AWD': 5, '650i xDRIVE CABRIOLET': 5, 'F-TYPE CONVERTIBLE': 5, '650i xDRIVE COUPE': 5, '650i xDRIVE GRAN COUPE': 5,
                'QX80 4WD': 5, 'A5 CABRIOLET QUATTRO': 5, 'QX70 AWD': 5, 'DART FFV': 5, 'CR-V AWD': 5, 'CHEROKEE 4X4': 5, 'A4': 5, 'X6 xDRIVE50i': 5, 'CIVIC': 5, 
                'FUSION HYBRID': 5, 'CR-V': 5, 'FIESTA ST': 5, 'X5 xDRIVE50i': 5, 'ENCLAVE': 5, 'V8 VANTAGE': 5, 'V8 VANTAGE S': 5, 'VANQUISH': 5,
                 'CHEROKEE TRAILHAWK 4X4': 5, 'CITY EXPRESS': 4, 'Sierra FFV': 4, 'Terrain AWD': 4, 'Sierra 4WD FFV': 4, 'Yukon 4WD': 4, 'X5 xDRIVE35d': 4,
                  'JETTA TDI (modified)': 4, 'JETTA GLI': 4, 'M6 COUPE': 4, 'RLX HYBRID': 4, 'M235i CABRIOLET': 4, 'TOUAREG': 4, 'XTS AWD': 4, 'RAPIDE S': 4,
                   'ALPINA B6 xDRIVE GRAN COUPE': 4, 'V12 VANTAGE S': 4, '640i xDRIVE CABRIOLET': 4, 'VANTAGE GT': 4, '428i GRAN COUPE': 4,
                    'CONTINENTAL GT CONVERTIBLE': 4, 'S3': 4, 'Q3': 4, 'A4 ALLROAD QUATTRO': 4, 'CADENZA': 4, 'Acadia AWD': 4, 'BEETLE TDI (modified)': 4,
                     'DART GT': 4, 'DART TURBO AERO': 4, 'PHANTOM DROPHEAD COUPE': 4, 'PHANTOM COUPE': 4, '500 HATCHBACK TURBO': 4, 'E150 VAN FFV': 4, 
                     'PANAMERA 4S': 4, 'Forte': 4, 'CAYENNE TURBO S': 4, 'CAYENNE TURBO': 4, 'CAYENNE': 4, 'EXPLORER': 4, 'TAURUS': 4, 'TAURUS AWD': 4,
                      'XTERRA 4WD': 4, 'xB': 4, 'FORTWO CABRIOLET': 4, 'CHARGER AWD': 4, 'PRIUS v': 4, 'G70 AWD': 4, 'TRAVERSE AWD': 4, 'Yukon XL 4WD FFV': 4, 
                      '300': 4, 'SIENNA AWD': 4, 'SEQUOIA 4WD': 4, 'PRIUS c': 4, 'CHALLENGER SRT (MDS)': 4, 'HIGHLANDER HYBRID AWD': 4, 'HIGHLANDER AWD': 4, 
                      '300 (MDS)': 4, 'COROLLA LE ECO (2-mode)': 4, 'TOWN & COUNTRY FFV': 4, 'AVALON': 4, 'Yukon XL 4WD': 4, 'X5 xDRIVE35i': 4, 
                      'EDGE (Start/Stop)': 4, 'CRUZE HATCHBACK': 4, 'GT': 4, 'G90 AWD': 4, 'IONIQ': 4, 'ACCORD SEDAN': 4, 'ACCORD COUPE': 4, 'Sonata': 4, 
                      'Santa Fe AWD': 4, 'DURANGO AWD': 4, 'RS 7': 4, 'S5 CABRIOLET': 4, 'CRUZE LIMITED': 4, 'Accent': 4, 'M2': 4, 'Golf': 4,
                       'COOPER CLUBMAN ALL4': 4, 'RDX AWD': 4, 'MX-5 (SIL)': 4, 'EXPEDITION 4X4': 4, 'AMG C 63': 4, 'V60 CC T5 AWD': 4, 
                       '1500 Classic 4X4': 4, 'S60 T5': 4, 'Legacy AWD': 4, 'GOLF R': 4, 'YARIS HATCHBACK': 4, 'Outback AWD': 4, '440i COUPE': 4, '440i xDRIVE COUPE': 4,
                        'M240i CABRIOLET': 4, 'M240i COUPE': 4, 'AMG GLE 63 S 4MATIC': 4, 'AMG G 63': 4, 'XT5 AWD': 4, 'AMG C 63 S': 4, 'COOPER COUNTRYMAN ALL4': 4, 
                        'JOHN COOPER WORKS CLUBMAN ALL4': 4, '328d xDRIVE': 4, 'V60 T5 AWD': 4, 'RENEGADE': 4, 'CHEROKEE 4X4 FFV': 4, 'X3 xDRIVE28i': 4, 
                        'X3 xDRIVE35i': 4, 'XC90 T5 AWD': 4, 'Sentra': 4, 'X6 M': 4, 'GENESIS COUPE': 4, 'GENESIS AWD': 4, 'X6 xDRIVE35i': 4, 'Qashqai': 4, 
                        'Z4 sDRIVE35i': 4, '500': 4, 'TRANSIT CONNECT VAN': 4, 'ENCLAVE AWD': 4, 'Civic Coupe': 4, 'AVENTADOR ROADSTER': 4, 'Versa': 4, 
                        '750i xDRIVE': 4, 'CROSSTREK AWD': 4, 'S60 T5 AWD': 4, '4RUNNER 4WD (Part-Time 4WD)': 4, '1500': 4, 'GOLF SPORTWAGEN': 4,
                         'PATHFINDER 4WD PLATINUM': 4, 'S90 T6 AWD': 4, 'RC 350 AWD': 4, 'Civic Sedan': 4, 'E 400 4MATIC WAGON': 4, 'E 400 4MATIC': 4, 
                         'C 300 4MATIC': 4, 'B 250 4MATIC': 4, 'NAVIGATOR 4X4': 4, 'Explorer AWD': 4, 'PATHFINDER 4WD': 4, 'CX-9 4WD': 4, 'Sportage AWD': 4,
                          'Charger (MDS)': 4, 'Edge AWD': 4, 'Silverado FFV': 4, 'S 550 4MATIC SWB': 4, 'LS 460 AWD': 4, 'S 550 4MATIC LWB': 4, 
                          'MAZDA3 5-DOOR (i-ELOOP)': 4, 'COOPER S COUPE': 4, 'MKZ HYBRID': 4, 'ACCORD HYBRID': 4, 'M240i Cabriolet': 4, 'Q70 HYBRID': 4, 
                          'MAZDA3 4-DOOR (i-ELOOP)': 4, 'Equinox AWD': 4, 'Silverado 4WD FFV': 4, 'QX60': 4, 'Blazer': 4, 'COOPER S ROADSTER': 4, 'M240i Coupe': 4,
                           'M240i Coupe M Performance': 4, 'Camaro SS': 4, 'CR-Z': 4, 'PILOT': 4, 'JOHN COOPER WORKS ROADSTER': 4, 'ODYSSEY': 4, 
                           'JOHN COOPER WORKS COUPE': 4, 'QX60 HYBRID AWD': 4, 'GRANTURISMO CONVERTIBLE': 4, 'COOPER PACEMAN': 4, 'COOPER ROADSTER': 4, 
                           'CLS 550 4MATIC': 4, 'JUKE AWD': 4, 'RX 350 AWD': 4, 'ARMADA 4WD': 4, 'RX 450h AWD': 4, 'Tahoe 4WD': 4, 'Charger FFV': 4, 
                           'Continental AWD': 4, 'MAXIMA': 4, 'Q50': 4, 'MURANO AWD': 4, 'SLK 250': 4, 'Suburban 4WD FFV': 4, 'PATHFINDER': 4, 'Suburban 4WD': 4, 
                           'MKT AWD': 4, '440i xDrive Coupe': 4, 'GS 450h': 4, 'Rio': 4, 'Escape AWD': 4, 'LS 460 L AWD': 4, 'SANTA FE SPORT': 4, 
                           '335i xDRIVE GRAN TURISMO': 3, 'GHIBLI': 3, '911 Carrera 4S': 3, 'GRANTURISMO': 3, 'GOLF ALLTRACK': 3, 'JUKE NISMO RS': 3, 
                           'JUKE NISMO RS AWD': 3, 'GOLF SPORTWAGEN 4MOTION': 3, 'GOLF SPORTWAGON': 3, 'RAV4 LE/XLE': 3, 'MURANO': 3, 'PROMASTER CITY': 3, 
                           'Fit': 3, '428i xDRIVE COUPE': 3, '535i xDRIVE GRAN TURISMO': 3, 'MKT LIVERY AWD': 3, '1500 4X4 ECODIESEL': 3, 
                           '550i xDRIVE GRAN TURISMO': 3, '1500 ECODIESEL': 3, 'RANGE ROVER SUPERCHARGED LWB': 3, '750Li xDRIVE': 3, 'X3 M40i': 3, 'SEDONA SXL': 3,
                            'Civic Hatchback': 3, 'MAZDA6 (i-ELOOP)': 3, 'Q50 HYBRID AWD': 3, 'Wrangler 4X4': 3, 'Regal AWD': 3, 'Envision AWD': 3, 
                            'SONATA SPORT/LIMITED': 3, 'YUKON XL DENALI 4WD': 3, 'Sorento AWD': 3, 'YUKON DENALI 4WD': 3, 'Z4 sDRIVE35is': 3, 'E 250 BLUETEC 4MATIC': 3,
                             'ENCORE': 3, 'ENCORE AWD': 3, 'F-150 4X4 XL/XLT': 3, 'Frontier 4WD': 3, 'Frontier': 3, 'ACTIVEHYBRID 5': 3, 'HURACAN': 3, 'Blazer AWD': 3,
                              'NAVIGATOR L 4X4': 3, 'V90 T6 AWD': 3, 'S 600': 3, 'S 550 4MATIC COUPE': 3, 'V90 CC T6 AWD': 3, '911 Carrera S Cabriolet': 3,
                               '328i xDRIVE TOURING': 3, '911 Carrera S': 3, 'CLA 250 4MATIC': 3, 'Q70': 3, 'RS 3': 3, 'Civic Hatchback Sport': 3, 'RC F': 3, 
                               'F-TYPE Convertible': 3, 'NX 300h AWD': 3, 'NX 200t AWD F SPORT': 3, 'NX 200t AWD': 3, 'RANGE ROVER SPORT SUPERCHARGED': 3,
                                'RANGE ROVER SUPERCHARGED': 3, '86': 3, 'SL 450': 3, 'MKT LIVERY': 3, 'Tundra 4WD': 3, '1500 4X4 eTorque': 3, 'AMG G 65': 3, 
                                'XT5': 3, 'Silverado 4WD Trail Boss': 3, 'LR4': 3, 'CX-3 4WD': 3, 'QUATTROPORTE S': 3, 'GHIBLI S': 3, 'RC 300 AWD': 3, 'IS 300 AWD': 3, 
                                'ESCAPE FFV': 3, 'Veloster Turbo': 3, 'TSX': 3, 'DISCOVERY SPORT': 3, 'Tucson AWD': 3, 'Malibu': 3, 'Tacoma 4WD': 3, 
                                'Corolla Hatchback': 3, 'AMG S 65': 3, 'Tahoe 4WD FFV': 3, 'ALTIMA SR': 3, 'Crosstrek AWD': 3, 'Impreza 4-Door AWD': 3, 
                                'Impreza 5-Door AWD': 3, '1500 Classic': 3, 'OPTIMA HYBRID EX': 3, 'BEETLE DUNE': 3, 'RAV4 HYBRID AWD': 3, 'METRIS PASSENGER': 3,
                                 'AMG SL 63': 3, 'METRIS CARGO': 3, 'GLE 550 4MATIC': 3, 'GRAND CHEROKEE 4X4 (MDS)': 3, 'GLE 400 4MATIC': 3, 'SEDONA': 3,
                                  'F-TYPE Coupe': 3, 'AMG SL 65': 3, 'Challenger': 3, 'Equinox': 3, '328i xDRIVE GRAN TURISMO': 3, 'Corvette': 3, 'AMG GLE 43 4MATIC': 3,
                                   'Camaro ZL1': 3, 'LS 460': 3, '320i xDRIVE': 3, 'Golf GTI': 3, 'AMG SLC 43': 3, 'GLC 300 4MATIC': 3, 'GLS 450 4MATIC': 3, 
                                   'Jetta GLI': 3, 'GLS 550 4MATIC': 3, 'Yukon 4WD FFV': 3, 'SLC 300': 3, 'LS 600h L': 3, 'COOPER S CLUBMAN ALL4': 3, 'XFR': 3, 
                                   'XC60 T5': 3, '911 Carrera 4S Cabriolet': 3, 'ENVISION AWD': 3, 'CT6': 3, 'TTS COUPE QUATTRO': 3, 'RS 5': 3, 'YUKON 4WD FFV': 3, 
                                   'CT 200h': 3, 'XJR LWB': 3, 'Cherokee': 3, 'XJR': 3, 'Cherokee 4X4 Active Drive I': 3, 'FOCUS RS AWD': 3, '500X AWD': 3, 'CTS-V': 3, 
                                   'GS 350': 3, 'Challenger (MDS)': 3, 'TAHOE 4WD FFV': 3, 'Wrangler Unlimited 4X4': 3, 'TT COUPE QUATTRO': 3, 'TT ROADSTER QUATTRO': 3,
                                    'IS 350': 3, 'LACROSSE eASSIST': 3, 'Cooper S Countryman ALL4': 3, 'Wrangler JL Unlimited 4X4': 3, 'A6 quattro': 3, 'CC 4MOTION': 3, 
                                    'PANAMERA 4': 3, 'FORTWO COUPE': 3, 'PANAMERA': 3, 'GL 350 BLUETEC 4MATIC': 3, 'Cooper Clubman ALL4': 3, 'Cooper Convertible': 3, 
                                    'Cooper Countryman ALL4': 3, 'Cooper S 3 Door': 3, 'Cooper S 5 Door': 3, 'NEW WRANGLER UNLIMITED 4X4': 3, 'Cooper 5 Door': 3, 
                                    'NEW WRANGLER 4X4': 3, 'Cooper S Clubman ALL4': 3, 'Cooper S Convertible': 3, '440i Coupe': 3, 'John Cooper Works 3 Door': 3,
                                     'John Cooper Works Clubman ALL4': 3, 'CAYENNE S': 3, 'John Cooper Works Convertible': 3, 'CAYENNE GTS': 3, 'TRAX AWD': 3, 
                                     'PANAMERA 4S EXECUTIVE': 3, 'LS 500 AWD': 3, 'John Cooper Works Countryman ALL4': 3, 'Silverado 4WD Custom Trail Boss': 3, 
                                     'CRUZE ECO': 3, 'WRX STI AWD': 3, 'JOURNEY AWD': 3, 'OUTLANDER': 3, 'JOURNEY': 3, 'PASSAT TDI (modified)': 3, 
                                     'EXPRESS 1500 CARGO': 3, 'DURANGO AWD (MDS)': 3, 'TLX SH-AWD': 3, 'M2 Competition': 3, 'A3 QUATTRO': 3, 'Cooper 3 Door': 3, 
                                     'A3 CABRIOLET QUATTRO': 3, 'C-MAX HYBRID': 3, 'Q3 QUATTRO': 3, 'GL 550 4MATIC': 3, 'Mazda3 5-Door': 3, 'GL 450 4MATIC': 3, 
                                     'PANAMERA TURBO EXECUTIVE': 3, 'PANAMERA TURBO': 3, 'PANAMERA S': 3, 'Vantage V8': 3, 'COOPER COUPE': 3, 'Wrangler JL 4X4': 3,
                                      'XV CROSSTREK HYBRID AWD': 3, 'FUSION (Start/Stop)': 3, 'TITAN 4WD': 3, 'Terrain': 3, 'FLEX AWD': 3, 'X4 xDRIVE28i': 3, 
                                      'X3 xDRIVE28d': 3, 'M4 Coupe': 3, 'EQUUS': 3, 'HIGHLANDER HYBRID AWD LE': 3, 'X5 M': 3, 'FLEX': 3, 'TITAN': 3, 
                                      'TRANSIT CONNECT WAGON': 3, 'SRX': 3, 'Outlander 4WD': 3, 'SANTA FE': 3, 'SAVANA 1500 CARGO': 3, 'ROGUE': 3, 
                                      'M4 Coupe Competition': 3, 'CHARGER SRT (MDS)': 3, '300 AWD': 3, '911 TURBO S CABRIOLET': 3, '911 TURBO S': 3, 
                                      '911 TURBO CABRIOLET': 3, 'CHARGER AWD (MDS)': 3, 'E 550 COUPE': 3, 'E 550 4MATIC': 3, 'COROLLA LE ECO (1-mode)': 3,
                                       '911 TURBO': 3, 'CHALLENGER SRT': 3, 'E 550 CABRIOLET': 3, 'Corvette ZR1': 2, 'AMG C 63 CABRIOLET': 2, 'Corvette Z06': 2, 
                                       'Kona': 2, '430i xDrive Gran Coupe': 2, 'NEW COMPASS': 2, 'Range Rover 5.0 Supercharged': 2, 'Range Rover 3.0': 2, 'LEVANTE': 2, 
                                       'AMG C 63 COUPE': 2, 'Taurus FFV': 2, 'Cayenne S': 2, 'CHEROKEE 4X4 ACTIVE DRIVE LOCK': 2, 'CHEROKEE 4X4 ACTIVE DRIVE I': 2,
                                        'LEVANTE S': 2, 'Challenger SRT Hellcat': 2, 'Levante Trofeo': 2, 'F-TYPE R AWD Coupe': 2, 'Cherokee 4X4 Active Drive II': 2,
                                         '911 Targa 4S': 2, 'Boxster': 2, 'A5 Sportback quattro': 2, 'Cayman GTS': 2, 'Boxster GTS': 2, 'Boxster S': 2, 
                                         'RANGE ROVER EVOQUE CONVERTIBLE': 2, 'A5 Cabriolet quattro': 2, 'Cayenne': 2, 'Shelby GT350 Mustang': 2, 'Stinger AWD': 2, 
                                         'FORTE (MPI)': 2, 'A7 quattro': 2, 'Colorado ZR2 4WD': 2, '430i xDrive Coupe': 2, 'A5 quattro': 2, 'MKC AWD (Start/Stop)': 2, 
                                         'Kona AWD': 2, 'NEW COMPASS 4X4': 2, 'Levante GTS': 2, 'T-150 Wagon': 2, 'Q8': 2, 'Cayman': 2, 'Renegade': 2, 
                                         'Cayman S': 2, '330i xDRIVE': 2, '230i xDrive Cabriolet': 2, 'Expedition 4X4': 2, '540i xDRIVE': 2, '530i xDRIVE': 2, 
                                         '440i xDRIVE GRAN COUPE': 2, 'Fiesta': 2, '440i xDRIVE CABRIOLET': 2, '430i xDRIVE GRAN COUPE': 2, 'Expedition MAX 4X4': 2,
                                          '430i xDRIVE COUPE': 2, '430i xDRIVE CABRIOLET': 2, '340i xDRIVE GRAN TURISMO': 2, '330i xDRIVE TOURING': 2, 
                                          '330i xDRIVE GRAN TURISMO': 2, '230i xDRIVE COUPE': 2, 'SONATA HYBRID SE': 2, '230i xDRIVE CABRIOLET': 2, '230i COUPE': 2,
                                           'Huracan Spyder AWD': 2, '1500 Classic FFV': 2, 'Optima': 2, 'Optima Hybrid': 2, 'Tahoe FFV': 2, '1500 Classic 4X4 FFV': 2, 
                                           'Huracan Spyder': 2, 'Explorer FFV AWD': 2, 'Cullinan': 2, 'Dawn': 2, 'Ghost': 2, 'Ghost EWB': 2, 'Bentayga': 2, 'Spark': 2,
                                            'M240i xDRIVE CABRIOLET': 2, 'Escape FFV': 2, 'EcoSport AWD': 2, 'Sonata Hybrid': 2, 'F-TYPE R AWD Convertible': 2,
                                             'Mustang Bullitt': 2, 'Mazda3 4-Door': 2, 'S5 Cabriolet': 2, 'Mustang (Performance Pkg)': 2, 'Aventador Coupe': 2,
                                              'FOCUS (Start/Stop)': 2, 'Veloster': 2, 'F-TYPE Coupe R-Dynamic': 2, 'S5 Sportback': 2, 'TT Coupe quattro': 2, 
                                              '124 SPIDER': 2, 'Edge': 2, 'Fusion Hybrid': 2, 'AMG C 63 S CABRIOLET': 2, 'CRUZE HATCHBACK PREMIER': 2, 
                                              'Huracan Coupe': 2, 'TT Roadster quattro': 2, 'Trax': 2, 'COLORADO ZR2 4WD': 2, 'Traverse AWD': 2, '1500 eTorque': 2, 
                                              'Huracan Coupe AWD': 2, '1500 HFE eTorque': 2, 'Fusion': 2, 'Escape': 2, 'M240i xDRIVE COUPE': 2, 'PACIFICA': 2, 
                                              'Transit Connect Van FFV': 2, 'A4 allroad quattro': 2, 'Civic Coupe Si': 2, '230i xDrive Coupe': 2, 
                                              'M240i xDrive Coupe M Performance': 2, 'Titan 4WD Pro-4X': 2, 'CHEROKEE 4X4 ACTIVE DRIVE I FFV': 2, 
                                              'Suburban FFV': 2, 'TT RS': 2, 'Sedona': 2, 'Regal': 2, 'M4 Cabriolet': 2, 'Durango AWD': 2, 'Range Rover Sport 3.0': 2,
                                               'Escalade 4WD': 2, 'Titan 4WD': 2, 'Sentra Nismo': 2, 'Charger AWD FFV': 2, 'WRANGLER JK 4X4': 2,
                                                'WRANGLER JK UNLIMITED 4X4': 2, 'RANGE ROVER VELAR': 2, '911 Carrera': 2, 'IS 300': 2, '911 Carrera Cabriolet': 2,
                                                 '911 Carrera GTS': 2, 'LC 500': 2, 'LC 500h': 2, '911 Carrera GTS Cabriolet': 2, '911 Carrera T': 2, 'LS 500h AWD': 2,
                                                  'NX 300 AWD': 2, 'AMG C 43 4MATIC': 2, 'AMG CLA 45 4MATIC': 2, '911 Carrera 4': 2, 'F-TYPE COUPE R-DYNAMIC': 2, 
                                                  'F-TYPE CONVERTIBLE R-DYNAMIC': 2, '911 Carrera 4 Cabriolet': 2, 'MKZ Hybrid': 2, 'M850i xDrive Coupe': 2, 
                                                  '500 ABARTH': 2, 'Micra': 2, 'M850i xDrive Cabriolet': 2, 'Renegade 4X4': 2, '370Z Roadster': 2, 
                                                  'CIVIC HATCHBACK SPORT': 2, 'Sentra (Turbo)': 2, 'M5 Competition': 2, 'Armada 4WD': 2, 'Altima SR/Platinum': 2, 
                                                  'KONA AWD': 2, 'Yukon XL FFV': 2, 'M4 CS': 2, 'Grand Caravan FFV': 2, 'X1 xDrive28i': 2, 
                                                  'Mirage G4': 2, 'X2 xDrive28i': 2, 'CHALLENGER GT AWD FFV': 2, 'Pathfinder 4WD': 2, 'CRUZE HATCHBACK DIESEL': 2, 
                                                  'Pathfinder 4WD Platinum': 2, 'X3 xDrive30i': 2, 'Mirage': 2, 'Qashqai AWD': 2, 'X4 xDrive30i': 2, 'X5 xDrive50i': 2,
                                                   'X7 xDrive50i': 2, 'Enclave AWD': 2, 'M4 Cabriolet Competition': 2, 'Encore AWD': 2, 'AMG GLC 43 4MATIC': 2, 
                                                   'AMG GLS 63 4MATIC': 2, 'AMG C 63 S COUPE': 2, 'COOPER S COUNTRYMAN  ALL4': 2, 'C 300 4MATIC COUPE': 2, 
                                                   'Yukon FFV': 2, 'A3 Cabriolet quattro': 2, 'Transit Connect Wagon LWB': 2, 'Journey FFV': 2, 
                                                   'Transit Connect Wagon LWB FFV': 2, 'JOHN COOPER WORKS 3 DOOR': 2, 'Cherokee 4X4 Active Drive Lock': 2, 
                                                   '440i xDrive Cabriolet': 2, 'MIRAGE G4': 2, '440i xDrive Gran Coupe': 2, 'QASHQAI': 2, 'A3 quattro': 2, 
                                                   'QASHQAI AWD': 2, 'C 300 4MATIC CABRIOLET': 2, 'Transit Connect Van': 2, '911 Targa 4': 2, 'AMG S 63 4MATIC': 2, 
                                                   '124 Spider': 2, 'AMG GT S COUPE': 2, 'AMG GT COUPE': 2, 'Taurus FFV AWD': 2, '911 Targa 4 GTS': 2, 
                                                   'AMG GLE 63 S 4MATIC COUPE': 2, 'AMG GLE 43 4MATIC COUPE': 2, 'Ridgeline AWD': 2, 'Charger': 2, 'EcoSport': 2, 
                                                   'AMG GLC 43 4MATIC COUPE': 2, 'A4 quattro': 2, 'AMG GLA 45 4MATIC': 2, 'Pilot AWD': 2, 'SENTRA (Turbo)': 2, 
                                                   'Civic Sedan Si': 2, 'Compass 4X4': 2, 'C-HR': 2, '911 Carrera 4 GTS Cabriolet': 2, '911 TARGA 4 GTS': 2, 
                                                   'Sportage': 2, 'S 560 4MATIC SWB': 2, 'Odyssey': 2, 'Grand Cherokee 4X4': 2, 'SENTRA NISMO': 2, 
                                                   'S 450 4MATIC SWB': 2, 'Alpina B7 xDrive': 2, 'Civic Type R': 2, 'M240i xDrive Cabriolet': 2, 
                                                   'M240i xDrive Coupe': 2, '911 Carrera 4 GTS': 2, 'S90 T5 AWD': 2, 'RDX AWD A-SPEC': 2, 'Giulia Quadrifoglio': 2, 
                                                   'Mazda6': 2, 'Nautilus': 2, 'Navigator 4X4': 2, 'Compass': 2, 'COROLLA iM': 2, 'Passport AWD': 2, 
                                                   'Stelvio AWD Quadrifoglio': 2, 'IMPREZA 5-DOOR AWD': 2, 'IMPREZA 4-DOOR AWD': 2, 'Mazda3 5-Door (SIL)': 2, 
                                                   'Ghibli S': 2, 'Levante S': 2, 'DAWN': 2, 'TITAN 4WD PRO-4X': 2, 'Quattroporte S': 2, 'RC 350': 2, 
                                                   'F-TYPE Convertible R-Dynamic': 2, 'CT4 AWD': 2, '428i xDRIVE GRAN COUPE': 2, '435i CABRIOLET': 2, 'CT5': 2,
                                                    '435i xDRIVE CABRIOLET': 2, '435i xDRIVE GRAN COUPE': 2, 'RIDGELINE AWD': 2, 'Nautilus AWD': 2, 'CT4': 2, 
                                                    'M3 SEDAN': 2, 'YUKON DENALI XL AWD': 2, 'YUKON DENALI AWD': 2, 'SAVANA 1500 PASSENGER AWD': 2, 
                                                    'SAVANA 1500 PASSENGER': 2, 'SAVANA 1500 CARGO CONV AWD': 2, 'SAVANA 1500 CARGO CONV': 2, 'M235i COUPE': 2, 
                                                    '428i xDRIVE CABRIOLET': 2, '428i CABRIOLET': 2, '335i xDRIVE SEDAN': 2, '335i SEDAN': 2, 'XJL AWD PORTFOLIO': 2,
                                                     'XJ SUPERCHARGED': 2, 'XFR-S': 2, '228i COUPE': 2, 'Q60 COUPE': 2, '228i xDRIVE CABRIOLET': 2, 'Q60 CONVERTIBLE': 2,
                                                      'Q50 HYBRID': 2, 'TUCSON 4WD': 2, 'SONATA HYBRID LIMITED': 2, 'SANTA FE SPORT 4WD': 2, '320i SEDAN': 2,
                                                       'Corsair AWD': 2, '328i SEDAN': 2, 'CT5 AWD': 2, 'SAVANA 1500 CARGO AWD': 2, 'M5 SEDAN': 2, 'E 400 CABRIOLET': 2, 
                                                       'Q60': 2, 'CX-30': 2, 'CX-30 4WD': 2, 'ELANTRA COUPE': 2, 'SANTA FE AWD': 2, '200 SEDAN FFV': 2, '200 SEDAN': 2, 
                                                       'SANTA FE ULTIMATE AWD': 2, '200 CONVERTIBLE FFV': 2, 'X4 xDRIVE35i': 2, '200 CONVERTIBLE': 2, 'ORLANDO': 2,
                                                        'SEDONA SX': 2, 'RANGE ROVER': 2, 'RANGE ROVER SPORT': 2, 'EXPRESS 1500 PASSENGER AWD': 2,
                                                         'EXPRESS 1500 PASSENGER': 2, 'AVENGER': 2, 'SAVANA 3500 PASSENGER FFV': 2, 'AVENGER FFV': 2, 
                                                         'SAVANA 2500 PASSENGER FFV': 2, 'ESCALADE ESV 4WD': 2, 'TRANSIT CONNECT': 2, 'FOCUS SFE FFV': 2,
                                                          'EXPRESS 2500 PASSENGER FFV': 2, 'EXPRESS 3500 PASSENGER FFV': 2, 'FLEX AWD (EcoBoost)': 2, '200': 2,
                                                           'CHARGER SRT HELLCAT': 2, 'F-150 RAPTOR 4X4': 2, 'EXPEDITION 4X4 FFV': 2, 'E350 WAGON FFV': 2, 'EXPEDITION MAX 4X4': 2, 'E150 WAGON FFV': 2, '500L TURBO': 2,
                                                            'DURANGO AWD FFV': 2, 'XJL SUPERCHARGED': 2, 'XKR CONVERTIBLE': 2, 'XKR COUPE': 2, 'PANAMERA GTS': 2, 'LANCER AWD': 2, 'LANCER EVOLUTION': 2, 
                                                            'T-150 Wagon FFV 4WD': 2, 'T-150 Wagon FFV': 2, 'QUEST': 2, 'CAYENNE DIESEL (modified)': 2, 'Gladiator 4X4': 2, 'Mustang Convertible (Performance Pkg)': 2, 
                                                            'XKR-S CONVERTIBLE': 2, 'C 300 4MATIC FFV': 2, '1500 HFE': 2, 'CARGO VAN FFV': 2, 'C 250 COUPE': 2, 'iQ': 2, 'xD': 2, 'MAZDA2': 2, 'JOHN COOPER WORKS CLUBMAN': 2,
                                                             'Transit Connect Van LWB': 2, 'SLS AMG GT COUPE': 2, 'SLK 55 AMG': 2, 'Venue': 2, 'C 63 AMG COUPE': 2, 'E 63 AMG S 4MATIC': 2, 'E 63 AMG S 4MATIC WAGON': 2, 
                                                             'G 63 AMG': 2, 'GL 63 AMG': 2, 'GLK 250 BLUETEC 4MATIC': 2, 'GLK 350 4MATIC': 2, 'ML 350 4MATIC FFV': 2, 'ML 550 4MATIC': 2, 'ML 63 AMG 4MATIC': 2, 
                                                             'S 63 AMG 4MATIC': 2, 'SL 63 AMG': 2, 'SL 65 AMG': 2, 'SLK 350': 2, 'CX-9': 2, 'GHIBLI AWD': 2, 'NAVIGATOR 4X4 FFV': 2, 'RANGE ROVER SPORT V6 3.0 SC FFV': 2,
                                                              'RANGE ROVER EVOQUE COUPE': 2, 'GALLARDO COUPE': 2, 'SOUL ECO Dynamics': 2, 'SORENTO 4WD': 2, 'RIO ECO': 2, 'WRANGLER UNLIMITED 4X4 (4-DOOR)': 2,
                                                               'WRANGLER 4X4 (2-DOOR)': 2, 'XC60 AWD': 2, 'PATRIOT 4X4 TRAIL RATED': 2, 'GRAND CHEROKEE SRT 4X4 (MDS)': 2, 'GRAND CHEROKEE 4X4 FFV': 2, 'XC70 AWD': 2,
                                                                'COMPASS 4X4 TRAIL RATED': 2, 'XKR-S COUPE': 2, 'Silverado 4WD LT Trail Boss': 2, 'RANGE ROVER LWB V8 5.0 SC FFV': 2, 'Forte 5': 2, 'COROLLA MATRIX': 2,
                                                                 'RANGE ROVER SPORT V8 5.0 SC FFV': 2, 'FJ CRUISER 4WD': 2, 'RAV4 LIMITED AWD': 2, 'EOS': 2, 'GOLF WAGON': 2, 'GOLF WAGON TDI (modified)': 2, 'IS 350 C': 2, 
                                                                 'IS 250 C': 2, 'Challenger SRT Hellcat Widebody': 2, 'TOUAREG TDI (modified)': 2, 'IS 250': 2, 'Challenger Widebody (MDS)': 2, 'RANGE ROVER V8 5.0 SC FFV': 2,
                                                                  'Wrangler Unlimited 4X4 eTorque': 2, 'RANGE ROVER V6 3.0 SC FFV': 2, 'S60 AWD': 2, 'CLS 400 4MATIC': 2, 'CLS 63 AMG 4MATIC': 2, 'E 400 COUPE': 2, 
                                                                  'F-TYPE R AWD CONVERTIBLE': 2, 'SIERRA eASSIST 4WD': 2, 'Yaris (SIL)': 2, 'Yaris': 2, 'Q50S RED SPORT AWD': 2, '535i xDRIVE': 2, '535d xDRIVE': 2, 
                                                                  'EXPRESS 1500 CARGO CONV AWD': 2, 'TL AWD': 2, 'F-TYPE R AWD COUPE': 2, 'F-TYPE S CONVERTIBLE AWD': 2, '528i xDRIVE': 2, '335i xDRIVE': 2, '335i': 2,
                                                                   '328i xDRIVE': 2, '4Runner 4WD (Part-Time 4WD)': 2, 'Yaris Hatchback': 2, 'TRANSIT CONNECT WAGON FFV': 2, 'SHELBY GT350 MUSTANG': 2, 'FOCUS ST': 2, 
                                                                   '4Runner 4WD': 2, 'iM': 2, 'FLEX AWD GTDI': 2, 'RAV4 LIMITED/SE AWD': 2, '550i xDRIVE': 2, '740Li xDRIVE': 2, 'YARIS (SIL)': 2, 'ACTIVEHYBRID 3': 2, 
                                                                   'Highlander AWD': 2, 'ACTIVEHYBRID 7L': 2, 'EXPEDITION EL 4X4': 2, 'Arteon 4MOTION': 2, '328i': 2, 'Camry': 2, 'SILVERADO eASSIST 4WD': 2, 
                                                                   'Highlander Hybrid AWD': 2, 'RAV4 Hybrid AWD': 2, 'IS 200t': 2, 'Prius': 2, 'ILX HYBRID': 2, 'AMG S 65 COUPE': 2, 'GHIBLI SQ4': 2, 'MAZDA6 (SIL)': 2, 
                                                                   'CONTINENTAL GTC': 2, 'AMG CLA 45': 2, 'AMG S 63 COUPE': 2, 'AMG E 63 S 4MATIC': 2, 'A7 QUATTRO TDI (modified)': 2, 'A6 QUATTRO TDI (modified)': 2, 
                                                                   'AMG E 63 S 4MATIC WAGON': 2, 'Sequoia 4WD': 2, 'Sienna': 2, 'Q5 HYBRID': 2, 'CLA 250 4MATIC FFV': 2, 'E 400 4MATIC COUPE': 2, 'HURACAN SPYDER': 2, 
                                                                   'Camry Hybrid XLE/SE': 2, 'Camry Hybrid LE': 2, '4C': 2, 'XJ R-SPORT 3.0 AWD': 2, 'RS 5 CABRIOLET': 2, 'MAYBACH S 600': 2, 'TTS ROADSTER QUATTRO': 2,
                                                                    'Camry XLE/XSE': 2, 'Camry LE/SE': 2, 'F-TYPE S COUPE AWD': 2, 'LANCER 4WD': 2, 'TRAX 4WD': 2, 'S60 CC T5 AWD': 2, 'MALIBU HYBRID': 2, 'A8 QUATTRO': 2, 
                                                                    'MDX SH-AWD ELITE': 2, 'XC40 T5 AWD': 2, 'XC70 T5': 2, 'Wraith': 2, 'CTS SEDAN': 2, 'CTS SEDAN AWD': 2, 'Continental GT': 2, 'Continental GT Convertible': 2,
                                                                     'CTS SPORT WAGON': 2, 'CTS SPORT WAGON AWD': 2, 'CTS-V COUPE': 2, 'S80 T5': 2, 'CTS-V SEDAN': 2, 'CTS-V SPORT WAGON': 2, 'JETTA HYBRID': 2, 'GOLF SPORTWAGON TDI (modified)': 2,
                                                                      'GOLF TDI (modified)': 2, '1500 ECODIESEL HFE': 2, 'PANAMERA TURBO S EXECUTIVE': 2, 'PANAMERA TURBO S': 2, 'MACAN TURBO': 2, 'MACAN S': 2, '370Z COUPE': 2, 
                                                                      'ESCALADE AWD': 2, 'ESCALADE ESV AWD': 2, 'SRX AWD': 2, 'CAMARO 2LS': 2, 'EXPRESS 1500 CARGO AWD': 2, 'EXPRESS 1500 CARGO CONV': 2, 'Tiguan 4MOTION': 2, 
                                                                      'Highlander': 2, 'Tiguan': 2, 'Golf SportWagen': 2, 'A8L QUATTRO': 2, 'Golf R': 2, '228i': 2, 'REGAL eASSIST': 2, 'M235i': 2, 'X1 xDRIVE35i': 2,
                                                                       'S60 POLESTAR': 2, 'S60 INSCRIPTION T5 AWD': 2, 'ALPINA B7 xDRIVE SWB': 2, 'LACROSSE FFV': 2, 'LACROSSE AWD FFV': 2, 'CRUZE PREMIER': 2, 
                                                                       'CRUZE LIMITED ECO': 2, 'IMPALA DUAL FUEL': 2, 'ALPINA B7 xDRIVE LWB': 2, 'RLX': 2, 'Golf Alltrack': 2, 'Passat': 2, 'S5 QUATTRO': 2, 'Jetta': 2, 
                                                                       'Q5 QUATTRO': 2, 'V60 POLESTAR': 2, 'Golf SportWagen 4MOTION': 2, 'S4 QUATTRO': 2, 'ES 350 F SPORT': 1, 'Tacoma 4WD D-Cab TRD Off-Road/Pro': 1,
                                                                        'XE P250 AWD': 1, 'UX 250h': 1, 'XF 30t AWD': 1, 'Atlas Cross Sport 4MOTION': 1, 'F-TYPE P300 Coupe': 1, 'Range Rover Evoque Convertible': 1, 
                                                                        'RAV4 AWD TRD Off-Road': 1, 'Range Rover Velar P380': 1, 'XF S AWD': 1, 'F-TYPE Coupe R-Dynamic AWD': 1, 'Range Rover Sport TD6 Diesel': 1, 
                                                                        'Range Rover Sport Supercharged': 1, 'RX 450h L AWD': 1, 'UX 200': 1, 'Range Rover Velar P300': 1, 'UX 250h AWD': 1, 'XE P300 AWD': 1, 
                                                                        'Range Rover Velar D180': 1, 'Range Rover Evoque': 1, 'F-TYPE SVR AWD Coupe': 1, 'F-TYPE Convertible R-Dynamic AWD': 1, 'Range Rover 5.0 Supercharged LWB': 1,
                                                                         'Highlander Hybrid AWD Limited/Platinum': 1, 'Ghibli S Q4': 1, 'Range Rover Evoque P300': 1, 'Range Rover Velar P250': 1, 'Range Rover Velar P340': 1,
                                                                          'Cullinan Black Badge': 1, 'Range Rover Velar SVAutobiography Dynamic': 1, 'Sorento': 1, 'Aviator': 1, 'Grand Cherokee 4X4 EcoDiesel': 1, 
                                                                          'Grand Cherokee 4X4 SRT': 1, '1500 4X4 EcoDiesel': 1, '1500 EcoDiesel': 1, 'Range Rover SVAutobiography LWB': 1, 'Niro Touring': 1, 
                                                                          'Grand Cherokee 4X4 Trackhawk': 1, 'Niro FE': 1, 'Niro': 1, 'Sentra SR': 1, 'Quattroporte S Q4': 1, 'F-TYPE SVR AWD Convertible': 1, 
                                                                          'Cadenza': 1, 'Renegade 4X4 Trailhawk': 1, 'CX-30 4WD (Cylinder Deactivation)': 1, 'Range Rover Evoque P250': 1, 'Range Rover Sport SVR': 1, 
                                                                          'Range Rover SVAutobiography Dynamic': 1, 'Aventador Roadster': 1, 'XJ R-Sport AWD': 1, 'XJL Portfolio AWD': 1, 'Wrangler 4X4 eTorque': 1, 
                                                                          'GR Supra': 1, 'Corolla Hybrid': 1, 'Corolla XSE': 1, 'Corolla XLE': 1, 'Wrangler Unlimited 4X4 EcoDiesel': 1, 'Range Rover TD6 Diesel': 1,
                                                                           'Camry AWD XLE/XSE': 1, 'Discovery Sport': 1, 'Discovery TD6 Diesel': 1, 'Discovery': 1, 'Telluride AWD': 1, 'Urus': 1, 'Discovery Sport P250': 1,
                                                                            'Discovery Sport P290': 1, 'Camry AWD LE/SE': 1, 'Huracan Performante Spyder': 1, 'Huracan Performante Coupe': 1, 'Camry TRD': 1, 'CX-3 (SIL)': 1, 
                                                                            'Phantom EWB': 1, 'F-TYPE P300 Convertible': 1, '540i xDrive Sedan': 1, 'Titan': 1, 'M8 Cabriolet Competition': 1, 'M8 Cabriolet': 1, 'M760i xDrive Sedan': 1,
                                                                             'M550i xDrive Sedan': 1, 'M5 Sedan': 1, 'M340i xDrive Sedan': 1, '750Li xDrive Sedan': 1, '750i xDrive Sedan': 1, '530i xDrive Sedan': 1, 'X6 M50i': 1, 
                                                                             '430i Coupe': 1, '330i xDrive Sedan': 1, '230i Coupe': 1, '230i Cabriolet': 1, 'Flying Spur': 1, '911 GT2 RS': 1, '911 GT3 RS': 1, 'R8 Spyder': 1, 
                                                                             'R8 Coupe': 1, 'M8 Coupe': 1, 'Rogue AWD': 1, 'Rogue': 1, 'M8 Coupe Competition': 1, 'Eclipse Cross 4WD': 1, 'X5 M50i': 1, 'Altima': 1, 'Altima AWD': 1,
                                                                              'Altima AWD SR/Platinum': 1, 'X4 M Competition': 1, 'X4 M': 1, 'Kicks': 1, 'Maxima': 1, 'X3 M Competition': 1, 'X3 M': 1, 'Murano': 1, 'X2 M35i': 1, 
                                                                              'M850i xDrive Gran Coupe': 1, 'Murano AWD': 1, 'NV200 Cargo Van': 1, 'Pathfinder': 1, 'M8 Gran Coupe Competition': 1, 'M8 Gran Coupe': 1, 'A6 allroad': 1, 
                                                                              'TLX SH-AWD A-SPEC/Limited Edition': 1, '911 GT3 Touring': 1, 'Panamera 4S ST': 1, 'Tacoma': 1, 'Sienna AWD': 1, 'Prius c': 1, 'Prius AWD': 1,
                                                                               'Panamera GTS': 1, 'Panamera GTS ST': 1, 'Panamera Turbo': 1, 'Highlander AWD LE': 1, 'Panamera Turbo Executive': 1, 'Panamera Turbo ST': 1, 
                                                                               'Highlander AWD (Start/Stop System)': 1, 'Corolla LE Eco': 1, '1500 Classic EcoDiesel': 1, 'Camry XSE': 1, 'Avalon': 1, '1500 Classic 4X4 EcoDiesel': 1, 
                                                                               'ProMaster City': 1, 'Forester AWD': 1, 'Ascent AWD': 1, 'Tacoma 4WD D-Cab Off-Road': 1, 'Panamera 4S Executive': 1, '911 Speedster': 1, 'Panamera 4S': 1,
                                                                                'Beetle Dune Convertible': 1, 'Beetle Dune': 1, 'Beetle Convertible': 1, 'Beetle': 1, 'Atlas 4MOTION': 1, 'Atlas': 1, '911 Turbo': 1, 
                                                                                '911 Turbo Cabriolet': 1, '911 Turbo S': 1, '911 Turbo S Cabriolet': 1, '911 Turbo S Exclusive Cabriolet': 1, 'Tundra': 1, 'Cayenne Turbo': 1,
                                                                                 'Macan': 1, 'Macan S': 1, 'Panamera': 1, 'Panamera 4': 1, 'Panamera 4 Executive': 1, 'Panamera 4 ST': 1, 'X6 xDrive40i': 1, 'X7 M50i': 1, 
                                                                                 'F-PACE SVR': 1, 'A 250 4MATIC': 1, 'Grand Caravan': 1, 'Charger SRT Hellcat Widebody': 1, 'Mazda3 4-Door 4WD': 1, 'Charger Widebody (MDS)': 1,
                                                                                  'Mazda3 5-Door 4WD': 1, 'Mazda6 Turbo': 1, 'A 220': 1, 'A 220 4MATIC': 1, 'A 250': 1, 'AMG C 43 4MATIC Cabriolet': 1, 'Z4 sDrive30i': 1, 
                                                                                  'AMG C 43 4MATIC Coupe': 1, 'AMG C 43 4MATIC Wagon': 1, 'AMG C 63 S Cabriolet': 1, 'Challenger AWD': 1, 'AMG C 63 S Coupe': 1, 
                                                                                  'AMG CLS 53 4MATIC+': 1, 'AMG E 53 4MATIC+': 1, 'Voyager (Stop-Start)': 1, 'Phantom': 1, 'Escape Hybrid': 1, 'Escape Hybrid AWD': 1, 
                                                                                  'Mazda3 4-Door (Cylinder Deactivation)': 1, 'Mazda3 4-Door (SIL)': 1, 'F-PACE S': 1, 'F-PACE 30t': 1, 'MKT Livery AWD': 1, 'E-PACE P300': 1,
                                                                                   'Palisade AWD': 1, 'Palisade': 1, 'Insight EX/Touring': 1, 'Sierra WT 4WD': 1, 'Ghibli': 1, 'Ghibli SQ4': 1, 'GranTurismo Convertible': 1, 
                                                                                   'Levante': 1, 'Sierra WT': 1, 'Quattroporte SQ4': 1, 'Quattroporte GTS': 1, 'Shelby GT500 Mustang': 1, 'CX-5 Turbo 4WD': 1, 'CX-5 Diesel 4WD': 1,
                                                                                    'Explorer Hybrid AWD': 1, 'AMG E 53 4MATIC+ Coupe': 1, 'AMG E 53 4MATIC+ Wagon': 1, 'AMG E 63 S 4MATIC+': 1, 'E 450 4MATIC': 1, 'Silverado WT 4WD': 1,
                                                                                     'Silverado WT': 1, 'E 450 4MATIC Coupe': 1, 'E 450 4MATIC Wagon': 1, 'GLC 300 4MATIC Coupe': 1, 'Maybach S 560 4MATIC': 1, 'Maybach S 650': 1, 
                                                                                     'Metris Cargo': 1, 'Metris Cargo LWB': 1, 'Metris Passenger': 1, 'S 560 Cabriolet': 1, 'XT6 AWD': 1, 'CT5-V AWD': 1, 'CT5-V': 1, 'CT4-V AWD': 1, 
                                                                                     'CT4-V': 1, 'Encore GX AWD': 1, 'Encore GX': 1, 'Z4 M40i': 1, 'E 450 4MATIC Cabriolet': 1, 'CLS 450 4MATIC': 1, 'Trax AWD': 1, 
                                                                                     'C 300 4MATIC Wagon': 1, 'AMG E 63 S 4MATIC+ Wagon': 1, 'AMG GLC 43 4MATIC Coupe': 1, 'AMG GLC 63 S 4MATIC+': 1, 'AMG GLC 63 S 4MATIC+ Coupe': 1,
                                                                                      'AMG GLE 43 4MATIC Coupe': 1, 'AMG GLE 63 S 4MATIC Coupe': 1, 'AMG GT 53 4MATIC+ Coupe': 1, 'AMG GT 63 4MATIC+ Coupe': 1,
                                                                                       'AMG GT 63 S 4MATIC+ Coupe': 1, 'AMG GT C Coupe': 1, 'AMG GT C Roadster': 1, 'AMG GT R Coupe': 1, 'AMG S 63 4MATIC+': 1, 
                                                                                       'AMG S 63 4MATIC+ Cabriolet': 1, 'AMG S 63 4MATIC+ Coupe': 1, 'AMG S 65 Cabriolet': 1, 'AMG S 65 Coupe': 1, 'C 300 4MATIC Cabriolet': 1, 
                                                                                       'C 300 4MATIC Coupe': 1, 'AMG E 53 4MATIC+ Cabriolet': 1, 'C 450 AMG SPORT 4MATIC': 1, 'E-PACE P250': 1, 'Q50S AWD': 1, 'S8 QUATTRO': 1, 
                                                                                       'SQ5 QUATTRO': 1, '228i xDRIVE': 1, 'M235i xDRIVE': 1, 'M235i xDRIVE CABRIOLET': 1, 'ENCORE SPORT TOURING': 1, 'ENCORE SPORT TOURING AWD': 1, 
                                                                                       'MALIBU LIMITED': 1, 'VIPER SRT': 1, 'TRANSIT CONNECT WAGON LWB': 1, 'ACCORD SPORT': 1, 'Q50S RED SPORT': 1, 'S6 QUATTRO': 1, 
                                                                                       'F-TYPE PROJECT 7 CONVERTIBLE': 1, 'XF AWD ': 1, 'XJL 3.0 AWD PORTFOLIO': 1, 'SOUL ECO DYNAMICS': 1, 'RANGE ROVER TD6 DIESEL': 1, 
                                                                                       'RANGE ROVER SPORT TD6 DIESEL': 1, 'GS 200t': 1, 'GS 200t F SPORT': 1, 'GS 350 F SPORT': 1, 'GS F': 1, 'RC 200t': 1, 'S7 QUATTRO': 1,
                                                                                        'S5 CABRIOLET QUATTRO': 1, 'Q60 AWD Red Sport': 1, 'S80 T6 AWD': 1, 'CLA 45 AMG': 1, 'GLA 45 AMG 4MATIC': 1, 'ML 400 4MATIC': 1, 
                                                                                        'S 400 4MATIC': 1, 'S 63 AMG COUPE': 1, 'S 65 AMG': 1, 'S 65 AMG COUPE': 1, 'SLS AMG GT ROADSTER': 1, 'S60 POLESTAR AWD': 1, 'S60 T5 ': 1, 
                                                                                        'S60 T6   ': 1, 'V60 CC': 1, 'S3 QUATTRO': 1, 'V60 CC AWD': 1, 'V60 POLESTAR AWD': 1, 'XC60 3.2 AWD': 1, 'XC60 T6  ': 1, 'XC70 3.2 AWD': 1, 
                                                                                        'XC70 T6 AWD': 1, 'DB9 GT': 1, 'A8 QUATTRO TDI (modified)': 1, 'Q5 QUATTRO TDI (modified)': 1, 'Q5 HYBRID QUATTRO': 1, 'RS 7 QUATTRO': 1, 'CX-5 (SIL)': 1,
                                                                                         'AMG CLS 63 S 4MATIC': 1, 'AMG GL 63 S': 1, 'ENCORE AWD (LE2 Engine)': 1, 'GIULIA QUADRIFOGLIO': 1, 'DB11 V12': 1, 'A4 ULTRA': 1, 'BENTAYGA': 1, 'MULSANNE EWB': 1,
                                                                                          '230i CABRIOLET': 1, 'ALPINA B7 xDRIVE': 1, 'M760i xDRIVE': 1, 'ENCORE (LUV Engine)': 1, 'ENCORE (LE2 Engine)': 1, 'ENCORE AWD (LUV Engine)': 1, 
                                                                                          'PACIFICA (Stop-Start)': 1, 'AMG GLA 45': 1, 'CHALLENGER GT': 1, 'VIPER': 1, 'IONIQ BLUE': 1, 'Q60S RED SPORT AWD': 1, 'QX30': 1, 'QX30 AWD': 1, 'F-PACE 35t': 1,
                                                                                          'F-TYPE R CONVERTIBLE AWD': 1, 'F-TYPE R COUPE AWD': 1, 'XE 20d AWD': 1, 'XE 35t AWD': 1, 'GIULIA AWD': 1, 'GIULIA': 1, '4C SPIDER': 1, 'NSX': 1, 
                                                                                          'AMG GLE 63 S COUPE 4MATIC': 1, 'AMG GT S': 1, 'AMG S 63': 1, 'AMG SLK 55': 1, 'GLE 350d 4MATIC': 1, 'GLE 350d 4MATIC COUPE': 1, 
                                                                                          'GLE 450 AMG SPORT 4MATIC COUPE': 1, 'S 400 4MATIC SWB': 1, 'SLK 300': 1, 'ALTIMA 3.5': 1, '911 GT3RS': 1, 'BOXSTER SPYDER': 1, 'CAYMAN GT4': 1, 
                                                                                          'TACOMA 4WD D-CAB OFF-ROAD': 1, 'S60 INSCRIPTION': 1, 'S60 T6': 1, 'S60 3.0T AWD': 1, 'V60 3.0T AWD': 1, 'XC60 T6': 1, 'XC60 3.0T AWD': 1, 'XC70 T5 AWD': 1, 
                                                                                          'XC90 T5': 1, 'MDX HYBRID AWD': 1, 'C 400 4MATIC': 1, 'VENENO ROADSTER': 1, 'XF AWD': 1, 'IS 250 AWD': 1, 'XF 3.0L AWD': 1, 'XJ AWD': 1, 'XK CONVERTIBLE': 1, 
                                                                                          'XK COUPE': 1, 'GRAND CHEROKEE 4X4 DIESEL': 1, 'LR2': 1, 'RANGE ROVER LWB V8 5.0 SC': 1, 'RANGE ROVER SPORT V6 3.0 SC': 1, 'RANGE ROVER SPORT V8 5.0 SC': 1, 
                                                                                          'RANGE ROVER V6 3.0 SC': 1, 'RANGE ROVER V8 5.0 SC': 1, 'IS F': 1, 'E 350 4MATIC WAGON': 1, 'C 250': 1, 'C 350': 1, 'C 350 4MATIC': 1, 'C 350 4MATIC COUPE': 1,
                                                                                           'C 350 COUPE': 1, 'C 63 AMG': 1, 'CL 550 4MATIC': 1, 'CL 63 AMG': 1, 'CLA 45 AMG 4MATIC': 1, 'CLS 63 AMG S 4MATIC': 1, 'E 350 4MATIC': 1, 'XF': 1, 
                                                                                           'F-TYPE V8 S CONVERTIBLE': 1, 'Q60 AWD COUPE': 1, 'SANTA FE 4WD': 1, 'MDX 4WD': 1, 'TL': 1, 'DB9': 1, 'RAPIDE': 1, 'A8 TDI (modified)': 1, 'A8L TDI (modified)': 1,
                                                                                            'ALLROAD QUATTRO': 1, 'Q5 TDI (modified)': 1, 'Q7 TDI (modified)': 1, 'CONTINENTAL GT SPEED CONVERTIBLE': 1, '528i': 1, '760Li': 1, 'CTS COUPE': 1, 
                                                                                            'CTS COUPE AWD': 1, 'CTS SEDAN Vsport': 1, 'IMPALA ECO': 1, '300 AWD (MDS)': 1, '300 SRT (MDS)': 1, '500 CABRIO TURBO': 1, 'E350 WAGON': 1, 
                                                                                            'TRANSIT CONNECT TAXI': 1, 'CROSSTOUR AWD': 1, 'GENESIS': 1, 'E 350 4MATIC COUPE': 1, 'E 350 CABRIOLET': 1, 'F-TYPE V8 R COUPE': 1, '750Li xDRIVE SEDAN': 1, 
                                                                                            '328d xDRIVE SEDAN': 1, '328i xDRIVE SEDAN': 1, '435i GRAN COUPE': 1, '528i SEDAN': 1, '528i xDRIVE SEDAN': 1, '535d xDRIVE SEDAN': 1, '535i xDRIVE SEDAN': 1, 
                                                                                            '550i xDRIVE SEDAN': 1, '740Ld xDRIVE SEDAN': 1, '740Li xDRIVE SEDAN': 1, '750i xDRIVE SEDAN': 1, '760Li SEDAN': 1, 'E 350 COUPE': 1, 'M235i xDRIVE COUPE': 1, 
                                                                                            'CAMARO Z/28': 1, '200 AWD': 1, 'CHARGER SRT 392 HEMI': 1, 'VIPER SRT COUPE': 1, 'EDGE SPORT AWD': 1, 'EXPLORER AWD (EcoBoost)': 1, 
                                                                                            'TRANSIT CONNECT WAGON TAXI': 1, 'CIVIC Si': 1, 'CIVIC HYBRID': 1, 'PILOT 4WD': 1, '320i xDRIVE SEDAN': 1, '228i xDRIVE COUPE': 1, 
                                                                                            '228i CABRIOLET': 1, 'CONTINENTAL GT3-R': 1, 'E 400 HYBRID': 1, 'E 63 AMG 4MATIC': 1, 'E 63 AMG 4MATIC WAGON': 1, 'ML 350 BLUETEC 4MATIC': 1, 
                                                                                            'SLS AMG BLACK SERIES COUPE': 1, 'SLS AMG ROADSTER': 1, 'LANCER RALLIART': 1, 'PATHFINDER HYBRID 4WD': 1, 'CAYENNE S HYBRID': 1, '1500 4X4 DIESEL': 1, 
                                                                                            '1500 DIESEL': 1, 'VIPER COUPE': 1, 'VIPER GTS COUPE': 1, 'TRIBECA AWD': 1, '4RUNNER (Part-Time 4WD)': 1, 'JETTA TURBO HYBRID': 1, 'ROUTAN': 1, 'S60': 1,
                                                                                             'S80': 1, 'S80 AWD': 1, 'XC60': 1, 'XC90 AWD': 1, 'A3 TDI (modified)': 1, 'XF 20d AWD': 1, 'XF 35t AWD': 1, 'XJL PORTFOLIO 3.0 AWD': 1, 'M6 Gran Coupe': 1, 
                                                                                             '330i xDrive Touring': 1, '430i xDrive Cabriolet': 1, '530i xDrive': 1, '540i xDrive': 1, '640i xDrive Gran Coupe': 1, '640i xDrive Gran Turismo': 1, 
                                                                                             '650i xDrive Gran Coupe': 1, '750i xDrive': 1, '750Li xDrive': 1, 'Alpina B6 xDrive Gran Coupe': 1, 'M550i xDrive': 1, 'M760Li xDrive': 1, 'XT4': 1,
                                                                                              'X5 xDrive40i': 1, 'X6 xDrive35i': 1, 'X6 xDrive50i': 1, 'X7 xDrive40i': 1, 'Chiron': 1, 'Enclave': 1, 'Encore': 1, 'Encore (SIDI with Stop/Start)': 1, 
                                                                                              'Encore AWD (SIDI with Stop/Start)': 1, 'LaCrosse': 1, 'LaCrosse eAssist': 1, '330i xDrive Gran Turismo': 1, '330i xDrive': 1, 'Mulsanne': 1, 
                                                                                              'TTS Coupe': 1, 'CAMRY XLE/XSE': 1, 'CAMRY XSE': 1, 'ATLAS': 1, 'ATLAS 4MOTION': 1, 'BEETLE DUNE CONVERTIBLE': 1, 'V90 CC T5 AWD': 1, 'MDX SH-AWD A-SPEC': 1, 
                                                                                              'MDX Hybrid AWD': 1, 'RLX Hybrid': 1, '4C Coupe': 1, '4C Spider': 1, 'Giulia': 1, 'Giulia AWD': 1, 'Stelvio': 1, 'Stelvio AWD': 1, 'DB11 AMR': 1, 
                                                                                              'DBS Superleggera': 1, 'Rapide AMR': 1, 'Vanquish Zagato': 1, 'Q3 quattro': 1, 'RS 5 Coupe': 1, 'RS 5 Sportback': 1, 'TT RS Coupe': 1, 'LaCrosse AWD': 1,
                                                                                               'XT4 AWD': 1, 'WRX STI AWD TYPE RA': 1, 'Insight Touring': 1, 'Fiesta ST': 1, 'Ranger 4WD': 1, 'Taurus AWD': 1, 'G70': 1, 'Sierra LTD': 1, 
                                                                                               'Sierra LTD 4WD': 1, 'Yukon': 1, 'Yukon XL': 1, 'Accord Sport/Touring': 1, 'Accord Hybrid': 1, 'Insight EX': 1, 'Odyssey Touring': 1, 'Cruze': 1, 
                                                                                               'Pilot': 1, 'IONIQ Blue': 1, 'Santa Fe': 1, 'Santa Fe XL': 1, 'Santa Fe XL AWD': 1, 'Santa Fe XL Ultimate AWD': 1, 'Sonata SE': 1, 'Sonata Hybrid SE': 1, 
                                                                                               'Tucson': 1, 'Veloster N': 1, 'Q50 AWD Red Sport': 1, 'Flex AWD GTDI': 1, 'Flex AWD': 1, 'Flex': 1, 'F-150 Raptor 4X4': 1, 'Cruze Premier': 1, 
                                                                                               'Cruze Diesel': 1, 'Cruze Hatchback': 1, 'Cruze Hatchback Premier': 1, 'Cruze Hatchback Diesel': 1, 'Malibu Hybrid': 1, 'Silverado LD': 1, 
                                                                                               'Silverado LD 4WD': 1, 'Suburban': 1, 'Tahoe': 1, 'Traverse': 1, 'Trax 4WD': 1, 'Pacifica': 1, 'Pacifica (Stop-Start)': 1, 'Challenger GT AWD': 1, 
                                                                                               'Challenger SRT Hellcat Redeye': 1, 'Charger AWD': 1, 'Charger AWD (MDS)': 1, 'Charger SRT Hellcat': 1, 'Durango AWD SRT': 1, 'Journey': 1,
                                                                                                'Journey AWD': 1, 'F-150 4X4 Limited': 1, 'CAMRY LE/SE': 1, 'BRZ tS': 1, 'XJR  LWB': 1, 'X3 xDRIVE30i': 1, 'STELVIO QUADRIFOGLIO': 1, 'DB11 V8': 1,
                                                                                                 'A5 SPORTBACK QUATTRO': 1, 'R8 QUATTRO': 1, 'S5 SPORTBACK': 1, 'TTS COUPE': 1, 'CONTINENTAL SUPERSPORTS': 1, '640i xDRIVE GRAN TURISMO': 1, 
                                                                                                 '750i xDRIVE SWB': 1, 'M550i xDRIVE': 1, 'X2 xDRIVE28i': 1, 'CHIRON': 1, 'CIVIC SEDAN Si': 1, 'ENCORE (SIDI with Stop/Start)': 1,
                                                                                                  'ENCORE AWD (SIDI with Stop/Start)': 1, 'SILVERADO eASSIST': 1, 'CHALLENGER GT AWD': 1, 'CHALLENGER SRT DEMON': 1, 'DURANGO AWD SRT': 1, 
                                                                                                  'ECOSPORT': 1, 'ECOSPORT AWD': 1, 'F-150 RAPTOR 4WD': 1, 'SIERRA eASSIST': 1, 'ACCORD SPORT/TOURING': 1, 'STELVIO AWD': 1, '4C COUPE': 1, 
                                                                                                  'TLX SH-AWD A-SPEC': 1, 'TLX A-SPEC': 1, 'GRAND CHEROKEE SRT8': 1, 'FORTE (GDI)': 1, 'NIRO': 1, 'NIRO FE': 1, 'NIRO TOURING': 1, 'OPTIMA FE': 1,
                                                                                                   'OPTIMA TURBO': 1, 'SORENTO AWD FE': 1, 'SOUL TURBO': 1, 'AVENTADOR COUPE LP 740': 1, 'AVENTADOR ROADSTER LP 740': 1, 'AMG GLS 63': 1,
                                                                                                    'AMG S 63 CABRIOLET': 1, 'AMG S 65 CABRIOLET': 1, 'S 550 4MATIC CABRIOLET': 1, 'CAYENNE PLATINUM': 1, 'MACAN': 1, 'MACAN GTS': 1, 
                                                                                                    'HIGHLANDER AWD (Start/Stop System)': 1, 'HIGHLANDER AWD LE': 1, 'S60 INSCRIPTION T5': 1, 'S90 T5': 1, 'V90 T5': 1, 'CIVIC COUPE Si': 1,
                                                                                                     'CIVIC TYPE R': 1, 'PANAMERA TURBO ST': 1, 'GLC 300 4MATIC COUPE': 1, 'AMG C 43 4MATIC CABRIOLET': 1, 'AMG C 43 4MATIC COUPE': 1, 
                                                                                                     'AMG E 43 4MATIC': 1, 'AMG GT ROADSTER': 1, 'AMG GT C COUPE': 1, 'AMG GT C ROADSTER': 1, 'AMG GT R COUPE': 1, 'AMG S 63 4MATIC CABRIOLET': 1,
                                                                                                      'AMG S 63 4MATIC COUPE': 1, 'C 300 4MATIC WAGON': 1, 'E 400 4MATIC CABRIOLET': 1, 'MAYBACH S 650': 1, 'ODYSSEY TOURING': 1, 'S 560 CABRIOLET': 1, 
                                                                                                      'S 560 4MATIC': 1, 'S 560 4MATIC COUPE': 1, 'ECLIPSE CROSS': 1, 'ECLIPSE CROSS 4WD': 1, 'KICKS': 1, '911 TURBO S EXCLUSIVE': 1, 'MACAN TURBO KIT': 1, 
                                                                                                      'PANAMERA 4 EXECUTIVE': 1, 'PANAMERA 4 ST': 1, 'PANAMERA 4S ST': 1, 'MAZDA6 TURBO': 1, 'CX-5 4WD (Cylinder Deactivation)': 1, 
                                                                                                      'CX-5 (Cylinder Deactivation)': 1, 'CX-5 ': 1, 'KONA': 1, 'SANTA FE SPORT ULTIMATE AWD': 1, 'Q50 AWD RED SPORT': 1, 'Q60 AWD RED SPORT': 1, 
                                                                                                      'F-PACE 20d': 1, 'F-PACE 25t': 1, 'F-TYPE CONVERTIBLE R-DYNAMIC AWD': 1, 'F-TYPE COUPE R-DYNAMIC AWD': 1, 'XE 25t AWD': 1, 'XF 25t AWD': 1, 'XJ R-SPORT AWD': 1, 
                                                                                        'XJL PORTFOLIO AWD': 1, 'GRAND CHEROKEE 4X4 SRT': 1, 'GRAND CHEROKEE 4X4 TRACKHAWK': 1, 'STINGER AWD': 1, 'AVENTADOR S COUPE': 1, 'AVENTADOR S ROADSTER': 1, 
                                                           'HURACAN AWD': 1, 'HURACAN SPYDER AWD': 1, 'LS 500': 1, 'LS 500h': 1, 'NX 300 AWD F SPORT': 1, 
                                                           'RX 350 L AWD': 1, 'XC40 T4 AWD': 1}

Vehicle= {'SUV - SMALL': 1006, 'MID-SIZE': 983, 'COMPACT': 903, 'SUV - STANDARD': 613, 'SUBCOMPACT': 533, 'FULL-SIZE': 508, 'PICKUP TRUCK - STANDARD': 475, 'TWO-SEATER': 381, 'MINICOMPACT': 274, 'STATION WAGON - SMALL': 214, 
            'PICKUP TRUCK - SMALL': 133, 'VAN - PASSENGER': 66, 'SPECIAL PURPOSE VEHICLE': 65, 'MINIVAN': 61, 'STATION WAGON - MID-SIZE': 45, 'VAN - CARGO': 22}



selected_make = st.selectbox('Pilih Merek Mobil:', list(make_to_code.keys()))
selected_model=st.selectbox('Pilih Model Mobil:', list(car_models.keys()))
selected_vehicle=st.selectbox('Pilih Model Mobil:', list(Vehicle.keys()))

# Menentukan langkah (step) untuk input cylinders
cylinders = st.number_input('Masukkan Nilai Cylinder:', min_value=1.0, max_value=12.0, step=0.1, value=4.0)

# Menentukan langkah (step) untuk input Fuel Consumption Comb (mpg)
mpg = st.number_input('Masukkan Nilai mpg:', min_value=1.0, max_value=12.0, step=0.1, value=4.0)


# Dummy variables yang sudah ada dari model
selected_fuel_dummy ={'Ethanol': {'Fuel_Ethanol': 1, 'Fuel_Regular gasoline': 0},
    'Regular gasoline': {'Fuel_Ethanol': 0, 'Fuel_Regular gasoline': 1}}
selected_fuel = 'Ethanol' if selected_fuel_dummy['Ethanol']['Fuel_Ethanol'] else 'Regular gasoline'


# Tampilkan radio button untuk memilih jenis bahan bakar
selected_fuel = st.radio('Pilih Jenis Bahan Bakar:', list(selected_fuel_dummy.keys()))




# Dummy variables transmisi
transmission_dummy = {
    'Automatic': {'Automatic': True, 'Automatic of Selective type': False, 'CVT': False, 'Manual': False},
    'Automatic of Selective type': {'Automatic': False, 'Automatic of Selective type': True, 'CVT': False, 'Manual': False},
    'CVT': {'Automatic': False, 'Automatic of Selective type': False, 'CVT': True, 'Manual': False},
    'Manual': {'Automatic': False, 'Automatic of Selective type': False, 'CVT': False, 'Manual': True}
}
selected_transmission = 'Automatic'

# Tampilkan radio button untuk memilih jenis transmisi
selected_transmission = st.radio('Pilih Jenis Transmisi:', list(transmission_dummy.keys()))






# Convert selections to numeric codes
make_code = make_to_code[selected_make]
model_code = car_models[selected_model]
vehicle_code = Vehicle[selected_vehicle]

# Convert fuel and transmission selections to dummy variables
fuel_data = selected_fuel_dummy.get(selected_fuel, {'Fuel_Ethanol': 0, 'Fuel_Regular gasoline': 0})
transmission_data = transmission_dummy.get(selected_transmission, {'Transmission_Automatic': 0, 'Transmission_Automatic of Selective type': 0, 'Transmission_CVT': 0, 'Transmission_Manual': 0})
# Combine all inputs into one array

input_data = [
    make_code, model_code, vehicle_code, cylinders,mpg,
    fuel_data['Fuel_Ethanol'], fuel_data['Fuel_Regular gasoline'],
    transmission_data.get('Automatic', 0),
    transmission_data.get('Automatic of Selective type', 0),
    transmission_data.get('CVT', 0),
    transmission_data.get('Manual', 0)
]

# Ensure input_data is a 2D array for the model
input_data = [input_data]


# Display prediction

predict= ''

if st.button('Estimasi Emisi yang dikeluarkan Mobil'):
    predict=model.predict(input_data)

st.write ('Estimasi Emisi yaitu :', predict)