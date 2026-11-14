(() => {
  "use strict";

  const REPO_RAW = "https://raw.githubusercontent.com/avasinim/KejyarBot/release/main-based-reconciled-2026-11-11/";
  const DATA = "course_data/";
  const $ = (selector) => document.querySelector(selector);
  const courseListEl = $("#course-list");
  const lessonNavEl = $("#lesson-nav");
  const lessonContentEl = $("#lesson-content");
  const courseOverviewEl = $("#course-overview");
  const courseSearchEl = $("#course-search");
  const progressKey = "kejyar-learning-progress-v1";

  let courses = [];
  let courseData = new Map();
  let selectedCourse = null;
  let selectedLesson = null;
  let progress = readProgress();

  function readProgress() {
    try {
      const value = JSON.parse(localStorage.getItem(progressKey) || "{}");
      return value && typeof value === "object" ? value : {};
    } catch (_) {
      return {};
    }
  }

  function saveProgress() {
    try { localStorage.setItem(progressKey, JSON.stringify(progress)); }
    catch (_) { /* Private browsing or full storage: the lesson remains readable. */ }
  }

  function completedSet(courseId) {
    return new Set(Array.isArray(progress[courseId]) ? progress[courseId] : []);
  }

  async function fetchJson(path) {
    const response = await fetch(REPO_RAW + path, { cache: "no-cache" });
    if (!response.ok) throw new Error("بارکردنی سەرچاوە سەرکەوتوو نەبوو: " + path);
    return response.json();
  }

  async function fetchText(path) {
    const response = await fetch(REPO_RAW + path, { cache: "no-cache" });
    if (!response.ok) throw new Error("بارکردنی سەرچاوە سەرکەوتوو نەبوو: " + path);
    return response.text();
  }

  function escapeText(value) {
    return String(value ?? "");
  }

  function addText(parent, tag, text, className) {
    const node = document.createElement(tag);
    node.textContent = escapeText(text);
    if (className) node.className = className;
    parent.appendChild(node);
    return node;
  }

  function inlineMarkdown(parent, source) {
    const pattern = /(\*\*[^*]+\*\*|`[^`]+`|\*[^*]+\*)/g;
    let last = 0;
    const text = String(source ?? "");
    for (const match of text.matchAll(pattern)) {
      if (match.index > last) parent.appendChild(document.createTextNode(text.slice(last, match.index)));
      const token = match[0];
      let node;
      if (token.startsWith("**")) {
        node = document.createElement("strong");
        node.textContent = token.slice(2, -2);
      } else if (token.startsWith("`")) {
        node = document.createElement("code");
        node.textContent = token.slice(1, -1);
      } else {
        node = document.createElement("em");
        node.textContent = token.slice(1, -1);
      }
      parent.appendChild(node);
      last = match.index + token.length;
    }
    if (last < text.length) parent.appendChild(document.createTextNode(text.slice(last)));
  }

  function renderMarkdown(parent, markdown) {
    const lines = String(markdown ?? "").replace(/\r/g, "").split("\n");
    let i = 0;
    while (i < lines.length) {
      const line = lines[i].trim();
      if (!line) { i++; continue; }
      if (/^(---+|\*{3,}|_{3,})$/.test(line)) {
        parent.appendChild(document.createElement("hr")); i++; continue;
      }
      const heading = /^(#{1,4})\s+(.+)$/.exec(line);
      if (heading) {
        addInlineHeading(parent, "h" + Math.min(heading[1].length + 1, 4), heading[2]);
        i++; continue;
      }
      if (line.startsWith("|") && line.endsWith("|")) {
        const rows = [];
        while (i < lines.length && lines[i].trim().startsWith("|") && lines[i].trim().endsWith("|")) {
          const cells = lines[i].trim().replace(/^\|/, "").replace(/\|$/, "").split("|").map(x => x.trim());
          if (!cells.every(x => /^:?-{3,}:?$/.test(x.replace(/\s/g, "")))) rows.push(cells);
          i++;
        }
        if (rows.length) {
          const table = document.createElement("table");
          rows.forEach((row, index) => {
            const tr = document.createElement("tr");
            row.forEach(cell => {
              const td = document.createElement(index === 0 ? "th" : "td");
              inlineMarkdown(td, cell);
              tr.appendChild(td);
            });
            table.appendChild(tr);
          });
          parent.appendChild(table);
        }
        continue;
      }
      if (line.startsWith(">")) {
        const quote = document.createElement("blockquote");
        while (i < lines.length && lines[i].trim().startsWith(">")) {
          const p = document.createElement("p");
          inlineMarkdown(p, lines[i].trim().replace(/^>\s?/, ""));
          quote.appendChild(p); i++;
        }
        parent.appendChild(quote); continue;
      }
      if (/^[-*]\s+/.test(line)) {
        const list = document.createElement("ul");
        while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) {
          const li = document.createElement("li");
          inlineMarkdown(li, lines[i].replace(/^\s*[-*]\s+/, ""));
          list.appendChild(li); i++;
        }
        parent.appendChild(list); continue;
      }
      if (/^\d+[.)]\s+/.test(line)) {
        const list = document.createElement("ol");
        while (i < lines.length && /^\s*\d+[.)]\s+/.test(lines[i])) {
          const li = document.createElement("li");
          inlineMarkdown(li, lines[i].replace(/^\s*\d+[.)]\s+/, ""));
          list.appendChild(li); i++;
        }
        parent.appendChild(list); continue;
      }
      const p = document.createElement("p");
      inlineMarkdown(p, line);
      parent.appendChild(p);
      i++;
    }
  }

  function addInlineHeading(parent, tag, text) {
    const node = document.createElement(tag);
    inlineMarkdown(node, text);
    parent.appendChild(node);
  }

  function addSection(parent, title, value) {
    if (value === undefined || value === null || value === "" || (Array.isArray(value) && !value.length)) return;
    addText(parent, "h2", title);
    if (typeof value === "string") {
      const p = document.createElement("p"); inlineMarkdown(p, value); parent.appendChild(p); return;
    }
    if (Array.isArray(value)) {
      const list = document.createElement("ul");
      value.forEach(item => {
        const li = document.createElement("li");
        if (Array.isArray(item)) {
          item.forEach((part, index) => {
            if (index) li.appendChild(document.createTextNode(" — "));
            li.appendChild(document.createTextNode(escapeText(part)));
          });
        } else if (item && typeof item === "object") {
          li.textContent = Object.entries(item).map(([k,v]) => k + ": " + v).join(" · ");
        } else {
          inlineMarkdown(li, item);
        }
        list.appendChild(li);
      });
      parent.appendChild(list);
      return;
    }
    if (typeof value === "object") {
      Object.entries(value).forEach(([key, item]) => {
        const p = document.createElement("p");
        const strong = document.createElement("strong"); strong.textContent = key + ": ";
        p.appendChild(strong); p.appendChild(document.createTextNode(escapeText(item)));
        parent.appendChild(p);
      });
    }
  }

  function formatStatus(status) {
    if (status === "draft_editorial_review" || status === "draft_for_review") return "ڕەشنووسی پێداچوونەوە";
    if (status === "scientific_review_complete_with_qualified_notes") return "پشکنینی زانستی تەواوە، بە تێبینی";
    if (status === "internal_cross_lesson_synthesis_no_external_source_mapping") return "پێداچوونەوەی ناوخۆیی";
    if (status === "owner_review_pending_expanded_draft") return "چاوەڕوانی پێداچوونەوەی خاوەندار";
    if (status === "source_review_pending") return "چاوەڕوانی پێداچوونەوەی سەرچاوە";
    if (status.includes("source_received")) return "سەرچاوە وەرگیراو و پارێزراو";
    return status;
  }

  function renderStructured(parent, lesson, courseId) {
    if (courseId === "grammar" && lesson.source_markdown) {
      renderMarkdown(parent, lesson.source_markdown);
      return;
    }
    addSection(parent, "🎯 ئامانج", lesson.objective);
    if (lesson.dialogue) {
      addText(parent, "h2", "🗣️ گفتوگۆ");
      const dialogue = document.createElement("div");
      dialogue.className = "dialogue";
      lesson.dialogue.forEach(turn => {
        const p = document.createElement("p");
        const speaker = document.createElement("strong");
        speaker.textContent = escapeText(turn[0]) + ": ";
        p.appendChild(speaker);
        p.appendChild(document.createTextNode(escapeText(turn[1])));
        dialogue.appendChild(p);
      });
      parent.appendChild(dialogue);
    }
    addSection(parent, "🔎 خاڵە سەرەکییەکان", lesson.key_points);
    addSection(parent, "📚 وشە و دەستەواژە", lesson.vocabulary);
    addSection(parent, "✍️ نموونەکان", lesson.examples);
    addSection(parent, "📎 پاشکۆ", lesson.appendix);
    addSection(parent, "🎯 چالاکییەکان", lesson.activities);
    addSection(parent, "✍️ ڕاهێنان", lesson.exercises);
    addSection(parent, "🧠 پرسیارەکانی تێگەیشتن", lesson.comprehension);
    addSection(parent, "🎭 ڕۆڵگێڕی / کاری پڕاکتیکی", lesson.role_play);
  }

  function renderAramiJson(parent, payload) {
    addSection(parent, "🎯 ئامانجەکان", payload.objectives);
    if (Array.isArray(payload.sections)) {
      payload.sections.forEach((section, index) => {
        addText(parent, "h2", section.title || ("بەشی " + (index + 1)));
        if (section.body) renderMarkdown(parent, section.body);
        if (section.content) renderMarkdown(parent, section.content);
        if (section.text) renderMarkdown(parent, section.text);
        if (Array.isArray(section.table)) {
          const table = document.createElement("table");
          section.table.forEach((row, rowIndex) => {
            const tr = document.createElement("tr");
            row.forEach(cell => addText(tr, rowIndex === 0 ? "th" : "td", cell));
            table.appendChild(tr);
          });
          parent.appendChild(table);
        }
        if (section.note) addText(parent, "p", section.note, "muted");
        if (section.points) addSection(parent, "خاڵە سەرەکییەکان", section.points);
        if (section.examples) addSection(parent, "نموونەکان", section.examples);
      });
    }
    addSection(parent, "کۆتایی", payload.conclusion);
  }

  function normalizeQuiz(lesson, courseId) {
    const items = Array.isArray(lesson.quiz) ? lesson.quiz : [];
    return items.map(item => ({
      question: item.q ?? item.question ?? "",
      options: item.options ?? [],
      answer: Number.isInteger(item.answer) ? item.answer :
        (Number.isInteger(item.answer_index) ? item.answer_index : (item.options || []).indexOf(item.answer)),
      explanation: item.explanation || ""
    }));
  }

  function renderQuiz(parent, quiz) {
    const usable = quiz.filter(q => q.question && Array.isArray(q.options) && q.options.length > 1 && q.answer >= 0 && q.answer < q.options.length);
    if (!usable.length) return;
    const box = document.createElement("section");
    box.className = "quiz-box";
    addText(box, "h2", "🧠 تاقیکردنەوەی خۆت");
    usable.forEach((q, index) => {
      const question = document.createElement("div");
      question.className = "quiz-question";
      addText(question, "p", (index + 1) + ". " + q.question);
      const feedback = document.createElement("div");
      feedback.className = "quiz-feedback";
      q.options.forEach((option, optionIndex) => {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "quiz-option";
        button.textContent = option;
        button.addEventListener("click", () => {
          question.querySelectorAll("button").forEach(b => { b.disabled = true; });
          if (optionIndex === q.answer) {
            button.classList.add("correct");
            feedback.textContent = "✓ ڕاستە. " + q.explanation;
          } else {
            button.classList.add("wrong");
            question.querySelectorAll("button")[q.answer]?.classList.add("correct");
            feedback.textContent = "وەڵامی ڕاست: " + q.options[q.answer] + (q.explanation ? " — " + q.explanation : "");
          }
        });
        question.appendChild(button);
      });
      question.appendChild(feedback);
      box.appendChild(question);
    });
    parent.appendChild(box);
  }

  async function loadAllData() {
    const [courseManifest, aramiManifest, dailyA, dailyB, dailyC, dailyD, unified, grammar, grammarOverrides, latinManifest, latin1, latin2] = await Promise.all([
      fetchJson("courses.json"),
      fetchJson(DATA + "arami_course1_manifest.json"),
      fetchJson(DATA + "daily_conversation_lessons_01_06.json"),
      fetchJson(DATA + "daily_conversation_lessons_07_30.json"),
      fetchJson(DATA + "daily_conversation_lessons_31_36.json"),
      fetchJson(DATA + "daily_conversation_lessons_37_42.json"),
      fetchJson(DATA + "unified_orthography_lessons_01_66.json"),
      fetchJson(DATA + "grammar_course4_lessons.json"),
      fetchJson(DATA + "grammar_course4_quiz_overrides.json"),
      fetchJson(DATA + "latin_courses_manifest_draft.json"),
      fetchText(DATA + "latin_course_1_source_aligned_lessons_01_12.md"),
      fetchText(DATA + "latin_course_2_source_aligned_lessons_01_12.md")
    ]);

    const latinCourses = new Map(latinManifest.courses.map(item => [item.id, item]));
    const active = courseManifest.courses.filter(item => item.status === "active");
    const dailyLessons = [...dailyA.lessons, ...dailyB.lessons, ...dailyC.lessons, ...dailyD.lessons];
    const overrideMap = new Map(grammarOverrides.overrides.map(item => [item.lesson_id + ":" + item.question_index, item.replacement]));

    const latinParse = (source, prefix) => {
      const lines = source.replace(/\r/g, "").split("\n");
      const starts = [];
      lines.forEach((line, index) => {
        const match = /^## Ders\s+(\d+)\s*[:—-]\s*(.+?)\s*$/.exec(line);
        if (match) starts.push({ index, number: Number(match[1]), title: match[2] });
      });
      return starts.map((start, position) => {
        const end = position + 1 < starts.length ? starts[position + 1].index : lines.length;
        return { id: prefix + "_" + String(start.number).padStart(2, "0"), number: start.number, title: start.title, markdown: lines.slice(start.index, end).join("\n").trim() };
      });
    };

    const latin1Lessons = latinParse(latin1, "kurmanji_latin_orthography");
    const latin2Lessons = latinParse(latin2, "kurmanji_latin_grammar");

    const map = new Map();
    active.forEach(course => {
      let lessons = [];
      if (course.id === "arami_orthography_foundations") {
        lessons = aramiManifest.lessons.map(item => ({
          id: item.id, number: item.number, title: item.title, status: item.status || "پێداچوونەوە",
          contentFile: item.content_file, type: "arami"
        }));
      } else if (course.id === "daily_conversation") {
        lessons = dailyLessons.map(item => ({
          id: "daily_conversation_" + String(item.number).padStart(2, "0"),
          number: item.number, title: item.title, status: item.review_status, type: "structured", source: item
        }));
      } else if (course.id === "unified_orthography") {
        lessons = unified.lessons.map(item => ({
          id: "unified_orthography_" + String(item.number).padStart(2, "0"),
          number: item.number, title: item.title, status: item.review_status, type: "structured", source: item
        }));
      } else if (course.id === "grammar") {
        lessons = grammar.lessons.map(item => {
          const quiz = (item.quiz || []).map((question, index) => {
            const replacement = overrideMap.get(item.id + ":" + index);
            return replacement || question;
          });
          return { id: item.id, number: item.number, title: item.title, status: item.review_status, type: "structured", source: { ...item, quiz } };
        });
      } else if (course.id === "kurmanji_latin_orthography") {
        lessons = latin1Lessons.map(item => ({ ...item, type: "markdown" }));
      } else if (course.id === "kurmanji_latin_grammar") {
        lessons = latin2Lessons.map(item => ({ ...item, type: "markdown" }));
      }
      map.set(course.id, { ...course, lessons, sourceStatus: course.id.startsWith("kurmanji_latin_") ? (latinCourses.get(course.id)?.status || "draft") : "" });
    });
    return map;
  }

  function renderCourseList(filter = "") {
    courseListEl.replaceChildren();
    const normalized = filter.trim().toLocaleLowerCase();
    let visible = 0;
    for (const course of courses) {
      if (normalized && !(course.title + " " + course.description).toLocaleLowerCase().includes(normalized)) continue;
      visible++;
      const button = document.createElement("button");
      button.type = "button";
      button.className = "course-button" + (selectedCourse?.id === course.id ? " active" : "");
      addText(button, "strong", course.title);
      addText(button, "small", course.lessons.length + " وانە");
      button.addEventListener("click", () => selectCourse(course.id));
      courseListEl.appendChild(button);
    }
    $("#course-count").textContent = visible + " / " + courses.length;
    if (!visible) addText(courseListEl, "p", "هیچ کۆرسێک نەدۆزرایەوە.", "muted");
  }

  function renderLessonNav() {
    lessonNavEl.replaceChildren();
    if (!selectedCourse) return;
    addText(lessonNavEl, "h3", "وانەکان (" + selectedCourse.lessons.length + ")");
    const done = completedSet(selectedCourse.id);
    selectedCourse.lessons.forEach(lesson => {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "lesson-link" + (selectedLesson?.id === lesson.id ? " active" : "") + (done.has(lesson.id) ? " done" : "");
      addText(button, "span", done.has(lesson.id) ? "✓" : String(lesson.number).padStart(2, "0"), "lesson-number");
      addText(button, "span", lesson.title);
      button.addEventListener("click", () => selectLesson(lesson.id));
      lessonNavEl.appendChild(button);
    });
  }

  function renderOverview() {
    if (!selectedCourse) return;
    courseOverviewEl.replaceChildren();
    addText(courseOverviewEl, "h2", selectedCourse.title);
    addText(courseOverviewEl, "p", selectedCourse.description || "");
    const completed = completedSet(selectedCourse.id).size;
    const total = selectedCourse.lessons.length;
    const percent = total ? Math.round(completed / total * 100) : 0;
    const row = document.createElement("div"); row.className = "progress-row";
    addText(row, "span", "پێشکەوتن: " + completed + " لە " + total);
    const track = document.createElement("div"); track.className = "progress-track";
    const fill = document.createElement("div"); fill.className = "progress-fill"; fill.style.width = percent + "%";
    track.appendChild(fill); row.appendChild(track); addText(row, "span", percent + "%");
    courseOverviewEl.appendChild(row);
    if (selectedCourse.id === "grammar") addText(courseOverviewEl, "p", "هەندێک وانە لە دۆخی پێداچوونەوەی Beta دان؛ کویز و پەسەندکردنی فەرمی بەپێی دۆخی وانە جیاوازن.", "status-note");
    else if (selectedCourse.id === "daily_conversation") addText(courseOverviewEl, "p", "وانەکانی ئەم کۆرسە لە دۆخی ڕەشنووسی پێداچوونەوەی دەق دان.", "status-note");
    else if (selectedCourse.id === "unified_orthography") addText(courseOverviewEl, "p", "ناوەڕۆکی ئەم کۆرسە لە دۆخی پێداچوونەوەی دەق و فێرکارییە.", "status-note");
    else if (selectedCourse.id.startsWith("kurmanji_latin_")) addText(courseOverviewEl, "p", "ئەم کۆرسە وەک ڕەشنووسی سەرچاوەیی نیشان دەدرێت؛ پێویستی بە پێداچوونەوەی کۆتایی هەیە.", "status-note");
    else if (selectedCourse.id === "arami_orthography_foundations") addText(courseOverviewEl, "p", "سەرچاوەی وانەکان پارێزراوە؛ دۆخی پێداچوونەوەی هەر وانە لە تۆماری سەرچاوەدا هەیە.", "status-note");
  }

  function selectCourse(courseId) {
    selectedCourse = courses.find(course => course.id === courseId) || null;
    selectedLesson = selectedCourse?.lessons[0] || null;
    renderCourseList(courseSearchEl.value);
    renderOverview();
    renderLessonNav();
    if (selectedLesson) selectLesson(selectedLesson.id);
  }

  async function selectLesson(lessonId) {
    selectedLesson = selectedCourse.lessons.find(lesson => lesson.id === lessonId);
    renderLessonNav();
    lessonContentEl.replaceChildren();
    if (!selectedLesson) return;
    addText(lessonContentEl, "div", "کۆرس " + selectedCourse.title + " · وانەی " + selectedLesson.number, "lesson-kicker");
    addText(lessonContentEl, "h1", selectedLesson.title);
    const meta = document.createElement("div"); meta.className = "lesson-meta";
    addText(meta, "span", "وانەی " + selectedLesson.number, "meta-pill");
    if (selectedLesson.status) addText(meta, "span", "دۆخ: " + formatStatus(selectedLesson.status), "meta-pill");
    lessonContentEl.appendChild(meta);
    addText(lessonContentEl, "p", "ناوەڕۆک بار دەکرێت...", "loading");
    try {
      const loading = lessonContentEl.querySelector(".loading");
      let quiz = [];
      if (selectedLesson.type === "arami") {
        const raw = await fetchText(selectedLesson.contentFile);
        if (loading) loading.remove();
        if (selectedLesson.contentFile.endsWith(".json")) renderAramiJson(lessonContentEl, JSON.parse(raw));
        else renderMarkdown(lessonContentEl, raw);
      } else if (selectedLesson.type === "markdown") {
        if (loading) loading.remove();
        renderMarkdown(lessonContentEl, selectedLesson.markdown);
      } else {
        if (loading) loading.remove();
        renderStructured(lessonContentEl, selectedLesson.source, selectedCourse.id);
        quiz = normalizeQuiz(selectedLesson.source, selectedCourse.id);
        renderQuiz(lessonContentEl, quiz);
      }
      const actions = document.createElement("div"); actions.className = "lesson-actions";
      const done = completedSet(selectedCourse.id).has(selectedLesson.id);
      const mark = document.createElement("button"); mark.type = "button";
      mark.className = "action-button"; mark.textContent = done ? "✓ تەواو کراوە" : "وانەکەم تەواو کرد";
      mark.addEventListener("click", () => {
        const set = completedSet(selectedCourse.id); set.add(selectedLesson.id);
        progress[selectedCourse.id] = Array.from(set); saveProgress();
        renderOverview(); renderLessonNav(); mark.textContent = "✓ تەواو کراوە";
      });
      actions.appendChild(mark);
      const index = selectedCourse.lessons.findIndex(item => item.id === selectedLesson.id);
      const prev = document.createElement("button"); prev.type = "button"; prev.className = "action-button secondary";
      prev.textContent = "وانەی پێشوو"; prev.disabled = index <= 0;
      prev.addEventListener("click", () => selectLesson(selectedCourse.lessons[index - 1].id));
      const next = document.createElement("button"); next.type = "button"; next.className = "action-button secondary";
      next.textContent = "وانەی دواتر"; next.disabled = index >= selectedCourse.lessons.length - 1;
      next.addEventListener("click", () => selectLesson(selectedCourse.lessons[index + 1].id));
      actions.append(prev, next);
      lessonContentEl.appendChild(actions);
      lessonContentEl.scrollIntoView({ behavior: "smooth", block: "start" });
    } catch (error) {
      lessonContentEl.querySelector(".loading")?.remove();
      addText(lessonContentEl, "p", error.message || "هەڵەیەک لە بارکردنی وانە ڕوویدا.", "error");
    }
  }

  async function init() {
    try {
      courseListEl.innerHTML = '<p class="muted">کۆرسەکان بار دەکرێن...</p>';
      courseData = await loadAllData();
      courses = Array.from(courseData.values());
      $("#course-count").textContent = courses.length;
      renderCourseList();
      if (courses.length) selectCourse(courses[0].id);
    } catch (error) {
      courseListEl.replaceChildren();
      addText(courseListEl, "p", error.message || "بارکردنی زانیاریی کۆرسەکان سەرکەوتوو نەبوو.", "error");
      lessonContentEl.replaceChildren();
      addText(lessonContentEl, "p", "تکایە پەیوەندیی ئینتەرنێت بپشکنە و دووبارە هەوڵ بدە.", "error");
    }
  }

  courseSearchEl.addEventListener("input", () => renderCourseList(courseSearchEl.value));
  init();
})();