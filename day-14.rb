def readto_string_hash(path="./data/d14")
    data = File.open(path).read.split("\n")
    starter = data.shift
    data.shift

    insertion_rules = {}
    for idx in 0..(data.length() - 1)
        insertion_rules[data[idx][0..1]] = data[idx][6]
        idx += 1
    end

    return starter, insertion_rules
end


def part1and2(starter, insertion_rules, steps)
    monomer_counter = {}
    for idx in 0..(starter.length() - 1)
        if monomer_counter.key?(starter[idx])
            monomer_counter[starter[idx]] += 1
        else
            monomer_counter[starter[idx]] = 1
        end
    end

    polymer_counter = {}
    for idx in 0..(starter.length() - 2)
       if polymer_counter.key?("#{starter[idx]}#{starter[idx + 1]}")
        polymer_counter["#{starter[idx]}#{starter[idx + 1]}"] += 1
       else
        polymer_counter["#{starter[idx]}#{starter[idx + 1]}"] = 1
       end
    end

    for step in 1..steps
        tmp_counter = {}
        polymer_counter.each do |key, value|
            if tmp_counter.key?("#{key[0]}#{insertion_rules[key]}")
                tmp_counter["#{key[0]}#{insertion_rules[key]}"] += value
            else
                tmp_counter["#{key[0]}#{insertion_rules[key]}"] = value
            end
            if tmp_counter.key?("#{insertion_rules[key]}#{key[1]}")
                tmp_counter["#{insertion_rules[key]}#{key[1]}"] += value
            else
                tmp_counter["#{insertion_rules[key]}#{key[1]}"] = value
            end
            if monomer_counter.key?("#{insertion_rules[key]}")
                monomer_counter["#{insertion_rules[key]}"] += value
            else
                monomer_counter["#{insertion_rules[key]}"] = value
            end
        end
        polymer_counter = tmp_counter
    end

    answer = monomer_counter.values.minmax
    return (answer[1] - answer[0])
end


starter, insertion_rules = readto_string_hash
puts "Part 1: #{part1and2(starter, insertion_rules, 10)}"
puts "Part 2: #{part1and2(starter, insertion_rules, 40)}"
__END__
