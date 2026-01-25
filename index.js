random_str = "abc123xyz";

const split_str = (str) => {
  let double_chars = "";
  let final_result = [];

  if (str.length % 2 != 0) {
    str += "_";
  }

  for (let i = 0; i < str.length; i += 2) {
    double_chars = str.substring(i, i + 2);
    final_result.push(double_chars);
  }

//   while (i < str.length) {
//     double_chars = str.substring(i, i + 2);
//     console.log(double_chars);
//     final_result.push(double_chars);
//     i += 2;
//   }
  console.log(final_result);
};

split_str(random_str);
