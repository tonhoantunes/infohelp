from django.shortcuts import render, redirect, get_object_or_404
from .models import Curso, Salvos, Aula
from usuarios.models import Perfil
from .forms import CursoForm, SalvosForm, AulaForm
from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.

def index(request):

    return render(request, "index.html")

def login(request):

    return render(request, "login.html")

def inicio(request):
    usuario = request.user
    perfil = None  # Valor padrão caso o usuário não esteja autenticado
    
    if usuario.is_authenticated:
        perfil = get_object_or_404(Perfil, usuario=usuario)
    
    context = {
        "cursos": Curso.objects.all(),
        "perfil": perfil,
    }
    
    return render(request, "inicio.html", context)


#CRUD de Cursos
def listar_cursos(request):
    context = {}

    # Obtém todos os cursos inicialmente
    cursos = Curso.objects.all()

    # Filtra por categoria, se fornecida
    cate = request.GET.get('categoria')
    if cate:
        cursos = cursos.filter(categoria__icontains=cate)  # Use icontains para busca case-insensitive

    # Filtra por busca, se fornecida
    busca = request.GET.get('busca')
    if busca:
        busca_descricao = cursos.filter(descricao__icontains=busca)
        busca_nome = cursos.filter(nome__icontains=busca)
        cursos = busca_descricao | busca_nome

    # Adiciona os cursos filtrados ao contexto
    context['cursos'] = cursos

    # Adiciona as categorias ao contexto
    categorias = Curso.categoria_do_curso  # Certifique-se de que isso retorna as categorias corretamente
    context['categorias'] = categorias

    # Adiciona o perfil do usuário ao contexto, se autenticado
    if request.user.is_authenticated:
        usuario = request.user
        perfil = get_object_or_404(Perfil, usuario=usuario)
        context['perfil'] = perfil

    return render(request, "listar_cursos.html", context)

def detalhes_curso(request, curso_id):
    usuario = request.user
    perfil = None  # Valor padrão caso o usuário não esteja autenticado
    
    # Se o usuário estiver autenticado, tenta carregar o perfil
    if usuario.is_authenticated:
        perfil = get_object_or_404(Perfil, usuario=usuario)

    # Carregar o curso
    curso = get_object_or_404(Curso, pk=curso_id)
    
    # Carregar as aulas do curso
    aulas = Aula.objects.filter(curso=curso)

    # Contar a quantidade de vídeos (aulas com link)
    quantidade_videos = aulas.filter(link__isnull=False).count()

    # Contar a quantidade de artigos (aulas com texto não vazio)
    quantidade_artigos = aulas.exclude(texto__exact='').count()  # Apenas aulas com texto não vazio

    context = {
        'curso': curso,
        'aula': aulas,
        'perfil': perfil,  # Pode ser None se o usuário não estiver autenticado
        'quantidade_videos': quantidade_videos,  # Passa a quantidade de vídeos para o template
        'quantidade_artigos': quantidade_artigos,  # Passa a quantidade de artigos para o template
    }

    return render(request, "pag_curso.html", context)

@login_required
@permission_required('infohelp.criar_curso', raise_exception=True)
def criar_curso(request):
    usuario = request.user
    perfil = get_object_or_404(Perfil, usuario=usuario)

    if request.method == "POST":
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            curso = form.save(commit=False)
            curso.usuario = request.user
            curso.save()
            messages.success(request, "Curso criado com sucesso!")  # Mensagem de sucesso
            return redirect('detalhes_curso', curso_id=curso.id)
        else:
            # Exibe mensagens de erro se o formulário não for válido
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")  # Mensagem de erro
    else:
        form = CursoForm()

    context = {
        'form': form,
        'perfil': perfil,
    }

    return render(request, "criar_curso.html", context)

@permission_required('infohelp.editar_curso', raise_exception=True)
def editar_curso(request, curso_id):
    usuario = request.user
    perfil = get_object_or_404(Perfil, usuario=usuario)

    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, "Curso atualizado com sucesso!")  # Mensagem de sucesso
            return redirect('listar_cursos')
        else:
            # Exibe mensagens de erro se o formulário não for válido
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")  # Mensagem de erro
    else:
        form = CursoForm(instance=curso)

    context = {
        "curso": curso,
        "form": form,
        "perfil": perfil,
    }

    return render(request, "editar_curso.html", context)

def excluir_curso(request, curso_id):
    usuario = request.user
    perfil = get_object_or_404(Perfil, usuario=usuario)

    context = {
        "curso": get_object_or_404(Curso, id=curso_id),
        "perfil": perfil,
    }

    if request.method == "POST":
        context["curso"].delete()
        return redirect('listar_cursos')
    else:
        return render(request, "excluir_curso.html", context)



#CRUD de Aulas
@permission_required('infohelp.criar_aula', raise_exception=True)
def criar_aula(request, curso_id):
    usuario = request.user
    perfil = get_object_or_404(Perfil, usuario=usuario)

    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == "POST":
        form = AulaForm(request.POST, request.FILES)
        if form.is_valid():
            aula = form.save(commit=False)
            aula.curso = curso
            aula.save()
            messages.success(request, "Aula criada com sucesso!")  # Mensagem de sucesso
            return redirect('detalhes_curso', curso_id=curso.id)
        else:
            # Exibe mensagens de erro se o formulário não for válido
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")  # Mensagem de erro
    else:
        form = AulaForm()

    context = {
        'form': form,
        'curso': curso,
        'perfil': perfil,
    }

    return render(request, 'criar_aula.html', context)

@permission_required('infohelp.editar_aula', raise_exception=True)
def editar_aula(request, curso_id, aula_id):
    usuario = request.user
    perfil = get_object_or_404(Perfil, usuario=usuario)

    aula = get_object_or_404(Aula, id=aula_id)
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == 'POST':
        form = AulaForm(request.POST, request.FILES, instance=aula)
        if form.is_valid():
            form.save()
            messages.success(request, "Aula atualizada com sucesso!")  # Mensagem de sucesso
            return redirect('detalhes_aula', curso_id=curso.id, aula_id=aula.id)
        else:
            # Exibe mensagens de erro se o formulário não for válido
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")  # Mensagem de erro
    else:
        form = AulaForm(instance=aula)

    context = {
        "aula": aula,
        "curso": curso,
        "form": form,
        "perfil": perfil,
    }

    return render(request, "editar_aula.html", context)

@login_required
def detalhes_aula(request, curso_id, aula_id):
    usuario = request.user
    perfil = get_object_or_404(Perfil, usuario=usuario)

    aulas = Aula.objects.all()

    aula = get_object_or_404(Aula, id=aula_id)
    curso = get_object_or_404(Curso, id=curso_id)
    
    return render(request, "exibir_aula.html", {'aulas' : aulas, 'curso' : curso, 'aula' : aula, 'perfil': perfil})

def excluir_aula(request, curso_id, aula_id):
    usuario = request.user
    perfil = get_object_or_404(Perfil, usuario=usuario)

    aula = get_object_or_404(Aula, id=aula_id)
    curso = get_object_or_404(Curso, id=curso_id)

    context = {
        "curso": get_object_or_404(Curso, id=curso_id),
        "aula": get_object_or_404(Aula, id=aula_id),
        "perfil": perfil,
    }

    if request.method == "POST":
        context["aula"].delete()
        return redirect('detalhes_curso', curso.id)
    else:
        return render(request, "excluir_aula.html", context)



@login_required
def biblioteca(request):
    usuario = request.user
    perfil = get_object_or_404(Perfil, usuario=usuario)

    # Coleções de cursos salvos pelo usuário
    salvos = Salvos.objects.filter(usuario=request.user)

    # Filtro por coleção (se fornecido)
    filtro_salvo = request.GET.get('filtro_salvo')
    if filtro_salvo:
        # Filtra os cursos pela coleção selecionada
        cursos_salvos = Curso.objects.filter(salvos__id=filtro_salvo, salvos__usuario=request.user).distinct()
        # Obtém a coleção filtrada
        colecao_filtrada = Salvos.objects.get(id=filtro_salvo)
    else:
        # Todos os cursos salvos pelo usuário (independentemente da coleção)
        cursos_salvos = Curso.objects.filter(salvos__usuario=request.user).distinct()
        colecao_filtrada = None

    context = {
        'salvos': salvos,
        'cursos_salvos': cursos_salvos,  # Cursos filtrados ou todos os cursos salvos
        'perfil': perfil,
        'filtro_salvo': int(filtro_salvo) if filtro_salvo else None,  # Passa o filtro selecionado para o template
        'colecao_filtrada': colecao_filtrada,  # Passa a coleção filtrada para o template
    }

    return render(request, 'biblioteca.html', context)

# exibiçãpo de cursos para quem não está logado
def busca(request):
    cursos = Curso.objects.all()

    return render(request, 'busca.html', {'cursos': cursos})


@login_required
def criar_salvos(request):
    if request.method == 'POST':
        form = SalvosForm(request.POST)
        if form.is_valid():
            salvos = form.save(commit=False)
            salvos.usuario = request.user  # Associar a salvos ao usuário logado
            salvos.save()
            form.save_m2m()  # Salvar a relação de muitos para muitos com músicas
            return redirect('listar_cursos')  # Redireciona para uma página de sucesso
    else:
        form = SalvosForm()

    return render(request, 'criar_salvos.html', {'form': form})



@login_required
def salvar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    salvos, created = Salvos.objects.get_or_create(usuario=request.user)
    
    if curso in salvos.cursos.all():
        salvos.cursos.remove(curso)
        salvo = False
    else:
        salvos.cursos.add(curso)
        salvo = True
    
    return JsonResponse({'salvo': salvo})


@login_required
def salvar_curso_em_colecao(request):
    if request.method == "POST":
        curso_id = request.POST.get("curso_id")
        salvos_id = request.POST.get("salvos_id")

        curso = get_object_or_404(Curso, id=curso_id)
        salvos = get_object_or_404(Salvos, id=salvos_id, usuario=request.user)

        if curso in salvos.cursos.all():
            return JsonResponse({"message": f"O curso já está salvo na coleção '{salvos.nome}'!", "salvo": True})
        else:
            salvos.cursos.add(curso)
            return JsonResponse({"message": f"Curso salvo na coleção '{salvos.nome}'!", "salvo": True})
    
    return JsonResponse({"error": "Requisição inválida"}, status=400)

@login_required
def listar_colecoes_salvos(request):
    colecoes = Salvos.objects.filter(usuario=request.user).values("id", "nome")
    return JsonResponse({"colecoes": list(colecoes)})

@login_required
def criar_nova_colecao(request):
    if request.method == "POST":
        nome_colecao = request.POST.get("nome")
        if nome_colecao:
            nova_colecao, created = Salvos.objects.get_or_create(usuario=request.user, nome=nome_colecao)
            return JsonResponse({"id": nova_colecao.id, "nome": nova_colecao.nome, "created": created})
    return JsonResponse({"error": "Nome inválido"}, status=400)

@login_required
def verificar_curso_salvo(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    colecoes = Salvos.objects.filter(usuario=request.user, cursos=curso).values("id", "nome")

    return JsonResponse({
        "salvo": colecoes.exists(),
        "colecoes": list(colecoes),
    })

@login_required
def remover_curso_de_salvos(request):
    if request.method == "POST":
        curso_id = request.POST.get("curso_id")
        curso = get_object_or_404(Curso, id=curso_id)

        # Remove o curso de todas as coleções do usuário
        salvos = Salvos.objects.filter(usuario=request.user, cursos=curso)
        if salvos.exists():
            for salvo in salvos:
                salvo.cursos.remove(curso)
            return JsonResponse({"removido": True})
        
        return JsonResponse({"removido": False, "error": "Curso não estava salvo!"})
    
    return JsonResponse({"error": "Requisição inválida"}, status=400)