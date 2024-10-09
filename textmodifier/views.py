from django.shortcuts import render
from .forms import TextFileUploadForm
from .utils import shake_text


def text_view(request):
    if request.method == 'POST':
        form = TextFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_content = uploaded_file.read().decode('utf-8')
            modified_text = shake_text(file_content)
            return render(request, 'textmodifier/result.html', {'modified_text': modified_text})
    else:
        form = TextFileUploadForm()
    return render(request, 'textmodifier/base.html', {'form': form})
