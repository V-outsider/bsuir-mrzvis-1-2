import math
import streamlit as st
import matplotlib.pyplot as plt

# Функция для вычисления закона Амдала
def amdal_law(serial_fraction, num_processors):
    return 1 / (serial_fraction + (1 - serial_fraction)*math.pow(num_processors, -1))

def efficiency(r, p):
    return r / p

def balanced_pipeline_r(k, p, t):
    return (k*p*t)/((k+p-1)*t)

def balanced_pipeline_e(k, p, t):
    return (k*t)/((k+p-1)*t)

def plot_graph(x, y, x_label, y_label, title):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.grid(True)
    st.pyplot(fig)

def main():
    with st.sidebar:
        st.title('BSUIR - 121731 - MRZVIS')
        st.write('Данное приложение разработано в ознакомительных целях.\n')
        st.write('Использованы следующие формулы:\n')

        st.divider()
        st.write('Закон Амдала\n')

        st.latex('S=\\frac{1}{(f+(1-f)*P^{-1})}')
        st.write('\nS - коэффициент ускорения')
        st.write('\nf - доля последовательных вычислений')
        st.write('\nP - колличество процессорных элементов')

        st.divider()

        st.write('Эффективность\n')
        st.latex('e=\\frac{r}{p}')
        st.write('\ne - коэффициент эффективности')
        st.write('\nr - коэффициент ускорения')
        st.write('\np - колличество процессорных элементов')

        st.divider()

        st.write('Ускорение сбалансированного конвейера\n')

        st.latex('S=\\frac{k*p*t}{(k+p-1)*t}')
        st.write('\nk - ранг задачи')
        st.write('\nt - время обработки этапа')
        st.write('\np - колличество процессорных элементов')

        st.divider()

        st.write('Эффективность сбалансированного конвейера\n')

        st.latex('e =\\frac{k*t}{(k+p-1)*t}')


        st.write('\nОбратная связь: V-outsider <voutsider@tutanota.com>.')

    with st.container(border=True):
        st.title('Калькулятор закона Амдала')
        st.write('Введите значения для расчета ускорения на основе закона Амдала')

        serial_fraction = st.number_input('Доля последовательной части', min_value=0.0, max_value=1.0, step=0.01,
                                        value=0.46)
        num_processors = st.number_input('Количество процессоров', min_value=1, max_value=1000, step=1, value=16)

        result = 0
        st.write()

        speedup = amdal_law(serial_fraction, num_processors)
        x = list(range(1, num_processors + 1))
        y = [amdal_law(serial_fraction, n) for n in x]
        
        plot_graph(x, y, 'Количество процессоров', 'Ускорение', 'Закон Амдала')

    with st.container(border=True):
        st.title('Коэффициент ускорения (ОКМД/ОКОД)')
        st.write('Введите значения для расчета коеффициента ускорения')

        simd = st.number_input('Время вычисления ОКОД', step=1.0, value=3.0)
        sisd = st.number_input('Время вычисления ОКМД', step=1.0, value=1.2)

        st.divider()

        st.write('Коэффициент ускорения: ' + str(simd/sisd))

    with st.container(border=True):
        st.title('Калькуляция эффективности:')
        input_values = st.text_input('Введите коэффициенты ускорения (,)', '1.35, 1.9, 2.1')
        acceleration_coefficient = [value.strip() for value in input_values.split(',')]

        input_values_2 = st.text_input('Введите колличество процессорных элементов (,)', '2, 8, 16')

        processors_count = [value.strip() for value in input_values_2.split(',')]

        e = []

        for r,p in zip(acceleration_coefficient, processors_count):
            e.append(efficiency(float(r),float(p)))

        plot_graph(processors_count, e, 'Колличество процессорных элеиентов', 'Эффективность','Кэффициент эффективности')
        

    with st.container(border=True):
        st.title('Сбалансированный конвейер')
        st.subheader('Коэффициенты ускорения и эффективности')

        k = st.number_input('Ранг задачи (k) (одновременно обрабатываемый объем данных)', min_value=1, max_value=1000, step=1, value=8)
        p = st.number_input('Колличество этапов (p)', min_value=1, max_value=1000, step=1, value=8)
        t = st.number_input('Время этапа (t)', min_value=0.1, max_value=1000.0, step=0.1, value=0.1)
        
        st.divider()

        st.write('Коэффициент ускорения: ' + str(balanced_pipeline_r(k, p, t)))
        st.write('Коэффициент эффективности: ' + str(balanced_pipeline_e(k, p, t)))





if __name__ == '__main__':
    main()