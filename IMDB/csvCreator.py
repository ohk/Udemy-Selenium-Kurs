import csv
class csvCretor:
    def csvCreate(self):
        with open('imdbtop250.csv', mode='a') as csv_file:
            fieldnames = ['movie_name', 'movie_description', 'movie_link']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            csv_file.close()

    def csvWriteRow(self,movie_name,movie_description,movie_link):
        with open('imdbtop250.csv', mode='a') as csv_file:
            fieldnames = ['movie_name', 'movie_description', 'movie_link']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'movie_name': movie_name, 'movie_description': movie_description, 'movie_link': movie_link})
            csv_file.close()
