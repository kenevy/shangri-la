from App.ext import models


class Article(models.Model):
    article_id = models.Column(models.Integer, primary_key=True)
    article_name = models.Column(models.String(255))
    article_content = models.Column(models.Text)
    article_tag = models.Column(models.String(255))
    create_at = models.Column(models.Integer)
    update_at = models.Column(models.Integer, default=create_at)
    reading_number = models.Column(models.Integer, default=0)
    edit_user = models.Column(models.String(50))
    comment_number = models.Column(models.Integer, default=0)

    def save(self):
        try:
            models.session.add(self)
            models.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    #
    # def update_tag(tag, attr):
    #     tag.update(attr)
    #     models.session.commit()

    def delete(self):
        try:
            models.session.delete(self)
            models.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
