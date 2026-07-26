function togglePw(inputId, btn, iconId) {
  btn.addEventListener('click', () => {
    const inp = document.getElementById(inputId);
    const showing = inp.type === 'text';
    inp.type = showing ? 'password' : 'text';
    document.getElementById(iconId).innerHTML = showing
      ? '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>'
      : '<path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/>';
  });
}

togglePw('password', document.getElementById('eyeBtn'), 'eyeIcon1');
togglePw('confirmPw', document.getElementById('eyeBtn2'), 'eyeIcon2');

// ==========================================
// PASSWORD STRENGTH & CHECKLIST
// ==========================================
const pwInput = document.getElementById('password');
const bars = ['sb1', 'sb2', 'sb3', 'sb4'].map(id => document.getElementById(id));
const strengthLabel = document.getElementById('strengthLabel');

const checks = {
  rLen:   v => v.length >= 8,
  rUpper: v => /[A-Z]/.test(v),
  rLower: v => /[a-z]/.test(v),
  rNum:   v => /\d/.test(v),
  rSpec:  v => /[^A-Za-z0-9]/.test(v)
};

const okSVG  = '<svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="#16A34A" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>';
const nokSVG = '<svg class="check-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/></svg>';

const barColors = ['#EF4444', '#F97316', '#EAB308', '#16A34A'];
const barLabels = ['Weak', 'Fair', 'Good', 'Strong'];

pwInput.addEventListener('input', () => {
  const v = pwInput.value;
  let score = 0;

  Object.entries(checks).forEach(([id, fn]) => {
    const li = document.getElementById(id);
    if (fn(v)) {
      li.classList.add('ok');
      li.innerHTML = okSVG + li.textContent.trim();
      score++;
    } else {
      li.classList.remove('ok');
      li.innerHTML = nokSVG + li.textContent.trim();
    }
  });

  if (!v) {
    bars.forEach(b => b.style.background = '#E2E8F0');
    strengthLabel.textContent = '';
    return;
  }

  const idx = Math.min(score - 1, 3);
  bars.forEach((b, i) => b.style.background = i <= idx ? barColors[idx] : '#E2E8F0');
  strengthLabel.textContent = barLabels[Math.min(score - 1, 3)] || '';
  strengthLabel.style.color = barColors[Math.min(score - 1, 3)] || '#64748B';
});

// ==========================================
// USERNAME AVAILABILITY (MOCK)
// ==========================================
const usernameInput  = document.getElementById('username');
const usernameStatus = document.getElementById('usernameStatus');
const takenNames     = ['admin', 'user', 'test', 'innolift', 'developer'];
let usernameTimer;

usernameInput.addEventListener('input', () => {
  clearTimeout(usernameTimer);
  const v = usernameInput.value.trim();

  if (v.length < 4) {
    usernameStatus.textContent = '';
    usernameStatus.className = 'status-msg';
    return;
  }

  usernameStatus.textContent = 'Checking…';
  usernameStatus.className = 'status-msg checking';

  usernameTimer = setTimeout(() => {
    if (takenNames.includes(v.toLowerCase())) {
      usernameStatus.textContent = '✗ Username already taken';
      usernameStatus.className = 'status-msg taken';
    } else {
      usernameStatus.textContent = '✓ Username available';
      usernameStatus.className = 'status-msg available';
    }
  }, 700);
});

// ==========================================
// STEPPER
// ==========================================
function updateStepper(filledSections) {
  const items = [
    document.getElementById('si1'),
    document.getElementById('si2'),
    document.getElementById('si3'),
    document.getElementById('si4')
  ];
  const connectors = [
    document.getElementById('sc1'),
    document.getElementById('sc2'),
    document.getElementById('sc3')
  ];

  items.forEach((el, i) => {
    el.classList.remove('active', 'done');
    if (i < filledSections)      el.classList.add('done');
    else if (i === filledSections) el.classList.add('active');
  });

  connectors.forEach((c, i) => {
    c.classList.toggle('done', i < filledSections);
  });
}

// Live stepper as user fills cards
document.getElementById('regForm').addEventListener('input', () => {
  const p1 = document.getElementById('firstName').value && document.getElementById('lastName').value;
  const p2 = document.getElementById('email').value && document.getElementById('phone').value;
  const p3 = document.getElementById('address').value
          && document.getElementById('city').value
          && document.getElementById('state').value
          && document.getElementById('pincode').value;

  let done = 0;
  if (p1) done = 1;
  if (p1 && p2) done = 2;
  if (p1 && p2 && p3) done = 3;

  updateStepper(done);
});

// ==========================================
// VALIDATION HELPERS
// ==========================================
function showErr(id, msg) {
  const el = document.getElementById(id);
  el.textContent = msg;
  el.classList.add('show');
}

function clearErr(id) {
  const el = document.getElementById(id);
  el.textContent = '';
  el.classList.remove('show');
}

function markField(inputEl, valid) {
  inputEl.classList.toggle('error', !valid);
  inputEl.classList.toggle('valid', valid);
}

// ==========================================
// ENABLE SUBMIT ON TERMS CHECK
// ==========================================
const submitBtn = document.getElementById('submitBtn');

document.getElementById('terms').addEventListener('change', function () {
  submitBtn.disabled = !this.checked;
});

// ==========================================
// FORM SUBMIT & VALIDATION
// ==========================================
document.getElementById('regForm').addEventListener('submit', function (e) {
  e.preventDefault();
  let valid = true;

  // — Personal —
  const fn = document.getElementById('firstName');
  if (!fn.value.trim()) { showErr('firstNameErr', 'First name is required'); markField(fn, false); valid = false; }
  else { clearErr('firstNameErr'); markField(fn, true); }

  const ln = document.getElementById('lastName');
  if (!ln.value.trim()) { showErr('lastNameErr', 'Last name is required'); markField(ln, false); valid = false; }
  else { clearErr('lastNameErr'); markField(ln, true); }

  const dob = document.getElementById("dob");

  if (!dob.value.trim()) {
    showErr("dobErr", "Date of birth is required");
    markField(dob, false);
    valid = false;
  } else {
    clearErr("dobErr");
    markField(dob, true);
  }

  const gender = document.querySelector('input[name="gender"]:checked');
  if (!gender) { showErr('genderErr', 'Please select a gender'); valid = false; }
  else { clearErr('genderErr'); }

  // — Contact —
  const email = document.getElementById('email');
  if (!email.value.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
    showErr('emailErr', 'Enter a valid email address'); markField(email, false); valid = false;
  } else { clearErr('emailErr'); markField(email, true); }

  const phone = document.getElementById('phone');
  if (!phone.value.trim() || !/^\d{10}$/.test(phone.value)) {
    showErr('phoneErr', 'Enter a valid 10-digit number'); markField(phone, false); valid = false;
  } else { clearErr('phoneErr'); markField(phone, true); }

  // — Address —
  const addr = document.getElementById('address');
  if (!addr.value.trim()) { showErr('addressErr', 'Street address is required'); markField(addr, false); valid = false; }
  else { clearErr('addressErr'); markField(addr, true); }

  const city = document.getElementById('city');
  if (!city.value.trim()) { showErr('cityErr', 'City is required'); markField(city, false); valid = false; }
  else { clearErr('cityErr'); markField(city, true); }

  const state = document.getElementById('state');
  if (!state.value) { showErr('stateErr', 'Please select a state'); markField(state, false); valid = false; }
  else { clearErr('stateErr'); markField(state, true); }

  const pin = document.getElementById('pincode');
  if (!pin.value.trim() || !/^\d{6}$/.test(pin.value)) {
    showErr('pincodeErr', 'Enter a valid 6-digit pincode'); markField(pin, false); valid = false;
  } else { clearErr('pincodeErr'); markField(pin, true); }

  // — Account —
  const uname = document.getElementById('username');
  if (!uname.value.trim() || uname.value.trim().length < 4) {
    showErr('usernameErr', 'Username must be at least 4 characters'); markField(uname, false); valid = false;
  } else if (takenNames.includes(uname.value.trim().toLowerCase())) {
    showErr('usernameErr', 'Username is already taken'); markField(uname, false); valid = false;
  } else { clearErr('usernameErr'); markField(uname, true); }

  const pw = document.getElementById('password');
  const allChecks = Object.values(checks).every(fn => fn(pw.value));
  if (!pw.value || !allChecks) {
    showErr('passwordErr', 'Password does not meet all requirements'); markField(pw, false); valid = false;
  } else { clearErr('passwordErr'); markField(pw, true); }

  const cpw = document.getElementById('confirmPw');
  if (!cpw.value || cpw.value !== pw.value) {
    showErr('confirmPwErr', 'Passwords do not match'); markField(cpw, false); valid = false;
  } else { clearErr('confirmPwErr'); markField(cpw, true); }

  if (!document.getElementById('terms').checked) {
    showErr('termsErr', 'You must accept the terms to continue'); valid = false;
  } else { clearErr('termsErr'); }

  if (!valid) return;

  // — Success —
  updateStepper(4);

  document.getElementById('sumName').textContent     = fn.value.trim() + ' ' + ln.value.trim();
  document.getElementById('sumDob').textContent      = dob.value;
  document.getElementById('sumGender').textContent   = gender.value.charAt(0).toUpperCase() + gender.value.slice(1);
  document.getElementById('sumEmail').textContent    = email.value.trim();
  document.getElementById('sumPhone').textContent    = phone.value.trim();
  document.getElementById('sumUsername').textContent = uname.value.trim();
  document.getElementById('sumAddress').textContent  =
    addr.value.trim() + ', ' + city.value.trim() + ', ' + state.value + ' – ' + pin.value + ', India';

  document.getElementById('regForm').style.display      = 'none';
  document.getElementById('summaryCard').style.display  = 'block';
  document.getElementById('summaryCard').scrollIntoView({ behavior: 'smooth' });

  const toast = document.getElementById('toast');
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 3500);
});

// ==========================================
// RESET FORM
// ==========================================
document.getElementById('resetBtn').addEventListener('click', () => {
  document.getElementById('regForm').reset();
  document.querySelectorAll('.err-msg').forEach(el => el.classList.remove('show'));
  document.querySelectorAll('input, select, textarea').forEach(el => el.classList.remove('error', 'valid'));
  strengthLabel.textContent = '';
  bars.forEach(b => b.style.background = '#E2E8F0');
  usernameStatus.textContent = '';
  usernameStatus.className = 'status-msg';
  submitBtn.disabled = true;
  updateStepper(0);
});

// Register another user button
document.getElementById('newRegBtn').addEventListener('click', () => {
  document.getElementById('summaryCard').style.display = 'none';
  document.getElementById('regForm').style.display     = 'block';
  document.getElementById('regForm').reset();
  document.querySelectorAll('.err-msg').forEach(el => el.classList.remove('show'));
  document.querySelectorAll('input, select, textarea').forEach(el => el.classList.remove('error', 'valid'));
  submitBtn.disabled = true;
  updateStepper(0);
  window.scrollTo({ top: 0, behavior: 'smooth' });
});
