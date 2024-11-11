from automat import Automat


def main():

    automat: Automat = Automat(5)
    
    print(automat)
    print()
    automat.włóż_monetę()
    automat.przekręć_gałkę()
    print()
    print(automat)
    print()
    automat.włóż_monetę()
    automat.zwróć_monetę()
    automat.przekręć_gałkę()
    print()
    print(automat)
    print()
    automat.włóż_monetę()
    automat.przekręć_gałkę()
    automat.włóż_monetę()
    automat.przekręć_gałkę()
    automat.zwróć_monetę()
    print()
    print(automat)
    print()
    automat.włóż_monetę()
    automat.włóż_monetę()
    automat.przekręć_gałkę()
    automat.włóż_monetę()
    automat.przekręć_gałkę()
    automat.włóż_monetę()
    automat.przekręć_gałkę()
    print()
    print(automat)

if __name__ == "__main__":
    main()