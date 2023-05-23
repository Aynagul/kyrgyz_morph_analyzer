from analyzer.models import Tags
import csv

def run():
    with open('tags.csv', encoding='utf-8') as file:
        reader  = csv.reader(file, delimiter=';')
        # Tags.objects.all().delete()
        # next(reader)  # Advance past the header
        for i in range(6):
            for row in reader:
                print(row)
                if(row[1]==i+1):
                    tag_obj, created = Tags.objects.get_or_create(tag=row[0],priority=i+1,description=row[2])
                    tag_obj.save()
