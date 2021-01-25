from django.db import models


class TypeSmi(models.Model):
    name = models.CharField("Тип СМИ", max_length=200)

    class Meta:
        verbose_name = u"Тип СМИ"
        verbose_name_plural = u"Типы СМИ"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class NewsType(models.Model):
    name = models.CharField("Категория новостей", max_length=200)

    class Meta:
        verbose_name = u"Категория новостей"
        verbose_name_plural = u"Категории новостей"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField("Название службы", max_length=200)

    class Meta:
        verbose_name = u"Служба"
        verbose_name_plural = u"Службы"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class KeyWord(models.Model):
    name = models.CharField("Ключевое слово", max_length=200)

    class Meta:
        verbose_name = u"Тэг"
        verbose_name_plural = u"Тэги"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Smi(models.Model):
    name = models.CharField("СМИ", max_length=200)
    url = models.URLField("Ссылка", blank=True, null=True)
    type_smi = models.ForeignKey(
        TypeSmi,
        on_delete=models.CASCADE,
        related_name="type_smi",
        verbose_name=u"Тип СМИ",
    )

    class Meta:
        verbose_name = u"СМИ"
        verbose_name_plural = u"СМИ"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField("Новость", max_length=280)
    url = models.URLField("Ссылка", blank=True, null=True)
    pub_date = models.DateField("Дата новости", auto_now_add=False)
    age = models.BooleanField("Дети", default=False)
    smi = models.ForeignKey(
        Smi,
        on_delete=models.CASCADE,
        related_name="smi",
        verbose_name=u"СМИ",
    )
    news_type = models.ForeignKey(
        NewsType,
        on_delete=models.CASCADE,
        related_name="news_type",
        verbose_name=u"Категория новости",
    )
    keywords = models.ManyToManyField(
        KeyWord,
        verbose_name=u"Ключевые слова",
    )
    departments = models.ManyToManyField(
        Department,
        verbose_name=u"Служба",
    )

    @property
    def display_ts(self):
        return self.smi.type_smi

    @property
    def display_key(self):
        return ", ".join([keywords.name for keywords in self.keywords.all()])

    @property
    def display_dept(self):
        return ", ".join([departments.name for departments in self.departments.all()])

    class Meta:
        verbose_name = u"Публикация"
        verbose_name_plural = u"Публикации"

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
