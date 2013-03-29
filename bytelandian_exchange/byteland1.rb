
def byteland(coin)
  if coin == 0
    return 1
  else 
    return byteland(coin/2) + byteland(coin/3) + byteland(coin/4)
  end
end

puts byteland(7)
puts byteland(1000)
