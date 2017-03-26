import fresh_tomatoes
import media

# TIP: In order to print a specific storyline type in command: print(nine9.storyline) and press F5.
# You can also watch specific movie trailer by using command: nine9.show_trailer()


nine9 = media.Movie('9',
                'A rag doll that awakens in a postapocalyptic future holds the key to humanity\'s salvation.',
                'https://upload.wikimedia.org/wikipedia/en/c/c9/9posterfinal.jpg',
                'https://www.youtube.com/watch?v=_qApXdc1WPY')


enders_game = media.Movie('Ender\'s Game',
                          'Young Ender Wiggin is recruited by the International Military to lead the fight against the Formics, a genocidal alien race which nearly annihilated the human race in a previous invasion.',
                          'https://upload.wikimedia.org/wikipedia/en/8/8c/Ender%27s_Game_poster.jpg',
                          'https://www.youtube.com/watch?v=2UNWLgY-wuo')


transporter2 = media.Movie('Transporter 2',
                'Mercenary Frank Martin is pretty good at driving a car.',
                'https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ5MDM0MTI2N15BMl5BanBnXkFtZTcwNTM5NDczMw@@._V1_SY1000_CR0,0,666,1000_AL_.jpg',
                'https://www.youtube.com/watch?v=_qApXdc1WPY')


resident_evil = media.Movie('Resident Evil',
                'A special military unit fights a powerful, out-of-control supercomputer and hundreds of scientists who have mutated into flesh-eating creatures after a laboratory accident.',
                'https://images-na.ssl-images-amazon.com/images/M/MV5BMTI5NzQ3OTI1NF5BMl5BanBnXkFtZTYwMDgyNTk5._V1_.jpg',
                'https://www.youtube.com/watch?v=qjRtay--vwg')


hunger_games = media.Movie('The Hunger Games',
                'Katniss Everdeen has never been so hungry, she even ate her sister\'s food.',
                'https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg',
                'https://www.youtube.com/watch?v=mfmrPu43DF8')


kungfu_panda = media.Movie('Kung Fu Panda',
                'Dragon Warrior mantle is supposedly mistaken to be bestowed upon an obese panda who is a tyro in martial arts.',
                'https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg',
                'https://www.youtube.com/watch?v=PXi3Mv6KMzY')


movies = [nine9, enders_game, transporter2, resident_evil, hunger_games, kungfu_panda]
fresh_tomatoes.open_movies_page(movies)


