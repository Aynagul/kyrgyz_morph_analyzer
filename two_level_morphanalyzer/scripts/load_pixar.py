from analyzer.models import AllRoot,Tags,PartOfSpeech
import csv

def run():
    with open('all.csv', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        # AllRoot.objects.all().delete()
        # Tags.objects.all().delete()
        # PartOf.objects.all().delete()
        # next(reader)  # Advance past the header
        for row in reader:
            print(row)
            # partof, _ = PartOf.objects.get_or_create(name=row[1])
            try:
                partof = PartOfSpeech.objects.get(part_of_speech=row[1])
            except PartOfSpeech.DoesNotExist:
                print("part of speech not found")
                partof = None
            tag_objs = []
            for tags in row[2:]:
                if (tags==''):
                    break
                # tag_obj, created = Tags.objects.get_or_create(name=tag.strip())
                # tag_objs.append(tag_obj)
                try:
                    tag_obj = Tags.objects.get(tag=tags.strip())
                except Tags.DoesNotExist:
                    print("tags not found")
                    tag_obj = None
                if tag_obj:
                    tag_objs.append(tag_obj)
            if partof:
                allroot, created = AllRoot.objects.get_or_create(root=row[0].lower(), part_of_speech=partof)
                # Add the Tag objects to the AllRoot's tag field
                if created:
                    allroot.tag.add(*tag_objs)


















            # # Split genres by semicolon and remove leading/trailing spaces
            # genre_names = [genre.strip() for genre in row[1].split(";")]
            
            # # Get or create all genres for the current film
            # genres = [Genre.objects.get_or_create(name=genre_name)[0]
            #           for genre_name in genre_names]
            
            # # Create the film object and add all genres to it
            # film = Film.objects.create(title=row[0], length=1, year=2)
            # film.genre.set(genres)
