" The VimL/VimScript code is included in this sample plugin to demonstrate the
" two different approaches but it is not required you use VimL. Feel free to
" delete this code and proceed without it.
"
nnoremap <silent> <leader>x :call Selection()<CR>
nnoremap <silent> <leader>z :call Refacto()<CR>
nnoremap <silent> <leader>s :call SelectionRefacto()<CR>
