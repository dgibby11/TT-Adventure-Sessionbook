// monsters.js — D&D 5e stat block renderer.
// Exposes window.MonsterRenderer = { buildStatBlock } for use by resources.js.

(function () {
  const ABILITY_NAMES = {
    str:'Strength', dex:'Dexterity', con:'Constitution',
    int:'Intelligence', wis:'Wisdom', cha:'Charisma',
  };

  function renderTag(tag, content) {
    const parts = content.split('|');
    const main  = parts[0].trim();
    switch (tag) {
      case 'atk': {
        const map = { mw:'Melee Weapon Attack', rw:'Ranged Weapon Attack', ms:'Melee Spell Attack', rs:'Ranged Spell Attack' };
        const types = main.split(',').map(k => map[k.trim()] || k);
        return `<em>${[...new Set(types)].join(' or ')}:</em>`;
      }
      case 'atkr': {
        const map2 = { m:'Melee Attack Roll', r:'Ranged Attack Roll' };
        const types2 = main.split(',').map(k => map2[k.trim()] || k);
        return `<em>${[...new Set(types2)].join(' or ')}:</em>`;
      }
      case 'dc':      return `DC ${main}`;
      case 'actSave': return `<strong>${ABILITY_NAMES[main.toLowerCase()] || main} Saving Throw:</strong>`;
      case 'actSaveFail':          return `<strong>Failure:</strong>`;
      case 'actSaveSuccess':       return `<strong>Success:</strong>`;
      case 'actSaveSuccessOrFail': return `<strong>Effect:</strong>`;
      case 'hit':    return `+${main} to hit`;
      case 'h':      return '<strong>Hit:</strong>';
      case 'damage': return main;
      case 'dice':   return main;
      case 'recharge': return main === '6' ? '(Recharge 6)' : `(Recharge ${main}–6)`;
      case 'i':      return `<em>${main}</em>`;
      case 'b':      return `<strong>${main}</strong>`;
      case 'spell':      return `<em>${main}</em>`;
      case 'condition':  return `<em>${main}</em>`;
      case 'status':     return `<em>${main}</em>`;
      case 'note':       return '';
      default:           return main;
    }
  }

  function renderText(str) {
    if (!str) return '';
    return str.replace(/\{@(\w+)([^}]*)\}/g, (_, tag, rest) => renderTag(tag, rest.trimStart()));
  }

  function renderEntries(entries) {
    if (!entries) return '';
    return entries.map(e => {
      if (typeof e === 'string') return `<p style="margin:0.15rem 0">${renderText(e)}</p>`;
      if (typeof e !== 'object') return '';
      switch (e.type) {
        case 'entries':
          return `<p style="margin:0.15rem 0"><strong>${renderText(e.name || '')}</strong> ${renderEntries(e.entries)}</p>`;
        case 'list':
          return `<ul style="margin:0.15rem 0 0.15rem 1.2rem">${(e.items||[]).map(i =>
            `<li>${typeof i === 'string' ? renderText(i) : renderEntries(i.entries||[])}</li>`).join('')}</ul>`;
        case 'inset': case 'quote':
          return `<blockquote style="margin:0.3rem 0 0.3rem 0.8rem;border-left:3px solid #9c2512;padding-left:0.5rem;font-style:italic">${renderEntries(e.entries)}</blockquote>`;
        default:
          if (e.entries) return renderEntries(e.entries);
          return '';
      }
    }).join('');
  }

  const SIZES = { T:'Tiny', S:'Small', M:'Medium', L:'Large', H:'Huge', G:'Gargantuan' };
  const LAW   = { L:'Lawful', N:'Neutral', C:'Chaotic' };
  const GOOD  = { G:'Good', N:'Neutral', E:'Evil' };

  function cap(s) { return s ? s[0].toUpperCase() + s.slice(1) : ''; }

  function fmtAlignment(arr) {
    if (!arr || !arr.length || arr.includes('U')) return 'Unaligned';
    if (arr.includes('A')) return 'Any Alignment';
    if (arr.length === 1 && arr[0] === 'N') return 'Neutral';
    if (arr.length === 2) {
      const l = LAW[arr[0]], g = GOOD[arr[1]];
      if (l && g) return `${l} ${g}`;
    }
    return arr.join(' ');
  }

  function fmtType(type) {
    if (!type) return '';
    if (typeof type === 'string') return cap(type);
    const base  = cap(type.type || '');
    const tags  = type.tags ? ` (${type.tags.join(', ')})` : '';
    const swarm = type.swarmSize ? ` swarm of ${SIZES[type.swarmSize]||type.swarmSize} ${base}s` : '';
    return swarm || (base + tags);
  }

  function abilMod(score) {
    const m = Math.floor((score - 10) / 2);
    return m >= 0 ? `+${m}` : `${m}`;
  }

  function fmtAC(ac) {
    if (!ac || !ac.length) return '–';
    const entry = ac[0];
    if (typeof entry === 'number') return `${entry}`;
    const from = (entry.from || []).join(', ');
    const cond = entry.condition ? ` ${entry.condition}` : '';
    return from ? `${entry.ac} (${from})${cond}` : `${entry.ac}${cond}`;
  }

  function fmtHP(hp) {
    if (!hp) return '–';
    return hp.special || `${hp.average} (${hp.formula})`;
  }

  function fmtSpeed(speed) {
    if (!speed) return '–';
    const parts = [];
    for (const key of ['walk','burrow','climb','fly','swim']) {
      if (!speed[key]) continue;
      const val   = speed[key];
      const num   = typeof val === 'object' ? val.number : val;
      const cond  = typeof val === 'object' && val.condition ? ` (${val.condition})` : '';
      const hover = key === 'fly' && speed.canHover ? ' (hover)' : '';
      const label = key === 'walk' ? '' : cap(key) + ' ';
      parts.push(`${label}${num} ft.${hover}${cond}`);
    }
    return parts.join(', ') || '–';
  }

  const CR_XP = {
    '0':5,'1/8':25,'1/4':50,'1/2':100,
    '1':200,'2':450,'3':700,'4':1100,'5':1800,'6':2300,'7':2900,'8':3900,
    '9':5000,'10':5900,'11':7200,'12':8400,'13':10000,'14':11500,'15':13000,
    '16':15000,'17':18000,'18':20000,'19':22000,'20':25000,
    '21':33000,'22':41000,'23':50000,'24':62000,'25':75000,
    '26':90000,'27':105000,'28':120000,'29':135000,'30':155000,
  };

  function fmtCR(cr) {
    const val = typeof cr === 'object' ? cr.cr : cr;
    if (!val && val !== '0') return '–';
    const xp    = CR_XP[val];
    const xpStr = xp != null ? ` (${xp.toLocaleString()} XP` : ' (';
    const lairXp = typeof cr === 'object' && cr.xpLair ? `; ${cr.xpLair.toLocaleString()} XP in Lair)` : ')';
    return `${val}${xpStr}${lairXp}`;
  }

  function fmtProfBonus(cr) {
    const val = typeof cr === 'object' ? cr.cr : cr;
    const n   = (val === '1/8'||val==='1/4'||val==='1/2'||val==='0') ? 0 : parseInt(val, 10);
    return `+${Math.max(2, Math.ceil(n / 4) + 1)}`;
  }

  function listStr(arr) {
    if (!arr || !arr.length) return '';
    return arr.map(s => typeof s === 'string' ? s : (s.name || '')).join(', ');
  }

  const SLOT_LABEL = {
    '0':'Cantrips (at will)', '1':'1st level', '2':'2nd level', '3':'3rd level',
    '4':'4th level', '5':'5th level', '6':'6th level', '7':'7th level',
    '8':'8th level', '9':'9th level',
  };

  function renderSpellcasting(sc) {
    const lines  = [];
    const scName = renderText(sc.name || 'Spellcasting');
    lines.push(sc.headerEntries
      ? `<div class="sb-entry"><span class="sb-entry-name">${scName}</span> ${renderEntries(sc.headerEntries)}</div>`
      : `<div class="sb-entry"><span class="sb-entry-name">${scName}</span></div>`);
    const ul = ['<ul class="sb-spell-list">'];
    if (sc.constant) ul.push(`<li><span class="sb-spell-slot-label">Constant:</span> ${sc.constant.map(s=>renderText(s)).join(', ')}</li>`);
    if (sc.will)     ul.push(`<li><span class="sb-spell-slot-label">At Will:</span> ${sc.will.map(s=>renderText(s)).join(', ')}</li>`);
    if (sc.ritual)   ul.push(`<li><span class="sb-spell-slot-label">Rituals:</span> ${sc.ritual.map(s=>renderText(s)).join(', ')}</li>`);
    if (sc.daily) {
      for (const [times, spells] of Object.entries(sc.daily)) {
        const label = times.endsWith('e') ? `${times.replace('e','')}/Day each` : `${times}/Day`;
        ul.push(`<li><span class="sb-spell-slot-label">${label}:</span> ${spells.map(s=>renderText(s)).join(', ')}</li>`);
      }
    }
    if (sc.spells) {
      for (const [level, data] of Object.entries(sc.spells)) {
        const label = SLOT_LABEL[level] || `${level}th level`;
        const slots = data.slots ? ` (${data.slots} slot${data.slots>1?'s':''})` : '';
        ul.push(`<li><span class="sb-spell-slot-label">${label}${slots}:</span> ${(data.spells||[]).map(s=>renderText(s)).join(', ')}</li>`);
      }
    }
    if (sc.footerEntries) ul.push(`<li><em>${renderEntries(sc.footerEntries)}</em></li>`);
    ul.push('</ul>');
    lines.push(ul.join(''));
    return lines.join('');
  }

  function renderSection(title, entries) {
    if (!entries || !entries.length) return '';
    const items = entries.map(e => {
      if (e.type === 'spellcasting') return renderSpellcasting(e);
      const nameHtml    = e.name ? `<span class="sb-entry-name">${renderText(e.name)}</span> ` : '';
      const textEntries = e.entries || [];
      if (!textEntries.length) return `<p class="sb-entry">${nameHtml}</p>`;
      return textEntries.map((te, idx) => {
        const prefix = idx === 0 ? nameHtml : '';
        if (typeof te === 'string') return `<p class="sb-entry">${prefix}${renderText(te)}</p>`;
        return `<div class="sb-entry">${prefix}${renderEntries([te])}</div>`;
      }).join('');
    }).join('');
    return title ? `<div class="sb-section-title">${title}</div>${items}` : items;
  }

  function buildStatBlock(m) {
    const size      = (m.size||[]).map(s=>SIZES[s]||s).join('/');
    const alignment = fmtAlignment(m.alignment);
    const meta      = [size, fmtType(m.type)].filter(Boolean).join(' ') + ', ' + alignment;

    const details = [];
    if (m.save && Object.keys(m.save).length)
      details.push(`<p><span class="label">Saving Throws</span> ${Object.entries(m.save).map(([k,v])=>`${cap(k)} ${v}`).join(', ')}</p>`);
    if (m.skill && Object.keys(m.skill).length)
      details.push(`<p><span class="label">Skills</span> ${Object.entries(m.skill).map(([k,v])=>`${cap(k)} ${v}`).join(', ')}</p>`);
    if (m.vulnerable && m.vulnerable.length)
      details.push(`<p><span class="label">Damage Vulnerabilities</span> ${listStr(m.vulnerable)}</p>`);
    if (m.resist && m.resist.length)
      details.push(`<p><span class="label">Damage Resistances</span> ${listStr(m.resist)}</p>`);
    if (m.immune && m.immune.length)
      details.push(`<p><span class="label">Damage Immunities</span> ${listStr(m.immune)}</p>`);
    if (m.conditionImmune && m.conditionImmune.length)
      details.push(`<p><span class="label">Condition Immunities</span> ${listStr(m.conditionImmune)}</p>`);
    details.push(`<p><span class="label">Senses</span> ${[...(m.senses||[]), `Passive Perception ${m.passive||10}`].join(', ')}</p>`);
    details.push(`<p><span class="label">Languages</span> ${(m.languages||[]).join(', ') || '—'}</p>`);

    const legActions = m.legendaryActionsLair != null ? m.legendaryActionsLair : 3;
    const monTypeName = (typeof m.type === 'string' ? m.type : m.type?.type) || 'creature';
    const legIntro = m.legendary && m.legendary.length
      ? `<p class="sb-legendary-intro">The ${monTypeName} can take ${legActions} legendary action${legActions!==1?'s':''}, choosing from the options below. Only one legendary action option can be used at a time and only at the end of another creature's turn. The ${monTypeName} regains spent legendary actions at the start of its turn.</p>`
      : '';

    let loreHtml = '';
    if (m.description && m.description.length) {
      const paras = m.description.map(d => {
        const headerMatch = d.match(/^\{@i ([^}]+)\}$/);
        if (headerMatch) return `<span class="lore-header">${headerMatch[1]}</span>`;
        return `<p>${renderText(d)}</p>`;
      }).join('');
      loreHtml = `<div class="sb-lore">${paras}</div>`;
    }

    return `
<div class="stat-block">
  <div class="sb-inner">
    <h2 class="sb-name">${m.name}</h2>
    <p class="sb-meta">${meta}</p>

    <hr class="sb-rule">
    <div class="sb-basics">
      <p><span class="label">Armor Class</span> ${fmtAC(m.ac)}</p>
      <p><span class="label">Hit Points</span> ${fmtHP(m.hp)}</p>
      <p><span class="label">Speed</span> ${fmtSpeed(m.speed)}</p>
    </div>

    <hr class="sb-rule">
    <div class="sb-abilities">
      ${['str','dex','con','int','wis','cha'].map(a => `
        <div class="sb-ability">
          <span class="score-label">${a.toUpperCase()}</span>
          <span class="score-val">${m[a]??'–'}</span>
          <span class="score-mod">(${abilMod(m[a]??10)})</span>
        </div>`).join('')}
    </div>

    <hr class="sb-rule">
    <div class="sb-details">
      ${details.join('')}
      <div class="sb-cr-row">
        <p><span class="label">Challenge</span> ${fmtCR(m.cr)}</p>
        <p><span class="label">Proficiency Bonus</span> ${fmtProfBonus(m.cr)}</p>
      </div>
    </div>

    ${m.trait && m.trait.length ? `<hr class="sb-rule">${renderSection('Traits', m.trait)}` : ''}
    ${m.action && m.action.length ? `<hr class="sb-rule">${renderSection('Actions', m.action)}` : ''}
    ${m.bonus && m.bonus.length ? `<hr class="sb-rule">${renderSection('Bonus Actions', m.bonus)}` : ''}
    ${m.reaction && m.reaction.length ? `<hr class="sb-rule">${renderSection('Reactions', m.reaction)}` : ''}
    ${m.legendary && m.legendary.length ? `<hr class="sb-rule"><div class="sb-section-title">Legendary Actions</div>${legIntro}${renderSection('', m.legendary)}` : ''}
    ${m.mythic && m.mythic.length ? `<hr class="sb-rule">${renderSection('Mythic Actions', m.mythic)}` : ''}
  </div>
  ${loreHtml}
  <div class="sb-source">${m.page ? `${m.source} p.${m.page}` : m.source}</div>
</div>`;
  }

  window.MonsterRenderer = { buildStatBlock };
})();
