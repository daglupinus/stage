#  0  ##gff-version 3.2.1
#  1  ##sequence-region   ctg123 1 1497228       
#  2  ctg123 . gene            1000  9000  .  +  .  ID=gene00001;Name=EDEN

#  3  ctg123 . TF_binding_site 1000  1012  .  +  .  ID=tfbs00001;Parent=gene00001

#  4  ctg123 . mRNA            1050  9000  .  +  .  ID=mRNA00001;Parent=gene00001;Name=EDEN.1
#  5  ctg123 . mRNA            1050  9000  .  +  .  ID=mRNA00002;Parent=gene00001;Name=EDEN.2
#  6  ctg123 . mRNA            1300  9000  .  +  .  ID=mRNA00003;Parent=gene00001;Name=EDEN.3

#  7  ctg123 . exon            1300  1500  .  +  .  ID=exon00001;Parent=mRNA00003
#  8  ctg123 . exon            1050  1500  .  +  .  ID=exon00002;Parent=mRNA00001,mRNA00002
#  9  ctg123 . exon            3000  3902  .  +  .  ID=exon00003;Parent=mRNA00001,mRNA00003
# 10  ctg123 . exon            5000  5500  .  +  .  ID=exon00004;Parent=mRNA00001,mRNA00002,mRNA00003
# 11  ctg123 . exon            7000  9000  .  +  .  ID=exon00005;Parent=mRNA00001,mRNA00002,mRNA00003

# 12  ctg123 . CDS             1201  1500  .  +  0  ID=cds00001;Parent=mRNA00001;Name=edenprotein.1
# 13  ctg123 . CDS             3000  3902  .  +  0  ID=cds00001;Parent=mRNA00001;Name=edenprotein.1
# 14  ctg123 . CDS             5000  5500  .  +  0  ID=cds00001;Parent=mRNA00001;Name=edenprotein.1
# 15  ctg123 . CDS             7000  7600  .  +  0  ID=cds00001;Parent=mRNA00001;Name=edenprotein.1

# 16  ctg123 . CDS             1201  1500  .  +  0  ID=cds00002;Parent=mRNA00002;Name=edenprotein.2
# 17  ctg123 . CDS             5000  5500  .  +  0  ID=cds00002;Parent=mRNA00002;Name=edenprotein.2
# 18  ctg123 . CDS         7000  7600     .  +  0  ID=cds00002;Parent=mRNA00002;Name=edenprotein.2

# 19  ctg123 . CDS             3301  3902  .  +  0  ID=cds00003;Parent=mRNA00003;Name=edenprotein.3
# 20  ctg123 . CDS         5000  5500     .  +  1  ID=cds00003;Parent=mRNA00003;Name=edenprotein.3
# 21  ctg123 . CDS         7000  7600     .  +  1  ID=cds00003;Parent=mRNA00003;Name=edenprotein.3

# 22  ctg123 . CDS             3391  3902  .  +  0  ID=cds00004;Parent=mRNA00003;Name=edenprotein.4
# 23  ctg123 . CDS         5000  5500     .  +  1  ID=cds00004;Parent=mRNA00003;Name=edenprotein.4
# 24  ctg123 . CDS         7000  7600     .  +  1  ID=cds00004;Parent=mRNA00003;Name=edenprotein.4

# KROTKA:
# * uporządkowana (tzn. pamieta w jakiej kolejności dane trzyma) (1, 2, 7)
# * niemodyfikowalne (tzn. nie pozwala "zmienić" żadnego elementu)

import gzip
from urllib.parse import unquote
# # http://stackoverflow.com/a/8628164

class GFFRecord:
    """http://www.ensembl.org/info/website/upload/gff.html"""
    FIELD_COUNT = 9 
    
    def __init__(seqid, source, type, start, end, score, strand, phase, attributes):
        self.seqid = seqid
        self.source = source
        self.type = type
        self.start = start
        self.end = end
        self.score = score
        self.strand = strand
        self.phase = phase
        self.attributes = attributes

        
def parse_gff_attributes(attribute_string):
    """Przekształca atrybuty: ID=cds00004;Parent=mRNA00003;Name=edenprotein.4 na słownik"""
    if attributeString == ".": 
        return {}
    result = {}
    for attribute in attribute_string.split(";"):
        key, value = attribute.split("=")
        # unquote przeksztalca wartosci z zapisu np. %20 na przyjazny tekst
        # dzieje sie dlatego, poniewaz format dokumenty chyba nie chcial zawierac bialych znakow (np. spacji)
        result[unquote(key)] = unquote(value)
    return result

def parse_gff3(filename):
    if filename.endswith(".gz"):
        open_func = gzip.open 
    else:
        open_func = open  # ta funkcja jest wbudowana i sluzy do otwierania plikow
    
    with open_func(filename) as document:
        # czytamy troche wolniej, ale wszystko sie zmiesci w pamieci
        # UWAGA: czytajac w ten sposob zawsze dokleja sie nam znak nowej linii \0
        # i warto go usunac przy uzyciu strip.
        for line in document:  
            # pomijamy komentarze
            if line.startswith("#"): 
                continue
                
            parts = line.strip().split("\t")
            # jesli tu jest blad to znaczy, z split trzeba usunac "\t"
            assert len(parts) == len(GFFRecord.FIELD_COUNT)
            #Normalize data
            normalizedInfo = {
                "seqid": None if parts[0] == "." else unquote(parts[0]),
                "source": None if parts[1] == "." else unquote(parts[1]),
                "type": None if parts[2] == "." else unquote(parts[2]),
                "start": None if parts[3] == "." else int(parts[3]),
                "end": None if parts[4] == "." else int(parts[4]),
                "score": None if parts[5] == "." else float(parts[5]),
                "strand": None if parts[6] == "." else unquote(parts[6]),
                "phase": None if parts[7] == "." else unquote(parts[7]),
                "attributes": parse_gff_attributes(parts[8])
            }
            #Alternatively, you can emit the dictionary here, if you need mutability:
            #    yield normalizedInfo
            yield GFFRecord(**normalizedInfo)
            
    
            
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="The GFF3 input file (.gz allowed)")
    parser.add_argument("--print-records", action="store_true", help="Print all GeneInfo objects, not only")
    parser.add_argument("--filter-type", help="Ignore records not having the given type")
    args = parser.parse_args()
    #Execute the parser
    record_count = 0
    for record in parseGFF3(args.file):
        #Apply filter, if any
        if args.filter_type and record.type != args.filter_type:
            continue
        #Print record if specified by the user
        if args.print_records: 
            print(record)  # warto podkreslic jakie pola chcemy wyswietlac np. record.type
        #Access attributes like this: my_strand = record.strand
        record_count += 1
    print("Total records: %d" % record_count)




# ŚCIAGA:
# values = [9, 0, 10, 10, 10, 4, 5]

# if values[0] % 2 == 0:
#     func = min
# else:
#     func = max
    
# print(func(values))


# Instrukcja with sama uruchomi procedure wyjscia na open (czyli zamknie dokument jesli pojawi sie blad)
#     document = open('/home/pk/pulpit/dane.txt')
#     ....
#     mamy blad 
#     ....
#     document.close()
    


# class Point:
    
#     def __init__(x, y):
#         self.x = x
#         self.y = y
        
# data = {'x': 1, 'y': 3}
# point = Point(x=data['x'], y=data['y'])
# point2 = Point(**data)