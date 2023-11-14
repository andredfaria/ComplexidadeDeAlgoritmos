require 'gruff'

def bubble_sort(arr)
  n = arr.length

  (0..n-1).each do |i|
    (0..n-i-2).each do |j|
      if arr[j] > arr[j+1]
        arr[j], arr[j+1] = arr[j+1], arr[j]
      end
    end
  end
end

def measure_time(arr)
  start_time = Time.now
  bubble_sort(arr)
  end_time = Time.now
  end_time - start_time
end

list_sizes = (100..20000).step(100).to_a

execution_times = []
list_sizes.each do |size|
  arr = Array.new(size) { rand(1..10000) }
  time_taken = measure_time(arr)
  execution_times << time_taken
end

# Using Gruff for plotting
graph = Gruff::Line.new
graph.title = 'Desempenho do Bubble Sort'
graph.x_axis_label = 'Tamanho da Lista'
graph.y_axis_label = 'Tempo de Execução (segundos)'
graph.data('Bubble Sort', execution_times)

graph.write('bubble_sort_performance.png')
