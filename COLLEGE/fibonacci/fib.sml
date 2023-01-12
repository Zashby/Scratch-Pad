fun fibonacci n =
  if n < 3 then
    1
  else
    fibonacci (n-1) + fibonacci (n-2)

fun aux n =
  if n > 16 then
    print "\n"
  else (
    print (Int.toString (fibonacci n) ^ ", ");
    aux (n + 1)
  );
aux 1;

fun fibonacci () = 
   let
      fun fib(a,b) = Cons(a+b, fn() => fib(b,a+b))
   in
      Cons(0, fn()=> fib(0,1))
   end  