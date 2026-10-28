/* Execute the shipped script against an in-memory DOM. This is not a browser/layout test. */
'use strict';
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');

class Element {
  constructor(tag,doc) {this.tagName=tag;this.doc=doc;this.children=[];this.attrs={};this.dataset={};this.events={};this.value='';this._text='';this.hidden=false;}
  set textContent(value) {this._text=String(value);this.children=[];}
  get textContent() {return this._text+this.children.map(c=>c.textContent).join('');}
  setAttribute(key,value) {this.attrs[key]=String(value);if(key==='id')this.doc.ids[value]=this;if(key.startsWith('data-'))this.dataset[key.slice(5)]=String(value);if(key==='hidden')this.hidden=true;}
  getAttribute(key) {return this.attrs[key];}
  append(...items) {for(const item of items)this.children.push(typeof item==='string'?Object.assign(new Element('#text',this.doc),{textContent:item}):item);}
  replaceChildren(...items) {this.children=[];this._text='';this.append(...items);}
  addEventListener(type,callback) {(this.events[type] ||= []).push(callback);}
  dispatch(type,extra={}) {for(const callback of this.events[type]||[])callback({target:this,preventDefault(){},...extra});}
  click() {this.dispatch('click');}
  focus() {this.doc.activeElement=this;}
  querySelectorAll(selector) {const result=[];for(const child of this.children){if(selector==='[data-label]'?child.dataset.label!==undefined:child.tagName===selector)result.push(child);result.push(...child.querySelectorAll(selector));}return result;}
}

function load(file) {
  const html=fs.readFileSync(file,'utf8');
  const dataMatch=html.match(/<script id="progress-data" type="application\/json">([\s\S]*?)<\/script>/);
  const scripts=[...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];
  assert.equal(scripts.length,1,'Exactly one self-contained executable script');
  const doc={ids:{},activeElement:null,createElement(tag){return new Element(tag,this);},getElementById(id){assert.ok(this.ids[id],`Missing ${id}`);return this.ids[id];}};
  doc.root=new Element('document',doc);doc.querySelectorAll=selector=>doc.root.querySelectorAll(selector);
  const source=html.replace(/<script\b[^>]*>[\s\S]*?<\/script>/g,'');
  const stack=[doc.root],voidTags=new Set(['meta','input','br','link','hr']);
  for(const token of source.match(/<[^>]+>|[^<]+/g)||[]) {
    if(token.startsWith('</')) {if(stack.length>1)stack.pop();continue;}
    if(token.startsWith('<!'))continue;
    if(token.startsWith('<')) {
      const tag=token.match(/^<([\w-]+)/)?.[1];if(!tag)continue;
      const el=doc.createElement(tag);
      for(const match of token.matchAll(/\s([\w-]+)(?:="([^"]*)")?/g))el.setAttribute(match[1],match[2]||'');
      stack.at(-1).append(el);if(!voidTags.has(tag))stack.push(el);
    } else stack.at(-1).append(token);
  }
  const data=doc.createElement('script');data.setAttribute('id','progress-data');data.textContent=dataMatch[1];doc.root.append(data);
  function Option(text,value){const el=doc.createElement('option');el.textContent=text;el.value=value;return el;}
  vm.runInNewContext(scripts[0][1],{document:doc,Option,console},{timeout:5000});
  return {doc,model:JSON.parse(dataMatch[1]),$:id=>doc.getElementById(id)};
}

const [fixture,empty,hostile,compact]=process.argv.slice(2);
const {doc,$,model}=load(fixture);
assert.equal($('days-count').textContent,'3');assert.equal($('attempts-count').textContent,'5');
assert.equal($('topics-count').textContent,'3');assert.equal($('demo').hidden,false);
assert.equal($('calendar').querySelectorAll('button').length,365);
const day=value=>$('calendar').querySelectorAll('button').find(b=>b.dataset.day===value);
day('2026-10-28').click();assert.equal($('day-details').querySelectorAll('article').length,3);
assert.ok($('day-details').textContent.includes('unchecked'));assert.ok(!$('day-details').textContent.includes('solution'));
$('topic').value='csharp.methods';$('topic').dispatch('change');
assert.equal($('attempts-count').textContent,'3');assert.equal($('concepts').querySelectorAll('article').length,1);
$('start').value='2026-10-28';$('end').value='2026-10-28';$('start').dispatch('change');
assert.equal($('attempts-count').textContent,'1');assert.equal($('calendar').querySelectorAll('button').length,1);
assert.ok($('concepts').textContent.includes(model.labels.statuses.consolidated));
assert.ok($('concepts').textContent.includes('debug, recall'),'Old support survives calendar filter');
$('outcome').value='incorrect';$('outcome').dispatch('change');
assert.equal($('attempts-count').textContent,'0');assert.equal($('empty').hidden,false);
assert.ok($('concepts').textContent.includes(model.labels.statuses.consolidated));
$('reset').click();assert.equal($('attempts-count').textContent,'5');assert.equal($('topic').value,'');
day('2026-10-28').dispatch('keydown',{key:'ArrowUp'});
assert.equal(doc.activeElement.dataset.day,'2026-10-27');assert.equal(doc.activeElement.getAttribute('aria-pressed'),'true');
$('start').value='2024-01-01';$('start').dispatch('change');assert.equal($('error').hidden,false);
$('end').value='2024-02-29';$('start').value='2024-02-01';$('end').dispatch('change');
assert.equal($('error').hidden,true);assert.ok(day('2024-02-29'));assert.equal($('calendar').querySelectorAll('button').length,29);
$('start').value='9999-12-31';$('end').value='9999-12-31';$('end').dispatch('change');
assert.equal($('calendar').querySelectorAll('button').length,1,'Maximum supported calendar date must terminate');
const blank=load(empty);assert.equal(blank.$('attempts-count').textContent,'0');assert.equal(blank.$('empty').hidden,false);
const attack=load(hostile);attack.$('topic').value=attack.model.events[0].topic;attack.$('topic').dispatch('change');
const attempt=attack.$('calendar').querySelectorAll('button').find(b=>b.dataset.day===attack.model.events[0].day);attempt.click();
assert.ok(attack.$('day-details').textContent.includes('</script><img'));
assert.equal(attack.$('day-details').querySelectorAll('img').length,0);
const compactPage=load(compact);
compactPage.$('calendar').querySelectorAll('button').find(b=>b.dataset.day==='2026-10-28').click();
assert.equal(compactPage.$('day-details').querySelectorAll('article').length,1);
assert.ok(compactPage.$('day-details').textContent.includes(compactPage.model.labels.closed));
console.log('PASS: day selection, filters/reset, historical support, keyboard, date validation/leap day, empty and hostile data (in-memory DOM; layout not tested)');
