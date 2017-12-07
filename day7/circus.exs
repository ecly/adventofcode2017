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
    {parent, children}
  end

  def parseChild(line) do
    [[_, child, weight]] = Regex.scan(@child, line)
    child
  end

  def parse(file, parents \\ [], children \\ []) do
    line = file |> IO.read(:line)
    cond do
      line == :eof -> {parents, children}
      Regex.match?(@parent, line) -> 
        {parent, newChildren} = parseParent line
        parse(file, [parent|parents], newChildren ++ children)
      Regex.match?(@child, line) -> 
        child = parseChild line
        parse(file, parents, [child|children])
      true -> {parents, children}
    end
  end

  def solve(filename) do
    {:ok, file} = File.open(filename, [:read])
    {parents, children} = parse(file)
    parents -- children
  end
end

Circus.solve("test.in")
|> IO.inspect
Circus.solve("input.in")
|> IO.inspect
