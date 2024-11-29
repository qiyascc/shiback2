from modeltranslation.translator import TranslationOptions, translator
from .models import Project, Badge

class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'client', 'industry')

class BadgeTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Project, ProjectTranslationOptions)
translator.register(Badge, BadgeTranslationOptions)
