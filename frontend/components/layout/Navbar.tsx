export default function Navbar() {
  return (
    <nav className="fixed top-0 w-full bg-gray-950/80 backdrop-blur-sm border-b border-gray-800 z-50">
      <div className="max-w-5xl mx-auto px-6 py-4 flex justify-between items-center">
        <span className="font-bold text-blue-400 text-lg">Muhammad Taufiq</span>
        <div className="flex gap-6 text-sm text-gray-400">
          <a href="#about" className="hover:text-white transition">
            About
          </a>
          <a href="#skills" className="hover:text-white transition">
            Skills
          </a>
          <a href="#projects" className="hover:text-white transition">
            Projects
          </a>
          <a href="#contact" className="hover:text-white transition">
            Contact
          </a>
        </div>
      </div>
    </nav>
  );
}
