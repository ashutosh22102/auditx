Review data for Chapters 3 and 4 (OpenAlex search run on 22 October 2026).

query.json            exact OpenAlex filter used for the database search
records.jsonl         all 1,807 records retrieved (title, abstract, journal, DOI)
ta_final.json         title/abstract decision for each record (two independent
                      AI-assisted classifications, adjudicated where they differed)
agreement.json        agreement between the two screening passes (Cohen's kappa)
included_final.json   the 120 included studies: verified extraction, quality
                      ratings, evidence categories, and a verbatim quote for
                      every reported result
citation_search.json  counts from the citation search (678 records not screened)

Before submission, check the inclusion decisions and the quoted results against
the papers themselves, as Section 3.2.2 of the thesis states.
