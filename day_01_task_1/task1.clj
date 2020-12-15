(use 'clojure.java.io)

(defn readfile [file_name]
    (map read-string
        (with-open [rdr (reader file_name)]
            (binding [*in* rdr] (doall (line-seq rdr))))))

(defn generate_all_pairs [numbers]
    (for [x numbers
          y numbers]
    [x y]))

(defn calc_product_of_good_pairs [pairs]
        (for [pair pairs
              :let [sum (apply + pair)]
              :when (= sum 2020)
             ]
             (apply * pair)))


(calc_product_of_good_pairs (generate_all_pairs (readfile "/home/fuszti/workspace/advent_of_code_2020/day_01_task_1/input.txt")))

