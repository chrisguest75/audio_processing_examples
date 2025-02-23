# flake.nix
{
    description = "A flake for developing with python 3.11.8";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = {nixpkgs, ...}: let
    system = "x86_64-linux";
    #       ↑ Swap it for your system if needed
    #       "aarch64-linux" / "x86_64-darwin" / "aarch64-darwin"
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system}.default = pkgs.mkShell {

      packages = [ 
          pkgs.python311Full 
          pkgs.python311Packages.pip 
          pkgs.uv 
       ];

      env = {
        NIX_LD_LIBRARY_PATH = pkgs.lib.strings.makeLibraryPath [
          pkgs.stdenv.cc.cc
        ];
        NIX_LD = pkgs.lib.fileContents "${pkgs.stdenv.cc}/nix-support/dynamic-linker";
      };

      shellHook = ''
        echo "***************************************************"
        echo "*** Welcome to python (uv)"
        echo "***************************************************"
        echo ""
        python --version
        uv version
      '';       
    };
  };
}
