i = 1;
j = 1;

    for(i=0:150)
     fib = i + j;
     i = j;
     j = fib;
     if(fib > 150)
     clear i;
     clear j;
     clear fib;
     break;
     endif
     disp(fib)
endfor
