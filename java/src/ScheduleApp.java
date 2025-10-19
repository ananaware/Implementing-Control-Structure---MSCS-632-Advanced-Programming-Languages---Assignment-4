import java.util.*;
import java.util.stream.Collectors;

public class ScheduleApp {

    // ----------- Constants -----------
    static final List<String> DAYS   = Arrays.asList("Mon","Tue","Wed","Thu","Fri","Sat","Sun");
    static final List<String> SHIFTS = Arrays.asList("morning","afternoon","evening");

    static final int MIN_PER_SHIFT   = 2;
    static final int MAX_DAYS_PER    = 5;
    static final int SHIFT_CAP       = 3;
    static final long RANDOM_SEED    = 42L;

    // ----------- Data -----------
    // schedule.get(day).get(shift) -> List<String> employees
    static final Map<String, Map<String, List<String>>> schedule = new LinkedHashMap<>();
    // workedDays.get(name) -> int (distinct days worked)
    static final Map<String, Integer> workedDays = new HashMap<>();
    // assignedToday.get(day) -> Set<String> (enforce 1 shift/day)
    static final Map<String, Set<String>> assignedToday = new HashMap<>();
    // preferences.get(name).get(day) -> ranked List<String> of shifts
    static final Map<String, Map<String, List<String>>> preferences = new HashMap<>();

    static final Random rnd = new Random(RANDOM_SEED);

    public static void main(String[] args) {
        initContainers();

        // Demo employees + ranked prefs
        List<String> employees = demoSeedPreferences();

        scheduleWeek(employees);
        prettyPrintSchedule();
        printSummary(employees);

        // (Optional) CSV/MD export could be added here if required
    }

    static void initContainers() {
        for (String d : DAYS) {
            Map<String, List<String>> byShift = new LinkedHashMap<>();
            for (String s : SHIFTS) byShift.put(s, new ArrayList<>());
            schedule.put(d, byShift);
            assignedToday.put(d, new HashSet<>());
        }
    }

    // ----------- Core helpers -----------
    static boolean canAssign(String name, String day) {
        return !assignedToday.get(day).contains(name) && workedDays.getOrDefault(name,0) < MAX_DAYS_PER;
    }

    static boolean shiftHasRoom(String day, String shift) {
        return schedule.get(day).get(shift).size() < SHIFT_CAP;
    }

    static boolean assign(String name, String day, String shift) {
        if (!canAssign(name, day)) return false;
        if (!shiftHasRoom(day, shift)) return false;
        schedule.get(day).get(shift).add(name);
        assignedToday.get(day).add(name);
        workedDays.put(name, workedDays.getOrDefault(name, 0) + 1);
        return true;
    }

    static boolean tryRanked(String name, String day) {
        List<String> ranks = preferences.getOrDefault(name, Collections.emptyMap())
                .getOrDefault(day, Collections.emptyList());
        for (String s : ranks) {
            if (assign(name, day, s)) return true;
        }
        return false;
    }

    static boolean resolveConflictOrReassign(String name, String day) {
        List<String> ranks = preferences.getOrDefault(name, Collections.emptyMap())
                .getOrDefault(day, Collections.emptyList());

        // 1) other shifts same day
        for (String s : SHIFTS) {
            if (ranks.contains(s)) continue;
            if (assign(name, day, s)) return true;
        }

        // find next day (no wrap)
        int idx = DAYS.indexOf(day);
        if (idx < 0 || idx >= DAYS.size() - 1) return false;
        String nextDay = DAYS.get(idx + 1);

        // 2) ranked next day
        List<String> nextRanks = preferences.getOrDefault(name, Collections.emptyMap())
                .getOrDefault(nextDay, Collections.emptyList());
        for (String s : nextRanks) {
            if (assign(name, nextDay, s)) return true;
        }

        // 3) any remaining next day
        for (String s : SHIFTS) {
            if (nextRanks.contains(s)) continue;
            if (assign(name, nextDay, s)) return true;
        }
        return false;
    }

    static void fillMinimumStaff(String day, List<String> allEmps) {
        for (String s : SHIFTS) {
            while (schedule.get(day).get(s).size() < MIN_PER_SHIFT) {
                // eligibles: not assigned today and < MAX_DAYS_PER
                List<String> elig = allEmps.stream()
                    .filter(e -> canAssign(e, day))
                    .filter(e -> !assignedToday.get(day).contains(e))
                    .collect(Collectors.toList());

                if (elig.isEmpty()) break;
                String pick = elig.get(rnd.nextInt(elig.size()));
                if (!assign(pick, day, s)) {
                    allEmps = allEmps.stream().filter(e -> !e.equals(pick)).collect(Collectors.toList());
                }
            }
        }
    }

    // ----------- Driver -----------
    static void scheduleWeek(List<String> allEmps) {
        for (String day : DAYS) {
            for (String name : allEmps) {
                if (!canAssign(name, day)) continue;
                if (tryRanked(name, day)) continue;
                resolveConflictOrReassign(name, day);
            }
            fillMinimumStaff(day, allEmps);
        }
    }

    // ----------- Demo data -----------
    static List<String> demoSeedPreferences() {
        List<String> emps = Arrays.asList("Alex","Blair","Casey","Dev","Eden","Finn");
        for (String e : emps) {
            Map<String, List<String>> byDay = new HashMap<>();
            for (String d : DAYS) {
                List<String> perm = new ArrayList<>(SHIFTS);
                Collections.shuffle(perm, rnd);  // random ranking
                byDay.put(d, perm);
            }
            preferences.put(e, byDay);
            workedDays.put(e, 0);
        }
        return emps;
    }

    // ----------- Output -----------
    static void prettyPrintSchedule() {
        System.out.println("\n============================");
        System.out.println("      Final Weekly Schedule");
        System.out.println("============================");
        for (String d : DAYS) {
            System.out.println("\n" + d + ":");
            for (String s : SHIFTS) {
                List<String> names = schedule.get(d).get(s);
                String joined = names.isEmpty() ? "-" : String.join(", ", names);
                System.out.printf("  %-10s (%d) -> %s%n", s, names.size(), joined);
            }
        }
    }

    static void printSummary(List<String> emps) {
        System.out.println("\n----------------------------");
        System.out.println("         Weekly Summary");
        System.out.println("----------------------------");
        emps.stream()
            .sorted(Comparator.comparing((String n) -> workedDays.getOrDefault(n,0)).reversed()
                    .thenComparing(n -> n))
            .forEach(n -> System.out.printf("%-10s : %d day(s)%n", n, workedDays.getOrDefault(n,0)));

        int total = 0;
        for (String d : DAYS) {
            for (String s : SHIFTS) total += schedule.get(d).get(s).size();
        }
        System.out.println("\nTotal assignments placed: " + total);

        List<String> shortages = new ArrayList<>();
        for (String d : DAYS) {
            for (String s : SHIFTS) {
                int c = schedule.get(d).get(s).size();
                if (c < MIN_PER_SHIFT) {
                    shortages.add(String.format("  %s %-10s -> %d/%d", d, s, c, MIN_PER_SHIFT));
                }
            }
        }
        if (shortages.isEmpty()) {
            System.out.println("\nAll shifts meet the minimum staffing requirement ✅");
        } else {
            System.out.println("\nShort-staffed shifts (below minimum):");
            shortages.forEach(System.out::println);
        }
    }
}
