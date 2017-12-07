defmodule Program do
  defstruct key: nil, weight: 0, children: [], disc_weight: 0
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

  def is_same?([x|xss]) do
    x == hd(xss) && is_same?(xss)
  end

  def solve_first(filename) do
    {:ok, file} = File.open(filename, [:read])
    parse(file)
    |> get_root
  end

  def solve_second(filename) do
    {:ok, file} = File.open(filename, [:read])
    parse(file)
  end
end

IO.write "first: "
Circus.solve_first("input.in")
|> IO.puts

# IO.write"second: "
# Circus.solve_second("input.in")
# |> IO.puts
