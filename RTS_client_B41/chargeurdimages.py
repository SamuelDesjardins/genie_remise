# changer pour changeurdimages

from tkinter import PhotoImage
    # toutes les images devraient �tre ins�r�es ici    
def chargerimages():
    images={
            'javelotGH':PhotoImage(file='./images/divers/javelotGH.png'),
            'javelotGB':PhotoImage(file='./images/divers/javelotGB.png'),
            'javelotDH':PhotoImage(file='./images/divers/javelotDH.png'),
            'javelotDB':PhotoImage(file='./images/divers/javelotDB.png'),
            'cerfD':PhotoImage(file='./images/animal/cerfD.png'),
            'cerfD':PhotoImage(file='./images/animal/cerfD.png'),
            'cerfG':PhotoImage(file='./images/animal/cerfG.png'),
            'cheval':PhotoImage(file='./images/animal/cheval.png'),
            'chevalG':PhotoImage(file='./images/animal/chevalG.png'),
            'daimMORT':PhotoImage(file='./images/animal/daimMORT.png'),
            'daimDB':PhotoImage(file='./images/animal/daimDB.png'),
            'daimDH':PhotoImage(file='./images/animal/daimDH.png'),
            'daimGB':PhotoImage(file='./images/animal/daimGB.png'),
            'daimGH':PhotoImage(file='./images/animal/daimGH.png'),
            
            #animaux maison par sam------------------------------
            'oursDB':PhotoImage(file='./images/animal/oursDB.png'),
            'oursDH':PhotoImage(file='./images/animal/oursDH.png'),
            'oursGB':PhotoImage(file='./images/animal/oursGB.png'),
            'oursGH':PhotoImage(file='./images/animal/oursGH.png'),
            'oursMORT':PhotoImage(file='./images/animal/oursMORT.png'),
            
            'cochonD':PhotoImage(file='./images/animal/cochonD.png'),
            'cochonG':PhotoImage(file='./images/animal/cochonG.png'),
            'cochonMORT':PhotoImage(file='./images/animal/cochonMORT.png'),
            
            'bouG':PhotoImage(file='./images/animal/bouG.png'),
            'bouD':PhotoImage(file='./images/animal/bouD.png'),
            'bouMORT':PhotoImage(file='./images/animal/bouMORT.png'),
            #---------------------------------------------------
            
            'ours60_db':PhotoImage(file='./images/animal/ours60_db.png'),
            'ours60_dh':PhotoImage(file='./images/animal/ours60_dh.png'),
            'ours60_gb':PhotoImage(file='./images/animal/ours60_gb.png'),
            'ours60_gh':PhotoImage(file='./images/animal/ours60_gh.png'),
            'arbre0grand':PhotoImage(file='./images/arbre/arbre0grand.png'),
            'arbre0petit':PhotoImage(file='./images/arbre/arbre0petit.png'),
            'arbre1grand':PhotoImage(file='./images/arbre/arbre1grand.png'),
            'arbre2grand':PhotoImage(file='./images/arbre/arbre2grand.png'),
            'arbresapin0grand':PhotoImage(file='./images/arbre/arbresapin0grand.png'),
            'arbresapin0petit':PhotoImage(file='./images/arbre/arbresapin0petit.png'),
            'baiegrand':PhotoImage(file='./images/arbuste/arbustebaiesgrand.png'),
            'baiepetit':PhotoImage(file='./images/arbuste/arbustebaiespetit.png'),
            'baievert':PhotoImage(file='./images/arbuste/arbustevert.png'),
            'aureusbrillant':PhotoImage(file='./images/aureus/aureusbrillant.png'),
            'aureusD_':PhotoImage(file='./images/aureus/aureusD_.png'),
            'aureusG':PhotoImage(file='./images/aureus/aureusG.png'),
            'aureusrocgrand':PhotoImage(file='./images/aureus/aureusrocgrand.png'),
            'aureusrocmoyen':PhotoImage(file='./images/aureus/aureusrocmoyen.png'),
            'aureusrocpetit':PhotoImage(file='./images/aureus/aureusrocpetit.png'),
            'B_abri':PhotoImage(file='./images/bleu/B_abri.png'),
            'B_archerD':PhotoImage(file='./images/bleu/B_archerD.png'),
            'B_archerG':PhotoImage(file='./images/bleu/B_archerG.png'),
            'B_caserne':PhotoImage(file='./images/bleu/B_caserne.png'),
            'B_chevalierD':PhotoImage(file='./images/bleu/B_chevalierD.png'),
            'B_chevalierG':PhotoImage(file='./images/bleu/B_chevalierG.png'),
            'B_druideD':PhotoImage(file='./images/bleu/B_druideD.png'),
            'B_druideG':PhotoImage(file='./images/bleu/B_druideG.png'),
            'B_maison':PhotoImage(file='./images/bleu/B_maison.png'),
            'B_mine':PhotoImage(file='./images/bleu/B_mine.png'),
            'B_moulin':PhotoImage(file='./images/bleu/B_moulin.png'),
            'B_ouvrierD':PhotoImage(file='./images/bleu/B_ouvrierD.png'),
            'B_ouvrierG':PhotoImage(file='./images/bleu/B_ouvrierG.png'),
            'B_soldatD':PhotoImage(file='./images/bleu/B_soldatD.png'),
            'B_soldatG':PhotoImage(file='./images/bleu/B_soldatG.png'),
            'gazonfond':PhotoImage(file='./images/divers/gazonfond.png'),
            'quaiD':PhotoImage(file='./images/divers/quaiD.png'),
            'quaiG':PhotoImage(file='./images/divers/quaiG.png'),
            'eau':PhotoImage(file='./images/eau/eau.png'),
            'eaugrand':PhotoImage(file='./images/eau/eaugrand.png'),
            'eaugrand1':PhotoImage(file='./images/eau/eaugrand1.png'),
            'eaugrand2':PhotoImage(file='./images/eau/eaugrand2.png'),
            'eaugrand3':PhotoImage(file='./images/eau/eaugrand3.png'),
            'eaujoncD':PhotoImage(file='./images/eau/eaujoncD.png'),
            'eaujoncG':PhotoImage(file='./images/eau/eaujoncG.png'),
            'eaumoyen':PhotoImage(file='./images/eau/eaumoyen.png'),
            'eaupetit':PhotoImage(file='./images/eau/eaupetit.png'),
            'eauquenouillesD':PhotoImage(file='./images/eau/eauquenouillesD.png'),
            'eauquenouillesG':PhotoImage(file='./images/eau/eauquenouillesG.png'),
            'eauquenouillesgrand':PhotoImage(file='./images/eau/eauquenouillesgrand.png'),
            'eautourbillon':PhotoImage(file='./images/eau/eautourbillon.png'),
            'eautroncs':PhotoImage(file='./images/eau/eautroncs.png'),
            'culturegrand':PhotoImage(file='./images/ferme/culturegrand.png'),
            'culturemoyen':PhotoImage(file='./images/ferme/culturemoyen.png'),
            'culturepetit':PhotoImage(file='./images/ferme/culturepetit.png'),
            'J_abri':PhotoImage(file='./images/jaune/J_abri.png'),
            'J_archeG':PhotoImage(file='./images/jaune/J_archeG.png'),
            'J_archerD':PhotoImage(file='./images/jaune/J_archerD.png'),
            'J_caserne':PhotoImage(file='./images/jaune/J_caserne.png'),
            'J_chevalierD':PhotoImage(file='./images/jaune/J_chevalierD.png'),
            'J_chevalierG':PhotoImage(file='./images/jaune/J_chevalierG.png'),
            'J_druideD':PhotoImage(file='./images/jaune/J_druideD.png'),
            'J_druideG':PhotoImage(file='./images/jaune/J_druideG.png'),
            'J_maison':PhotoImage(file='./images/jaune/J_maison.png'),
            'J_mine':PhotoImage(file='./images/jaune/J_mine.png'),
            'J_moulin':PhotoImage(file='./images/jaune/J_moulin.png'),
            'J_ouvrierD':PhotoImage(file='./images/jaune/J_ouvrierD.png'),
            'J_ouvrierG':PhotoImage(file='./images/jaune/J_ouvrierG.png'),
            'J_soldatD':PhotoImage(file='./images/jaune/J_soldatD.png'),
            'J_soldatG':PhotoImage(file='./images/jaune/J_soldatG.png'),
            'marais1':PhotoImage(file='./images/marais/marais1.png'),
            'marais2':PhotoImage(file='./images/marais/marais2.png'),
            'marais3':PhotoImage(file='./images/marais/marais3.png'),

            'V_tour':PhotoImage(file='./images/xxxbatiment/144_batiment-04.png'),

            'B_tour':PhotoImage(file='./images/xxxbatiment/144_batiment-04.png'),
            'R_tour':PhotoImage(file='./images/xxxbatiment/144_batiment-04.png'),
            'J_tour':PhotoImage(file='./images/xxxbatiment/144_batiment-04.png'),
            'V_scerie':PhotoImage(file='./images/xxxbatiment/144_scerie.png'),
            'B_scerie':PhotoImage(file='./images/xxxbatiment/144_scerie.png'),
            'R_scerie':PhotoImage(file='./images/xxxbatiment/144_scerie.png'),
            'J_scerie':PhotoImage(file='./images/xxxbatiment/144_scerie.png'),
            'roches1 grand':PhotoImage(file='./images/roche/roches1 grand.png'),
            'roches1petit':PhotoImage(file='./images/roche/roches1petit.png'),
            'roches2grand':PhotoImage(file='./images/roche/roches2grand.png'),
            'roches2petit':PhotoImage(file='./images/roche/roches2petit.png'),
            'roches3grand':PhotoImage(file='./images/roche/roches3grand.png'),
            'roches3petit':PhotoImage(file='./images/roche/roches3petit.png'),
            'roches4grand':PhotoImage(file='./images/roche/roches4grand.png'),
            'roches4petit':PhotoImage(file='./images/roche/roches4petit.png'),
            'roches5grand':PhotoImage(file='./images/roche/roches5grand.png'),
            'R_abri':PhotoImage(file='./images/rouge/R_abri.png'),
            'R_archerD':PhotoImage(file='./images/rouge/R_archerD.png'),
            'R_archerG':PhotoImage(file='./images/rouge/R_archerG.png'),
            'R_caserne':PhotoImage(file='./images/rouge/R_caserne.png'),
            'R_chevalierD':PhotoImage(file='./images/rouge/R_chevalierD.png'),
            'R_chevalierG':PhotoImage(file='./images/rouge/R_chevalierG.png'),
            'R_druideD':PhotoImage(file='./images/rouge/R_druideD.png'),
            'R_druideG':PhotoImage(file='./images/rouge/R_druideG.png'),
            'R_maison':PhotoImage(file='./images/rouge/R_maison.png'),
            'R_mine':PhotoImage(file='./images/rouge/R_mine.png'),
            'R_moulin':PhotoImage(file='./images/rouge/R_moulin.png'),
            'R_ouvrierD':PhotoImage(file='./images/rouge/R_ouvrierD.png'),
            'R_ouvrierG':PhotoImage(file='./images/rouge/R_ouvrierG.png'),
            'R_soldatD':PhotoImage(file='./images/rouge/R_soldatD.png'),
            'R_soldatG':PhotoImage(file='./images/rouge/R_soldatG.png'),
            'V_abri':PhotoImage(file='./images/vert/V_abri.png'),
            'V_archerD':PhotoImage(file='./images/vert/V_archerD.png'),
            'V_archerG':PhotoImage(file='./images/vert/V_archerG.png'),
            'V_caserne':PhotoImage(file='./images/vert/V_caserne.png'),
            'V_chevalierD':PhotoImage(file='./images/vert/V_chevalierD.png'),
            'V_chevalierG':PhotoImage(file='./images/vert/V_chevalierG.png'),
            'V_druideD':PhotoImage(file='./images/vert/V_druideD.png'),
            'V_druideG':PhotoImage(file='./images/vert/V_druideG.png'),
            'V_maison':PhotoImage(file='./images/vert/V_maison.png'),
            'V_mine':PhotoImage(file='./images/vert/V_mine.png'),
            'V_moulin':PhotoImage(file='./images/vert/V_moulin.png'),
            'V_ouvrierD':PhotoImage(file='./images/vert/V_ouvrierD.png'),
            'V_ouvrierG':PhotoImage(file='./images/vert/V_ouvrierG.png'),
            'V_soldatD':PhotoImage(file='./images/vert/V_soldatD.png'),
            'V_soldatG':PhotoImage(file='./images/vert/V_soldatG.png')
            }
    return images

def chargergif():
    gifs={}
    allgifs=["poissons.gif"]
    for nom in allgifs:
        listeimg=[]
        tempo=1
        no=1
        while no:
            try:
                img=PhotoImage(file='./images/gifs/'+nom,format="gif -index "+str(no))
                listeimg.append(img)
                no+=1
            except Exception:
                gifs[nom[:-4]]=listeimg
                no=0
    print("gifs",gifs)
    return gifs
