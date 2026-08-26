# [Explicação do algoritmo Wikipedia](https://pt.wikipedia.org/wiki/Crivo_de_Erat%C3%B3stenes)
Para exemplificá-lo, vamos determinar a lista de números entre 1 e 30.

- Inicialmente, determina-se o maior número a ser verificado. Ele corresponde à raiz quadrada do valor limite, arredondado para baixo. No caso, a raiz de 30, arredondada para baixo, é 5.
- Crie uma lista de todos os números inteiros de 2 até o valor limite, neste caso 30.
- Encontre o primeiro número da lista. Ele é um número primo, 2.
- Remova da lista todos os múltiplos de 2 (exceto ele próprio) até o valor limite. No nosso exemplo, a lista contem 2 e os números ímpares até 29.
- O próximo número da lista após o primo anterior é primo. Repita o procedimento. No caso, o próximo número da lista é 3. Removendo seus múltiplos, a lista fica: 2, 3, 5, 7, 11, 13, 17, 19, 23, 25 e 29. O próximo número, 5, também é primo; a lista fica: 2, 3, 5, 7, 11, 13, 17, 19, 23 e 29. 5 é o último número a ser verificado, conforme determinado inicialmente. Assim, a lista encontrada contém somente números primos.

Por <a href="//commons.wikimedia.org/w/index.php?title=User:M.qrius&amp;action=edit&amp;redlink=1" class="new" title="User:M.qrius (page does not exist)">M.qrius</a> - <span class="int-own-work" lang="pt">Obra do próprio</span>. Inspired on a similar picture by <a href="//commons.wikimedia.org/wiki/User:SKopp" title="User:SKopp">SKopp</a>., <a href="https://creativecommons.org/licenses/by-sa/4.0" title="Creative Commons Attribution-Share Alike 4.0">CC BY-SA 4.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=3287623">Hiperligação</a>
