from manim import *
from get_player_data import *

my_player = get_player_data("https://www.baseball-reference.com/players/b/brantmi02.shtml")
teams = list(my_player.teams.keys())
years = list(my_player.teams.values())

print("Run")


class Matike(Scene):
    def construct(self):

        self.camera.background_color = GREY_A

        black_rectangle = Rectangle(width=20, height=15, fill_color=BLACK, fill_opacity=1)

        title = Text(f"GUESS THE MLB PLAYER", font_size=40, color=WHITE, font="Open Sans", weight=BOLD).move_to((0,3.5,0))
        career_text = Text(f"Career Stats", font_size=30, color=GRAY_D, font="Open Sans", weight=BOLD).move_to((-5.5, -2.5, 0))

        top_bio = Rectangle(width=20, height=2, stroke_width=0, fill_color="#4267B2", fill_opacity=1).move_to((0,4,0))
        bottom_bio = Rectangle(width=20, height=2.5, stroke_width=0, fill_color=GREY_C, fill_opacity=1).move_to((0,-4,0))
        profile_pic = ImageMobject("manim_images/profile.png").scale(1).shift((-5,1,0))

        bullets = ["POSITION:","BATS:","THROWS:","BIRTHPLACE:"]
        values = [my_player.positions,my_player.bats,my_player.throws,my_player.birth_place]

        self.add(top_bio, title)

        bio_information = VGroup()

        for index, item in enumerate(bullets):
            line = VGroup()

            temp_answer = values[index]

            bullet = Circle(radius=0.1, fill_color=GRAY_D, fill_opacity=1, stroke_width=0)
            text = Text(f"{item}", font_size=32, color="#4267B2", font="Open Sans", weight=BOLD)

            if len(temp_answer) > 28 and item == "BIRTHPLACE:":
                temp_answer = temp_answer.replace(", ",", \n")
                answer = Text(f"{temp_answer}", font_size=30, color="#4267B2", font="Open Sans")

            elif len(temp_answer) > 26 and item == "POSITION:":
                temp_answer = temp_answer.replace(" and ","\nand ")
                answer = Text(f"{temp_answer}", font_size=30, color="#4267B2", font="Open Sans")

            else:
                answer = Text(f"{temp_answer}", font_size=30, color="#4267B2",font="Open Sans")

            line.add(bullet,text, answer).arrange(RIGHT, center=False, buff=.25).move_to((0,2.25 - 1.25*index,0))

            x,y,z = line.get_corner(LEFT)

            line.shift((-x-2,0,0))

            bio_information.add(line)

        self.play(FadeIn(profile_pic, bottom_bio), title.animate.shift((-3.25,0,0)))
        self.wait(0.5)

        self.play(FadeIn(bio_information), run_time=1)
        self.wait(2)

        career_stats_text = Text(f"WAR: {my_player.career_stats['WAR']} / BA: {my_player.career_stats['BA']} / HR: {my_player.career_stats['HR']} / OPS+: {my_player.career_stats['OPS+']} / OBP: {my_player.career_stats['OBP']}", font_size=30, color=WHITE, font="Open Sans")
        career_stats_text.move_to((0,-6.35,0))
        self.play(FadeIn(career_text), career_stats_text.animate.shift((0,3,0)))

        self.wait(4)

        self.play(FadeOut(top_bio,title,profile_pic,bottom_bio,career_text,bio_information,career_stats_text), FadeIn(black_rectangle, run_time=1))

        self.camera.background_color = "#196a21"

        title = Text(f"NUMBERS THEY HAVE WORN", font_size=40, color=WHITE, font="Open Sans", weight=BOLD).move_to(
            (0, 3, 0))

        list_of_rectangles = VGroup()

        for i in range(-2, 3):
            list_of_rectangles.add(
                Rectangle(width=20, height=1, stroke_width=0, fill_color=GREEN, fill_opacity=1).move_to((0, 2 * i, 0)))

        self.play(FadeIn(list_of_rectangles, title), FadeOut(black_rectangle), run_time=1.5)


        circles_background = VGroup()
        jersey_numbers = VGroup()

        for index, number in enumerate(my_player.numbers):
            temp_circle = Circle(radius=1.25, fill_color=WHITE, fill_opacity=1, stroke_width=6).shift(
                ((7 - len(my_player.numbers)) * (index - (len(my_player.numbers) - 1) / 2), 0, 0))
            jersey_number = Text(f"{number}", font_size=80, color=BLACK, font="Open Sans", weight=BOLD).move_to(
                (temp_circle.get_center()))

            circles_background.add(temp_circle)
            jersey_numbers.add(jersey_number)

            self.play(GrowFromCenter(temp_circle), GrowFromCenter(jersey_number), run_time=1)
            self.wait(2)

        self.wait(1)
        self.play(FadeOut(*circles_background, *jersey_numbers, title), FadeIn(black_rectangle))
        self.remove(*list_of_rectangles)




        self.camera.background_color = "#ab946b"

        title1 = Text(f"CAREER", font_size=30, color=WHITE, font="Open Sans", weight=BOLD).move_to((-5.25, -2, 0))
        title2 = Text(f"PROGRESSION", font_size=30, color=WHITE, font="Open Sans", weight=BOLD).move_to(
            (-5.25, -2.5, 0))

        left_line = Line(start=((-2.5, -1, 0)), end=((-8.64, 5.5, 0)), stroke_opacity=1, stroke_width=8)
        right_line = Line(start=((2.5, -1, 0)), end=((8.64, 5.5, 0)), stroke_opacity=1, stroke_width=8)

        left_box = Rectangle(width=2, height=4, stroke_opacity=1, stroke_width=8, color=WHITE).shift((-2.5, -3, 0))
        right_box = Rectangle(width=2, height=4, stroke_opacity=1, stroke_width=8, color=WHITE).shift((2.5, -3, 0))

        shirt = ImageMobject("manim_images/HomePlate.png").scale(.6).shift((0, -3, 0))

        self.play(FadeIn(title1, title2, shirt, right_box, left_box, right_line, left_line), FadeOut(black_rectangle))

        circles_background = VGroup()
        date_ranges = VGroup()
        team_logos = []

        for index, team in enumerate(teams):

            temp_circle = Circle(radius=1.15, fill_color=WHITE, color=BLACK, fill_opacity=1, stroke_width=6)
            image = ImageMobject(f"manim_images/{team}.jpg")

            if len(years[index]) == 1:
                year_range = years[index][0]
            else:
                year_range = f"{years[index][0]} - {years[index][-1]}"

            date_range = Text(f"{year_range}", font_size=24, color=WHITE, font="Open Sans", weight=BOLD)

            circles_background.add(temp_circle)
            team_logos.append(image)
            date_ranges.add(date_range)

        circles_background.arrange(RIGHT, center=True, aligned_edge=LEFT, buff=1.35).move_to((0, 1.5, 0))
        self.bring_to_back(right_line, left_line)

        self.wait(0.5)

        for i in range(len(teams)):
            circle = circles_background[i]
            team_logos[i].scale(1.7).shift((circle.get_center()))
            date_ranges[i].shift((circle.get_center())).shift((0, 1.5, 0))
            self.play(GrowFromCenter(circle), GrowFromCenter(team_logos[i]), run_time=1)
            self.wait(2)

        for date_range in date_ranges:
            self.play(FadeIn(date_range, run_time=1))

        self.play(FadeOut(right_line, left_line, *circles_background, *team_logos, *date_ranges, title1, title2, shirt, right_box, left_box),
                  FadeIn(black_rectangle))

        self.camera.background_color = BLACK




        title = Text(f"CAREER ACCOLADES:", font_size=30, color=WHITE, font="Open Sans", weight=BOLD).move_to((-4.5, 3.5, 0))
        self.play(FadeIn(title), FadeOut(black_rectangle))

        accolade_plaques1 = VGroup()
        accolade_plaques2 = VGroup()
        accolade_texts = VGroup()

        if len(my_player.accolades) > 5:
            for index, accolade in enumerate(my_player.accolades):
                plaque = RoundedRectangle(width=4, height=0.75, corner_radius=0.15, fill_color=GOLD, fill_opacity=1,
                                          color=WHITE, stroke_width=4)

                if index > 4:
                    accolade_plaques2.add(plaque)

                else:
                    accolade_plaques1.add(plaque)

            accolade_plaques1.arrange(DOWN, center=True, aligned_edge=LEFT, buff=.25).shift((-3, 0, 0))
            accolade_plaques2.arrange(DOWN, center=True, aligned_edge=LEFT, buff=.25).shift(
                (3, (10 - len(my_player.accolades)) * .5, 0))

            for plaque in accolade_plaques1:
                accolade_text = Text(f"{my_player.accolades.pop(0)}", font_size=24, color=BLACK, weight=BOLD).move_to(
                    plaque.get_center())
                accolade_texts.add(accolade_text)

            for plaque in accolade_plaques2:
                accolade_text = Text(f"{my_player.accolades.pop(0)}", font_size=24, color=BLACK, weight=BOLD).move_to(
                    plaque.get_center())
                accolade_texts.add(accolade_text)

            self.play(FadeIn(accolade_plaques1, accolade_plaques2, accolade_texts))
            self.wait(3)
            self.play(FadeOut(accolade_plaques1, accolade_plaques2, accolade_texts, title))



        else:
            for accolade in my_player.accolades:
                plaque = RoundedRectangle(width=4, height=0.75, corner_radius=0.15, fill_color=GOLD, fill_opacity=1,
                                          color=WHITE, stroke_width=4)
                accolade_plaques1.add(plaque)

            accolade_plaques1.arrange(DOWN, center=True, aligned_edge=LEFT, buff=.35)

            for plaque in accolade_plaques1:
                accolade_text = Text(f"{my_player.accolades.pop(0)}", font_size=24, color=BLACK, weight=BOLD,
                                     font="Open Sans").move_to(plaque.get_center())
                accolade_texts.add(accolade_text)

            self.play(FadeIn(accolade_plaques1, accolade_texts))
            self.wait(3)
            self.play(FadeOut(accolade_plaques1, accolade_texts, title))

        closing = Text(f"KNOW WHO IT IS?", font_size=35, color=WHITE, font="Open Sans", weight=BOLD).move_to((0, 1, 0))
        closing2 = Text(f"AT WHAT TIME DID YOU GET IT?", font_size=30, color=WHITE, font="Open Sans").move_to((0, -1, 0))
        follow = Text(f"FOLLOW @GLEYBERMETRICS on TWITTER FOR MORE", font_size=22, color=WHITE,
                      font="Open Sans").move_to((0, -3, 0))
        self.play(FadeIn(closing, follow, closing2))
        self.wait(3)

