export default function Contact() {
  return (
    <section
      id="contact"
      className="max-w-5xl mx-auto px-6 py-20 border-t border-gray-800"
    >
      <h2 className="text-3xl font-bold mb-4">Contact</h2>
      <p className="text-gray-400 mb-8">
        Tertarik untuk bekerja sama atau punya pertanyaan? Hubungi saya!
      </p>
      <div className="flex flex-col sm:flex-row gap-4">
        <a
          href="mailto:mhdtaufiq.work@gmail.com"
          className="bg-blue-600 hover:bg-blue-500 px-6 py-3 rounded-lg font-medium transition text-center"
        >
          mhdtaufiq.work@gmail.com
        </a>
        <a
          href="https://linkedin.com/in/mhdtaufiq28"
          target="_blank"
          className="border border-gray-700 hover:border-blue-600 px-6 py-3 rounded-lg font-medium transition text-center"
        >
          LinkedIn
        </a>
      </div>
    </section>
  );
}
