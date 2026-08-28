import { SkillGroup } from "@/types";

const skills: SkillGroup[] = [
  {
    title: "Programming",
    items: ["Python", "Golang", "TypeScript", "SQL", "HTML/CSS"],
  },
  {
    title: "Data & AI",
    items: [
      "Text Mining",
      "Machine Learning",
      "Naïve Bayes",
      "TF-IDF",
      "Data Analysis",
    ],
  },
  {
    title: "Tools & Systems",
    items: ["IT Support", "PostgreSQL", "Git", "Next.js", "FastAPI"],
  },
];

export default function Skills() {
  return (
    <section
      id="skills"
      className="max-w-5xl mx-auto px-6 py-20 border-t border-gray-800"
    >
      <h2 className="text-3xl font-bold mb-8">Skills</h2>
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {skills.map((group) => (
          <div
            key={group.title}
            className="bg-gray-900 border border-gray-800 rounded-xl p-6"
          >
            <h3 className="text-blue-400 font-semibold mb-4">{group.title}</h3>
            <div className="flex flex-wrap gap-2">
              {group.items.map((item) => (
                <span
                  key={item}
                  className="bg-gray-800 text-gray-300 text-sm px-3 py-1 rounded-full"
                >
                  {item}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
