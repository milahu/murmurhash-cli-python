{
  pkgs ? import <nixpkgs> {}
}:

let
  my-python = pkgs.python39;
  my-python-packages = python-packages: with python-packages; [

mmh3
murmurhash

  ]; 
  python-with-my-packages = my-python.withPackages my-python-packages;
in

python-with-my-packages.env
