export interface Project {
  title: string;
  desc: string;
  tags: string[];
  type: string;
}

export interface SkillGroup {
  title: string;
  items: string[];
}

export interface ContactInfo {
  label: string;
  value: string;
}
