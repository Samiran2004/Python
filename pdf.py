from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, '2023 Zoology Semester 1 Examination Questions', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 7, body)
        self.ln()

pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# --- Content Data ---

papers = {
    "Paper: ZCT-101 (Invertebrate Functional Forms and Adaptations)": [
        "1. (a) Draw and describe the feeding-digestive system of Cycliophorans.\n(b) What are 'Pandora larva' and 'Chordoid larva'?\n(c) Distinguish between Stoloniferous and Non-stoloniferous Ectoprocts.\n(d) How does lophophore regulate feeding in Ectoproct?",
        "2. (a) What were the food for the early metazoans in the ocean bottom? Highlight the adaptations that were necessary to feed.\n(b) Enumerate the major feeding modes among invertebrates.\n(c) Describe the major organs for suspension feeding in invertebrates with suitable illustration.",
        "3. (a) How do specialized cells determine the regenerative fate of cnidarians?\n(b) Explain why a Hydra can form the hypostome when it is cut at the anterior end.\n(c) Which is the most preferred type of regeneration in cnidarians and why?",
        "4. (a) Differentiate between Allomone and Kairomone in terms of their functions and chemical properties.\n(b) Define chemical mimicry in insects with suitable examples. Explain the phenomenon considering the role of cuticular hydrocarbons (CHC) in kin recognition and enemy identification.\n(c) Discuss how plant volatile compounds (VOC) and pheromone play significant role in insect-plant interaction.",
        "5. (a) How do the Magnus effect and Bernoulli's principle work together in the wing kinematics of insect flight?\n(b) Clarifying the three situations (1-3) shown in the figure (showing scutellar levers corresponding to three sequential states of an insect's wing posture), explain the flight-aerodynamics of insect considering the participation of associated muscles and wing elements.",
        "6. (a) Write about biogenic amines and their functions.\n(b) Define bioluminescence. Explain the bioluminescence mechanism in insects with suitable flow-diagram and mention its adaptive significances.\n(c) Qualitative 'song' is important for mating partner selection in insects-illustrate the opinion using song characters.",
        "7. (a) Discuss about the various forms of ventilation mechanisms observed in invertebrates with suitable diagram.\n(b) 'Gaseous exchanges are often affected by the body size and activities of the invertebrates.' Explain using suitable equation and graphical presentation.\n(c) Interpret the relation of partial pressure of oxygen as a factor influencing the respiration in invertebrates with suitable graphical presentation.",
        "8. (a) Prove that diapause in insect is a physiological state of dormancy.\n(b) Elaborate the role of neuroendocrine system in successful metamorphosis in insect using suitable flow diagram.\n(c) What do you mean by 'Token Stimuli'? Elaborate the role of different 'Token stimuli' in different processes of diapause."
    ],
    "Paper: ZCT-102 (Ecology)": [
        "1. (a) Explore 'net reproductive rate' and 'biotic potential', describing the quantitative estimation of each parameter. How do you perceive environmental resistance?\n(b) Derive the logistic equation dN/dt=rN(K-N/K) for deterministic population growth with suitable reasoning at each step. What are the assumptions to be considered for constructing such population growth model?",
        "2. (a) Explain recruitment function and Beverton-Holt model to prove that every population tends to converge at level K whenever it is lower than or greater than the carrying capacity of an environment.\n(b) How is the behaviour of each kind of population cycle evident in natural populations? Put up your explanations for such fluctuations.\n(c) How do the traits of opportunistic and equilibrium species differ as strategies of survival in contrasting environments? Expand your idea whether a transition from r selected strategy to k selected strategy is possible or not in the same species when exposed to competition as density dependent factor.",
        "3. (a) Describe the kind of abundance model you will expect to see in the species community on a volcanic island that is being populated afresh after a volcanic eruption.\n(b) Explain the term rarefaction. Differentiate between species accumulation curve and rarefaction curve.\n(c) With what different parameters you may measure the function of an ecosystem? 'An ecosystem keeps losing its decomposer species due to some reasons but still there is no change in the decomposition rate.' Explain this with a suitable diagram.",
        "4. (a) Differentiate between Eltonian and Grinellian specialization.\n(b) Why does a phylogenetic lineage become specialized, losing a past adaptive capacity in the process? Can you offer any hypothesis?\n(c) What may happen if (i) one habitat type were more common, and (ii) if fitnesses of two specialists greatly exceed the generalist in a coarse grained habitat?",
        "5. (a) How would you differentiate between an exotic species and an invasive species? What attributes make a species attain the status of an invasive species?\n(b) Outline 'Increased Competitive Ability Hypothesis' with a suitable example.\n(c) What factors contributed to Green Revolution in the country? Outline the problems that surfaced soon after.",
        "6. (a) 'Food webs can be represented in various forms' substantiate this statement with suitable illustrations. In what ways the information content of a typical food web different from a bipartite network?\n(b) Explain the terms (i) connectance and (ii) linkage density. Estimate the connectance of a food web comprising 10 species and the observed links is 30.\n(c) How is stability-complexity relationship interpreted using connectance, species richness and interaction strength as components?",
        "7. (a) 'Sponges and molluscs are suitable candidates for application for zooremediation' justify this statement using suitable examples. Distinguish between biostimulation and bioaugmentation as bioremediation strategies.\n(b) 'Manipulation of the plasmids in microbes can enhance bioremediation capacity'- substantiate this statement considering the superbug Pseudomonas putida as example.\n(c) Outline the principles of rhizofiltration as a bioremediation strategy.",
        "8. (a) With reference to the prey-predator interactions, outline the various forms of functional responses, using suitable diagrams. What are attack rate and handling time?\n(b) Elaborate prey switching as a mechanism that sustains predators in heterogenous environment with varying preferred prey availability.\n(c) Illustrate character displacement as a mechanism to reduce competitive interactions in co-occurring species."
    ],
    "Paper: ZCT-103 (Cell Biology)": [
        "1. (a) A student was treating liver cells with a drug 'X'. On analysis, the student discovered that the expressions of both proteins 'A' and 'B' had increased on treatment.\n   (i) How would the student elucidate if 'A' and 'B' worked in tandem?\n   (ii) In case one of the proteins stimulated the expression of the other protein, how would the student experimentally determine which protein was upstream of the other?\n(b) What is spectral shift? Explain with examples, the reasons behind dye diversity.\n(c) 'Rapid reorganization of the cytoskeleton is an essential feature of cell division.' Discuss the statement in brief.\n(d) What are the critical attributes of a plasma membrane?",
        "2. (a) How will you experimentally prove that SMAD-4 is important for both activation and inhibition of TGF-signalling pathways?\n(b) Write down the procedures of preparation of Carmine and Orcein from their natural sources.\n(c) Comment on the role of formin, ARP2/3 complex and gelsolin in actin polymerization.\n(d) What are lipid rafts? What functions do they play in cell signalling?",
        "3. (a) How does signalling take place in cells that are in apposition? Explain the involvement of enzymes in events downstream of ligand interaction.\n(b) State with example, the basis of nomenclature of dyes.\n(c) How do kinesin-13 and XMAP215 modulate microtubule dynamics in cells?\n(d) What are the post-translational modifications found in eukaryotic cells and why are they needed?",
        "4. (a) Lung cancer cells were exposed to compounds P, Q and R. Proteins were fractionated, followed by expression analyses. The results provided show expression levels for Grb2, SOS, Ras, pSTAT3, Cyclin D1, and B-tubulin. Explain the specific roles that P, Q and R play in modulating the lung cancer cells.\n(b) Write down the principle of metachromasia.\n(c) Briefly describe the structure of Goblet cells and Leydig interstitial cells. Why epithelial cells are considered to be polarized?\n(d) 'alpha and beta polypeptides heterogeneously combine to form the integrin superfamily.' - Explain with examples.",
        "5. (a) Indicate two ways in which phosphorylation of proteins on specific amino acids could lead to a cellular response.\n(b) State with example, the applications and tinctorial merits of the metachromatic stains.\n(c) How does loss of ALPL and SMPD3 function affect bone mineralization?\n(d) How do FACS and MACS help in cell separation?",
        "6. (a) Human liver cells were cultured in plates A and B containing media without serum. The proteins were isolated from the plates, one after 6 hours and the other after 24 hours. Proteins were subjected to western hybridization looking at Beclin 1, LC3-1/2, Bcl-2, Cleaved [Caspase], Cyclin D1, and B-tubulin.\n   (i) In which plate were cells cultured in absence of serum for 6 hours? Explain the results as observed with reasons.\n   (ii) Why did expression of the proteins change after 24 hours and what does it indicate, specifically with regard to the growth of the cells?\n(b) State the application of freezing microtome in histology.\n(c) Comment on the alterations in ECM of cells with age.\n(d) Explain with a flow diagram the process of endoplasmic reticulum-associated degradation (ERAD).",
        "7. (a) Explain briefly the effects of inhibiting GAP on the activities of Ras signalling pathway and downstream components.\n(b) In what ways do cytoplasmic receptors differ from cell surface receptors?\n(c) Briefly describe the process of intramembranous ossification with suitable diagram.\n(d) Compare and contrast amongst necrosis, apoptosis and anoikis in terms of onset and outcome.",
        "8. (a) 'Cyclic AMP and calcium are two major intracellular messenger molecules, arising from activation of a single receptor'. Explain the statement.\n(b) Distinguish between single and double bath mordanting.\n(c) 'Presence of glycosoaminoglycans in extracellular matrix of cartilages is important for function of cartilages.' - Justify. Why does an injury to hyaline cartilage heal much more slowly than a bone fracture?\n(d) How is protein structure determined using (i) chemical disruption and (ii) indirect visualization techniques?"
    ],
    "Paper: ZCT-104 (Genetics)": [
        "1. (a) Outline the major regulatory steps of the pathways utilized by a cell to produce nucleotides. Name the agents that facilitate the process of hybridization.\n(b) Elaborate how the HAT medium helps in hybrid cell selection.\n(c) With a schematic diagram describe the process of monoclonal antibody production using the hybridoma technology.",
        "2. (a) List the various types of DNA damage a cell may encounter.\n(b) Outline the process of base excision repair. Comment on its efficiency over the nucleotide excision mechanism.\n(c) Explain how a cell corrects mismatched DNA sequences arising from a faulty DNA replication.\n(d) Comment on the cause and symptoms of Fanconi anemia.",
        "3. (a) How is the Holliday model of homologous recombination different from the model put forward by Meselson-Radding?\n(b) Briefly explain the process of non-homologous recombination.\n(c) 'The resolution of a Holliday structure yields recombinants and patch recombinant products.' - Explain.\n(d) Outline the cascades of events occurring during meiotic recombination in human.",
        "4. (a) An irradiation experiment caused an inversion that placed the w locus next to the centromere. What phenotypic change do you expect to occur in the flies? Why?\n(b) How does an euchromatic segment located next to a heterochromatic segment maintain its function?\n(c) 'Histone methylation can be either transcription activating or repressing signal.' - Justify the statement.\n(d) What is histone code?\n(e) Comment on types and functions of methyl transferase.",
        "5. (a) 'XIST cannot act alone, it needs a companion to execute its function.' - Justify the statement with a proper illustration.\n(b) How the transcription status of XIST is regulated by lncRNAs?\n(c) Mammalian X-linked genes that escape inactivation show different spatial chromatin arrangement. - Explain.\n(d) Narrate salient features of the Ac-Ds element.",
        "6. (a) What component of DCC in Drosophila shows disruption of its function on the removal of one Zn ion from its 'C'-terminus? Briefly narrate the processing of messages that encode this product in the male and female sex of Drosophila melanogaster.\n(b) 'Molecular chaperones regulate histone turn-over in replication.' How?\n(c) How Pol-II CTD phosphorylations are important in eukaryotic transcription?",
        "7. (a) What is charged tRNA? What is the implication of charged tRNA in the eukaryotic translation process?\n(b) What is 'translation initiation complex'? With suitable illustrations elucidate the role of factors in the translation initiation process.\n(c) What is Wobble base pairing?",
        "8. (a) 'Continuous phosphorylation and de-phosphorylation of proteins dictate the cellular transition from G2-M-G1 phase of cell cycle'. Elaborate with a suitable diagram.\n(b) What are Licensing factors? Describe the mode of action of the positive and negative Licensing factors with suitable examples.\n(c) 'Ubiquitin-proteasome system is an important regulator of cell cycle control.' - Justify the statement with a suitable illustration."
    ]
}

# --- PDF Generation Loop ---

for paper_title, questions in papers.items():
    pdf.chapter_title(paper_title)
    for q in questions:
        pdf.chapter_body(q)

pdf.output("Zoology_Questions_2023.pdf")
print("PDF generated successfully: Zoology_Questions_2023.pdf")