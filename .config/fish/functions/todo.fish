# Defined in - @ line 1
function todo --wraps='vim ~/.todo' --description 'alias todo=vim ~/.todo'
  vim ~/.todo $argv;
end
