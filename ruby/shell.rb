def shell_sort(arr)
  n = arr.length
  gap = n / 2
  while gap > 0
    (gap...n).each do |i|
      temp = arr[i]
      j = i
      while j >= gap && arr[j - gap] > temp
        arr[j] = arr[j - gap]
        j -= gap
      end
      arr[j] = temp
    end
    gap = gap / 2
  end
end

def measure_time(arr)
  start_time = Time.now.to_f
  shell_sort(arr)
  end_time = Time.now.to_f
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
pyplot = Matplotlib::Pyplot

pyplot.plot(list_sizes, execution_times, marker: 'o', linestyle: '-', color: 'b')
pyplot.xlabel('Tamanho da Lista')
pyplot.ylabel('Tempo de Execução (segundos)')
pyplot.title('Desempenho do Shell Sort')
pyplot.grid(true)
pyplot.show
