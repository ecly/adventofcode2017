defmodule Circus do
  @parent ~r/(\w+) \((\d+)\) -> ([\w+,?\s?]+)/
  @child ~r/(\w+) \((\d+)\)/

  def parseChildren(children) do
    children
    |> String.split(",")
    |> Enum.map(fn s -> String.trim(s) end)
  end

  def parseParent(line) do
    [[_, parent, weight, childString]] = Regex.scan(@parent, line)
    children = parseChildren(childString)
    {parent, {weight, children}}
  end

  def parseChild(line) do
    [[_, child, weight]] = Regex.scan(@child, line)
    {child, {weight, []}}
  end

  def parse(graph \\ %{}, file) do
    line = file |> IO.read(:line)
    cond do
      line == :eof -> graph
      Regex.match?(@parent, line) -> 
        {parent, value} = parseParent(line)
        Map.put(graph, parent, value)
        |> parse(file)
      Regex.match?(@child, line) -> 
        {child, value} = parseChild(line)
        Map.put(graph, child, value)
        |> parse(file)
      true -> graph
    end
  end

  def solve(filename) do
    {:ok, file} = File.open(filename, [:read])
    graph = parse(file)
    parents = Enum.filter(graph, fn p -> !match?({_,{_,[]}}, p) end)
    children = Enum.flat_map(graph, fn {_,{_,c}} -> c end)
    Keyword.keys(parents) -- children
  end
end

Circus.solve("test.in")
|> IO.inspect
Circus.solve("input.in")
|> IO.inspect
