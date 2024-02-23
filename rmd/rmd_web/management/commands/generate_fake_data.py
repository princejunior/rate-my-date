import random
from faker import Faker
from datetime import datetime, timedelta
from django.utils import timezone
from rmd_web.models import User, Person, Post, Comments

fake = Faker()

# Generate fake data for User, Person, and Post
for _ in range(10):
    # Generate User data
    user = User.objects.create(
        firstname=fake.first_name(),
        lastname=fake.last_name(),
        phone=random.randint(1000000000, 9999999999),
        joined_date=fake.date_between(start_date='-2y', end_date='today')
    )

    # Generate Person data
    person = Person.objects.create(
        firstname=user.firstname,
        lastname=user.lastname,
        istagram_account=fake.user_name(),
        joined_date=user.joined_date
    )

    # Generate 5 posts for each person
    for _ in range(5):
        post = Post.objects.create(
            person_id=person.id,
            person_firstname=person.firstname,
            person_lastname=person.lastname,
            post=fake.text(max_nb_chars=255),
            agree=fake.word(),
            disagree=random.randint(0, 10),
            comments=fake.text(max_nb_chars=255)
        )

        # Generate comments for each post
        for _ in range(random.randint(0, 10)):
            comment = Comments.objects.create(
                post_id=post.id,
                comment_date_created=fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.get_current_timezone()),
                agree=fake.word(),
                disagree=random.randint(0, 5)
            )
