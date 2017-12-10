defmodule Program do
  defstruct key: nil, weight: 0, children: [], disc_weights: []
end

defmodule Circus do
  @parent ~r/(\w+) \((\d+)\) -> ([\w+,?\s?]+)/
  @child ~r/(\w+) \((\d+)\)/

  def parseChildren(children) do
    children
    |> String.split(",")
    |> Enum.map(&String.trim/1)
  end

  def parseParent(line) do
    [[_, key, weight, childString]] = Regex.scan(@parent, line)
    children = parseChildren(childString)
    %Program{key: key, weight: String.to_integer(weight), children: children}
  end

  def parseChild(line) do
    [[_, key, weight]] = Regex.scan(@child, line)
    %Program{key: key, weight: String.to_integer(weight)}
  end

  def parse(graph \\ %{}, file) do
    line = file |> IO.read(:line)
    cond do
      line == :eof -> graph
      Regex.match?(@parent, line) -> 
        parent = parseParent(line)
        Map.put(graph, parent.key, parent)
        |> parse(file)
      Regex.match?(@child, line) -> 
        child = parseChild(line)
        Map.put(graph, child.key, child)
        |> parse(file)
      true -> graph
    end
  end

  def get_root(graph) do
    parents = Enum.filter(graph, fn {_,v} -> !Enum.empty?(v.children) end)
              |> Enum.map(fn {k, _} -> k end)
    children = Enum.flat_map(graph, fn {_,v} -> v.children end)
    hd(parents -- children)
  end

  def is_same?([]), do: true
  def is_same?([x|xs]), do: Enum.all?(xs, fn y -> x==y end)
    
  def get_program_disc_weight(%Program{disc_weights: dw, weight: w}), do: w + Enum.sum(dw)

  def calculate_disc_weight(graph, key) do
    case graph[key] do
        %{children: []} -> graph
        p = %{disc_weights: []} -> 
                new_graph = List.foldr(p.children, graph, fn(c, acc) -> calculate_disc_weight(acc, c) end)
                disc_weights = Enum.map(p.children, fn c -> new_graph[c] end)
                               |> Enum.map(fn c -> get_program_disc_weight(c) end)
                %{new_graph | key => %Program{p | disc_weights: disc_weights}}
    end
  end

  # Finds the program that is unbalanced the furthest up the tree from the given keys 
  # Returns the value it should be to correct the imbalance - searches up from the given keys
  def get_correction(graph, program) do
     children = Enum.map(program.children, fn c -> graph[c] end)
     bad_branch = Enum.find(children, fn c -> !is_same?(c.disc_weights) end)
     case bad_branch do
        nil -> weights = Enum.map(children, &get_program_disc_weight/1)
               if is_same?(weights) do 
                   {:error, "Tree is balanced"}
               else 
                    occurences = Enum.reduce(weights, %{}, fn x, acc -> Map.update(acc, x, 1, &(&1 + 1)) end)
                    outlier_val = Enum.find(occurences, fn {_,v} -> v == 1 end) |> elem(0)
                    outlier = Enum.find(children, fn p -> get_program_disc_weight(p) == outlier_val end)
                    target_val = Enum.find(occurences, fn {_,v} -> v != 1 end) |> elem(0)
                    diff = target_val - outlier_val
                    {:ok, outlier.weight + diff}
               end
        p   -> get_correction(graph, p)
    end
  end

  def solve_first(filename) do
    {:ok, file} = File.open(filename, [:read])
    parse(file)
    |> get_root
  end

  # A rather unpleasant solution for the second half
  def solve_second(filename) do
    {:ok, file} = File.open(filename, [:read])
    graph = parse(file)
    root = get_root(graph)
    calculated_graph = calculate_disc_weight(graph, root)
    get_correction(calculated_graph, calculated_graph[root])
  end
end

IO.write "first: "
Circus.solve_first("input.in")
|> IO.puts

IO.write"second: "
Circus.solve_second("input.in")
|> elem(1)
|> IO.puts
