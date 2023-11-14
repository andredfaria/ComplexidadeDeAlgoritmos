def quick_sort(arr)
  return arr if arr.length <= 1

  pivot = arr[0]
  less = arr[1..].select { |x| x <= pivot }
  greater = arr[1..].select { |x| x > pivot }

  quick_sort(less) + [pivot] + quick_sort(greater)
end

def measure_time(arr)
  start_time = Time.now
  quick_sort(arr)
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

require 'matplotlib'
Matplotlib::Pyplot.plot(list_sizes, execution_times, marker: 'o', linestyle: '-', color: 'b')
Matplotlib::Pyplot.xlabel('Tamanho da Lista')
Matplotlib::Pyplot.ylabel('Tempo de Execução (segundos)')
Matplotlib::Pyplot.title('Desempenho do Quick Sort')
Matplotlib::Pyplot.grid(true)
Matplotlib::Pyplot.show
