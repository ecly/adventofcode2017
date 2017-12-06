import java.util.*;

public class Redistribution{

    public static List<Integer> reallocate(List<Integer> blocks){
        int biggestBlock = 0;
        for(int i = 1; i < blocks.size(); i++)
            if(blocks.get(i) > blocks.get(biggestBlock))
                biggestBlock = i;

        int amountToDistribute = blocks.get(biggestBlock);
        blocks.set(biggestBlock, 0);
        for(int i = biggestBlock+1; i<=biggestBlock+amountToDistribute; i++){
            int index = i%blocks.size();
            int current = blocks.get(index);
            blocks.set(index,current+1);
        }
        return blocks;
    }

    // returns amounts of redistributions needed to see a previously seen state
    public static int solveFirst(List<Integer> blocks){
        Set<List<Integer>> seen = new HashSet<>();
        int redistributionCount = 0;
        while(!seen.contains(blocks)){
            seen.add(blocks);
            blocks = reallocate(blocks);
            redistributionCount++;
        }
        return redistributionCount;
    }

    // returns the size of the loop found by solveFirst
    public static int solveSecond(List<Integer> blocks){
        HashMap<List<Integer>, Integer> seen = new HashMap<>();
        int redistributionCount = 0;
        while(!seen.containsKey(blocks)){
            seen.put(blocks, redistributionCount);
            blocks = reallocate(blocks);
            redistributionCount++;
        }
        return redistributionCount - seen.get(blocks);
    }

    public static void main(String[] args){
        Integer[] blocks = new Integer[]{11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11};
        Integer[] test = new Integer[]{0,2,7,0};
        System.out.println("First Test: " + solveFirst(Arrays.asList(test)));
        System.out.println("First Answer: " + solveFirst(Arrays.asList(blocks)));
        System.out.println("Second Test: " + solveSecond(Arrays.asList(test)));
        System.out.println("Second Answer: " + solveSecond(Arrays.asList(blocks)));
    }
}
