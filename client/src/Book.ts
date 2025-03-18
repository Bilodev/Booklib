export type status = 'finished' | 'to read' | 'paused' | 'reading' | null

export type bookBean = {
    id: string
    status: status
    // startDate: string | null
    // finishDate: string | null
};

export type Book = {
    id: string
    authors: string[]
    title: string
    description: string
    thumbnail: string
    publisher: string
    genres: string[]
}

export interface BookView extends Book {
    status: status
}
