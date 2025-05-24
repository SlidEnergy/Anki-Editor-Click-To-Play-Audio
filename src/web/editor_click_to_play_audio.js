window.addEventListener('click', (e) => {
    // Ignore clicks with modifiers
    if (e.shiftKey || e.ctrlKey || e.altKey || e.metaKey) {
        return;
    }

    const target = e.target;

    // Only handle clicks in editor fields
    if (
        !target.classList.contains('rich-text-editable') ||
        !target.closest('.editor-field')
    ) {
        return;
    }

    // Editor fields are shadow DOMs
    // Get the shadow root to access the selection properly
    const shadowRoot = target.shadowRoot;
    if (!shadowRoot) {
        return;
    }

    // Check if the click is inside a sound tag
    const selection = shadowRoot.getSelection();

    // only handle caret selections, not ranges
    if (!selection || selection.type !== 'Caret') {
        return;
    }

    const node = selection.anchorNode;

    if (!node || node.nodeType !== Node.TEXT_NODE) {
        return;
    }

    const offset = selection.anchorOffset;
    if (offset === 0 || offset === node.length) {
        return;
    }

    const text = node.textContent;

    // Get text before and after the caret
    const pre = text.slice(0, offset);
    const post = text.slice(offset);

    // Find the sound tag
    const preIdx = pre.lastIndexOf('[');
    const postIdx = post.indexOf(']');

    if (preIdx === -1 || postIdx === -1) {
        return;
    }

    const inner = text.slice(preIdx + 1, offset + postIdx);
    if (!inner.startsWith('sound:')) {
        return;
    }

    const soundFile = inner.slice(6);
    pycmd(`click-to-play-audio:play:${soundFile}`);
});
