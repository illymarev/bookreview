from django.views import generic
from .models import BookModel, Quote
from django.urls import reverse
from .forms import CommentForm


# Create your views here.

class BookList(generic.ListView):
    model = BookModel
    template_name = 'books/book_list.html'
    ordering = ['-created_date']


class BookDetail(generic.DetailView, generic.edit.ModelFormMixin):
    model = BookModel
    form_class = CommentForm
    template_name = 'books/book_detail.html'
    context_object_name = 'bookmodel'

    def get_success_url(self):
        return reverse('books:book-detail', kwargs={'pk': self.object.book.id})

    # self.object - Comment model, self.object.book.id - book model

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # adding form
        context['form'] = self.get_form()
        # adding comments
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        # getting data from POST request
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                # function defined below to save the form to DB
                return self.form_valid(comment_form)

    def form_valid(self, comment_form):
        new_comment = comment_form.save(commit=False)
        # Giving PK to comment
        new_comment.book = self.get_object()
        new_comment.save()
        return super().form_valid(comment_form)


class Quotes(generic.ListView):
    model = Quote
    template_name = 'books/all_quotes.html'

class BookQuotes(generic.ListView):
    model = Quote
    template_name = 'books/book_quotes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookid'] = int(self.kwargs.get('pk'))
        return context

