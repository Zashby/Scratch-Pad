## Copyright (C) 2022 bored
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <https://www.gnu.org/licenses/>.

## -*- texinfo -*-
## @deftypefn {} {@var{retval} =} fib (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: bored <bored@DESKTOP-UH8LQEQ>
## Created: 2022-10-06

function retval = fib (input1, input2)
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
endfunction

fib()
