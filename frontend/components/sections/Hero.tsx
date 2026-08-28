export default function Hero() {
  return (
    <section className="max-w-5xl mx-auto px-6 pt-40 pb-24">
      <p className="text-blue-400 text-sm font-medium mb-3">Hi, saya</p>
      <h1 className="text-5xl font-bold mb-4">Muhammad Taufiq</h1>
      <h2 className="text-2xl text-gray-400 mb-6">
        IT Support & Software Developer
      </h2>
      <p className="text-gray-400 max-w-xl leading-relaxed mb-8">
        Lulusan S1 Teknik Informatika dengan keahlian di bidang IT Support,
        analisis data, dan pengembangan sistem. Peneliti Text Mining & Machine
        Learning berbasis Python.
      </p>
      <div className="flex gap-4">
        <a
          href="#projects"
          className="bg-blue-600 hover:bg-blue-500 px-6 py-3 rounded-lg font-medium transition"
        >
          Lihat Proyek
        </a>
        <a
          href="#contact"
          className="border border-gray-700 hover:border-gray-500 px-6 py-3 rounded-lg font-medium transition"
        >
          Hubungi Saya
        </a>
      </div>
    </section>
  );
}
