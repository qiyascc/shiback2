from modeltranslation.translator import translator, TranslationOptions
from .models import TeamMember, Gallery

class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position')

translator.register(TeamMember, TeamMemberTranslationOptions)

class GalleryTranslationOptions(TranslationOptions):
    fields = ('description',)

translator.register(Gallery, GalleryTranslationOptions)