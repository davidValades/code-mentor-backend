(() => {
  'use strict';
  const data = JSON.parse(document.getElementById('progress-data').textContent);
  const t = data.labels;
  const $ = id => document.getElementById(id);
  const make = (tag, text, className) => {
    const el = document.createElement(tag);
    if (text !== undefined) el.textContent = text;
    if (className) el.className = className;
    return el;
  };
  document.querySelectorAll('[data-label]').forEach(el => { el.textContent = t[el.dataset.label]; });
  document.title = t.title;
  const dateOnly = value => new Date(value + 'T00:00:00Z');
  const iso = date => date.toISOString().slice(0, 10);
  const plus = (value, days) => { const d = dateOnly(value); d.setUTCDate(d.getUTCDate()+days); return iso(d); };
  const validDate = value => /^\d{4}-\d{2}-\d{2}$/.test(value) && !Number.isNaN(dateOnly(value).getTime()) && iso(dateOnly(value)) === value;
  const humanDay = value => new Intl.DateTimeFormat(data.language, {dateStyle:'medium',timeZone:'UTC'}).format(dateOnly(value));
  const humanStamp = value => new Intl.DateTimeFormat(data.language, {dateStyle:'medium',timeStyle:'short',timeZone:data.time_zone}).format(new Date(value));
  $('snapshot-line').textContent = `${t.scope[data.scope]} · ${t.generated}: ${humanStamp(data.display_generated_at)} · ${data.time_zone}`;
  if (data.demo) { $('demo').hidden=false; $('demo').textContent=t.demo; }
  for (const [key, value] of [['generated',data.generated_at],['zone',data.time_zone],['revision',data.source_revision],['digest',data.source_digest]]) {
    $('provenance').append(make('dt',t[key]),make('dd',String(value)));
  }
  const fill = (id, choices, allText) => {
    const select = $(id); select.append(new Option(allText, ''));
    for (const [value,label] of choices) select.append(new Option(label,value));
  };
  fill('topic',data.concepts.map(c => [c.topic,c.topic]),t.allTopics);
  fill('activity',Object.entries(t.activities).filter(([id]) => id !== 'declared'),t.all);
  fill('assistance',Object.entries(t.helps).filter(([id]) => id !== 'solution'),t.all);
  fill('outcome',Object.entries(t.outcomes),t.all);
  $('start').value=data.range.start; $('end').value=data.range.end;
  let selectedDay = null, filtered = [], byDay = new Map();
  const fields = ['topic','activity','assistance','outcome'];
  const matches = e => fields.every(key => !$(key).value || e[key] === $(key).value);

  function dayDetails() {
    const area=$('day-details'); area.replaceChildren();
    $('day-heading').textContent=selectedDay ? `${t.dayTitle} · ${humanDay(selectedDay)}` : t.dayTitle;
    if (!selectedDay) { area.append(make('p',t.chooseDay,'muted')); return; }
    const rows=byDay.get(selectedDay) || [];
    if (!rows.length) { area.append(make('p',t.noDay,'muted')); return; }
    for (const e of rows) {
      const article=make('article',undefined,'attempt');
      article.append(make('h3',e.topic));
      const tags=make('div');
      for (const text of [t.activities[e.activity],t.modes[e.modality],t.helps[e.assistance]]) tags.append(make('span',text,'tag'));
      tags.append(make('span',t.outcomes[e.outcome],`tag result-${e.outcome}`));
      article.append(tags,make('p',e.evidence_summary));
      article.append(make('p',`${t.session}: ${e.session_id} · ${t.evidence}: ${e.id} · ${t.recorded}: ${humanStamp(e.display_at)}`,'meta'));
      if (e.session_completed_display_at) article.append(make('p',`${t.closed}: ${humanStamp(e.session_completed_display_at)}`,'meta'));
      area.append(article);
    }
  }

  function selectDay(value, focus=false) {
    selectedDay=value;
    $('calendar').querySelectorAll('button').forEach(b => {
      const selected=b.dataset.day === value;
      b.setAttribute('aria-pressed',String(selected)); b.tabIndex=selected ? 0 : -1;
      if (selected && focus) b.focus();
    });
    dayDetails();
  }

  function history() {
    const target=$('concepts'); target.replaceChildren();
    const concepts=data.concepts.filter(c => !$('topic').value || c.topic === $('topic').value);
    if (!concepts.length) { target.append(make('p',t.noConcepts,'muted')); return; }
    for (const concept of concepts) {
      const section=make('article',undefined,'concept');section.append(make('h3',concept.topic));
      section.append(make('p',`${t.status}: ${t.statuses[concept.status]}`));
      const details=make('details'); details.append(make('summary',t.milestones));
      if (!concept.milestones.length) details.append(make('p',t.noMilestones,'muted'));
      const milestones=make('ul',undefined,'milestone-list');
      for (const m of concept.milestones) {
        const item=make('li',`${t.statuses[m.kind]} · ${humanDay(m.day)}`);
        item.append(make('div',`${t.evidence}: ${m.event_ids.join(', ')}`,'evidence-ids'));milestones.append(item);
      }
      details.append(milestones);section.append(details);
      const checks=make('details');checks.append(make('summary',t.latest));
      if (!concept.latest_checks.length) checks.append(make('p',t.noChecks,'muted'));
      const list=make('ul',undefined,'check-list');
      for (const e of concept.latest_checks) {
        const item=make('li',`${t.activities[e.activity]} · ${t.modes[e.modality]} · ${t.outcomes[e.outcome]} · ${t.helps[e.assistance]} · ${humanDay(e.day)}`);
        item.append(make('div',`${t.evidence}: ${e.id}`,'evidence-ids'));list.append(item);
      }
      checks.append(list);section.append(checks);target.append(section);
    }
  }

  function calendar() {
    const start=$('start').value,end=$('end').value;
    const grid=$('calendar');grid.replaceChildren();$('months').replaceChildren();$('weekdays').replaceChildren();
    const weekdayNames = Array.from({length:7},(_,n) => new Intl.DateTimeFormat(data.language,{weekday:'short',timeZone:'UTC'}).format(dateOnly(plus('2026-01-05',n))));
    for (let n=0;n<7;n++) $('weekdays').append(make('span',n%2===0?weekdayNames[n]:''));
    const offset=(dateOnly(start).getUTCDay()+6)%7;
    for(let n=0;n<offset;n++) { const pad=make('span');pad.setAttribute('aria-hidden','true');grid.append(pad); }
    let index=offset, previousMonth=-1;
    const columns=Math.ceil((offset + Math.round((dateOnly(end)-dateOnly(start))/86400000)+1)/7);
    const monthCells=Array.from({length:columns},()=>make('span'));
    for(let day=start;day<=end;day=plus(day,1),index++) {
      const count=(byDay.get(day)||[]).length;
      const b=make('button',undefined,`day level-${Math.min(count,4)}`);
      b.type='button';b.dataset.day=day;b.setAttribute('aria-label',`${humanDay(day)} · ${t.attempts}: ${count}`);
      b.title=`${day} · ${count}`;b.setAttribute('aria-pressed',String(day===selectedDay));
      b.tabIndex=(selectedDay ? day===selectedDay : day===start) ? 0 : -1;
      b.addEventListener('click',()=>selectDay(b.dataset.day));
      b.addEventListener('keydown',e=>{
        const delta={ArrowUp:-1,ArrowDown:1,ArrowLeft:-7,ArrowRight:7}[e.key];
        if (delta!==undefined) {e.preventDefault();const next=plus(b.dataset.day,delta);if(next>=start&&next<=end)selectDay(next,true);}
      });
      grid.append(b);
      const month=dateOnly(day).getUTCMonth();
      if(month!==previousMonth) {monthCells[Math.floor(index/7)].textContent=new Intl.DateTimeFormat(data.language,{month:'short',timeZone:'UTC'}).format(dateOnly(day));previousMonth=month;}
      if(day===end)break;
    }
    $('months').append(...monthCells);
    const table=$('practice-table');table.replaceChildren();
    for(const [day, rows] of [...byDay.entries()].sort((a,b)=>b[0].localeCompare(a[0]))) {
      const row=make('tr');row.append(make('td',humanDay(day)),make('td',String(rows.length)),make('td',[...new Set(rows.map(e=>e.topic))].join(', ')));
      const cell=make('td'),button=make('button',t.openDay,'day-link');button.type='button';button.addEventListener('click',()=>selectDay(day));cell.append(button);row.append(cell);table.append(row);
    }
  }

  function update() {
    history();
    const start=$('start').value,end=$('end').value;
    const valid=validDate(start)&&validDate(end)&&start<=end&&(dateOnly(end)-dateOnly(start))/86400000<366;
    $('error').hidden=valid;$('error').textContent=valid?'':t.rangeError;
    if (!valid) return;
    filtered=data.events.filter(e=>e.practice&&e.day>=start&&e.day<=end&&matches(e));
    byDay=new Map();for(const e of filtered) {if(!byDay.has(e.day))byDay.set(e.day,[]);byDay.get(e.day).push(e);}
    if(selectedDay&&(selectedDay<start||selectedDay>end))selectedDay=null;
    $('days-count').textContent=String(byDay.size);$('attempts-count').textContent=String(filtered.length);
    $('topics-count').textContent=String(new Set(filtered.map(e=>e.topic)).size);$('empty').hidden=filtered.length>0;
    calendar();dayDetails();
  }
  for(const id of [...fields,'start','end'])$(id).addEventListener('change',update);
  $('reset').addEventListener('click',()=>{for(const id of fields)$(id).value='';$('start').value=data.range.start;$('end').value=data.range.end;selectedDay=null;update();});
  update();
})();
