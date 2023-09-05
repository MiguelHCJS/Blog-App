from blog_setup.models.AppDesignPattern import DesignPatternSetup


def AppDesignPattern(request):
    setup = DesignPatternSetup.objects.order_by('-id').first()
    return {
        'AppDesignPattern': setup,
    }

# PROXIMAS IMPLEMENTAÇÕES
#
# def ConvencionalCommits(request):
#     setup = ConvencionalCommitsSetup.objects.order_by('-id').first()
#     return {
#         'ConvencionalCommits': setup,
#     }
