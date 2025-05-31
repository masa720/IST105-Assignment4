from django.shortcuts import render
from .forms import InputForm
import math

def calculate_view(request):
    result = None
    error = None
    message = None

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']

            if not all(isinstance(val, (int, float)) for val in [a, b, c]):
                error = "All inputs must be numeric."
            elif a < 1:
                error = "Input 'a' is too small."
            elif c < 0:
                error = "Input 'c' must be non-negative."
            else:
                if b == 0:
                    message = "Input 'b' is zero and will not affect the result."

                c_cubed = c ** 3
                sqrt_c_cubed = math.sqrt(c_cubed)

                if c_cubed > 1000:
                    temp = sqrt_c_cubed * 10
                else:
                    temp = sqrt_c_cubed / a

                final_result = temp + b
                result = f"{final_result:.2f}"

        else:
            error = "Invalid input. Please enter valid numbers."
    else:
        form = InputForm()

    return render(request, 'calculator/result.html', {
        'form': form,
        'result': result,
        'error': error,
        'message': message
    })
