import { ContactInfo } from "@/types";

const info: ContactInfo[] = [
  { label: "Lokasi", value: "Batam, Kepulauan Riau" },
  { label: "Email", value: "mhdtaufiq.work@gmail.com" },
  { label: "LinkedIn", value: "linkedin.com/in/mhdtaufiq28" },
  { label: "Status", value: "Open to work" },
];

export default function About() {
  return (
    <section
      id="about"
      className="max-w-5xl mx-auto px-6 py-20 border-t border-gray-800"
    >
      <h2 className="text-3xl font-bold mb-8">About Me</h2>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-10">
        <div>
          <p className="text-gray-400 leading-relaxed mb-4">
            Saya adalah fresh graduate S1 Teknik Informatika dari UIN Sultan
            Syarif Kasim Riau (IPK 3.16) yang aktif mengembangkan diri di bidang
            IT Support dan pengembangan web.
          </p>
          <p className="text-gray-400 leading-relaxed">
            Penelitian skripsi saya berfokus pada Analisis Sentimen Masyarakat
            terhadap Relokasi Penduduk Rempang menggunakan Text Mining dan Naïve
            Bayes Classifier — mencapai akurasi 81%.
          </p>
        </div>
        <div className="space-y-3">
          {info.map(({ label, value }) => (
            <div key={label} className="flex gap-3">
              <span className="text-blue-400 w-24 shrink-0">{label}</span>
              <span className="text-gray-300">{value}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
