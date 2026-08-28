import { Project } from "@/types";

const projects: Project[] = [
  {
    title: "Analisis Sentimen Rempang",
    desc: "Sistem klasifikasi sentimen opini publik terhadap relokasi penduduk Rempang menggunakan Naïve Bayes Classifier dan Text Mining. Akurasi 81%.",
    tags: ["Python", "Machine Learning", "NLP", "TF-IDF"],
    type: "Skripsi / Research",
  },
  {
    title: "Web Portofolio",
    desc: "Web portofolio pribadi dibangun dengan Next.js, Golang, dan Python. Full-stack modern dengan REST API dan layanan analisis data.",
    tags: ["Next.js", "Golang", "Python", "PostgreSQL"],
    type: "Web Development",
  },
];

export default function Projects() {
  return (
    <section
      id="projects"
      className="max-w-5xl mx-auto px-6 py-20 border-t border-gray-800"
    >
      <h2 className="text-3xl font-bold mb-8">Projects</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {projects.map((project) => (
          <div
            key={project.title}
            className="bg-gray-900 border border-gray-800 rounded-xl p-6 hover:border-blue-800 transition"
          >
            <span className="text-xs text-blue-400 font-medium">
              {project.type}
            </span>
            <h3 className="text-xl font-bold mt-2 mb-3">{project.title}</h3>
            <p className="text-gray-400 text-sm leading-relaxed mb-4">
              {project.desc}
            </p>
            <div className="flex flex-wrap gap-2">
              {project.tags.map((tag) => (
                <span
                  key={tag}
                  className="bg-gray-800 text-gray-400 text-xs px-2 py-1 rounded"
                >
                  {tag}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
