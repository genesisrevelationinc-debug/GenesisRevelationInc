# CLAUDE.md - AI Assistant Guide for GenesisRevelationInc

## Project Overview

**Genesis Revelation Inc** is a non-profit Christian ministry website built as a static HTML site. The project focuses on delivering ministry content, mission information, resources, and donation capabilities through a clean, performant web interface.

**Project Type**: Static HTML website with Jekyll build support
**Hosting**: Cloudflare Pages
**Repository**: GitHub (genesisrevelationinc-debug organization)
**Total Size**: ~941KB (263KB hero image + HTML files)

## Quick Reference

- **Main Branch**: `main` (production)
- **Current Working Branch**: `claude/add-claude-documentation-3z8wm`
- **Primary Language**: HTML5 with inline CSS
- **Build Tool**: Jekyll (Docker-based)
- **CI/CD**: GitHub Actions
- **Image Assets**: `northernlights.jpg` (hero background, 263KB)

## Repository Structure

```
GenesisRevelationInc/
├── .github/
│   └── workflows/
│       ├── jekyll-docker.yml           # Jekyll build CI/CD
│       └── generator-generic-ossf-slsa3-publish.yml  # Supply chain security
├── index.html          # Main homepage with hero image (111 lines)
├── index2.html         # Cloudflare Pages placeholder (12 lines)
├── mission.html        # Ministry mission statement (70 lines)
├── resources.html      # Resources directory page (67 lines)
├── donate.html         # Donations page (73 lines)
├── contact.html        # Contact information page (53 lines)
├── northernlights.jpg  # Hero background image (263KB)
├── README.md           # Minimal project identifier
├── README2.md          # Project description
└── CLAUDE.md          # This file - AI assistant guide
```

## Technology Stack

### Frontend
- **HTML5**: Semantic markup with proper accessibility attributes
- **CSS3**: Inline styles using modern features (flexbox, gradients, rgba)
- **Images**: JPEG format for photography (optimized)

### Build & Deployment
- **Jekyll**: Static site generator (latest version via Docker)
- **Docker**: `jekyll/builder:latest` for consistent builds
- **GitHub Actions**: Automated CI/CD workflows
- **SLSA v3**: Supply chain security framework (OpenSSF compliance)

### Hosting & Infrastructure
- **Cloudflare Pages**: Static hosting platform
- **Git**: Version control with GitHub

## Development Workflows

### CI/CD Pipeline

#### Jekyll Build Workflow (`jekyll-docker.yml`)
**Trigger**: Push to `main` branch or pull requests
**Process**:
1. Checkout code
2. Build using Docker: `jekyll/builder:latest`
3. Run `jekyll build --future`
4. Output to `_site/` directory

**Important**: Always test builds locally before pushing to ensure Jekyll compatibility.

#### SLSA Provenance Workflow (`generator-generic-ossf-slsa3-publish.yml`)
**Trigger**: Manual dispatch or release creation
**Purpose**: Generate cryptographic provenance for supply chain security
**Process**:
1. Create build artifacts
2. Generate SHA256 hashes (base64 encoded)
3. Call SLSA framework workflow (v1.4.0)
4. Optionally upload to GitHub releases

### Git Workflow

**Branch Naming Convention**:
- Feature branches: `claude/<description>-<session-id>`
- Main branch: `main`

**Commit Message Style**:
- Use conventional commits format: `type: description`
- Examples: `fix: preload hero background for faster paint`
- Types: `fix`, `feat`, `refactor`, `docs`, `chore`

**Push Requirements**:
- Always use: `git push -u origin <branch-name>`
- Branch must start with `claude/` and match session ID
- Retry on network errors: exponential backoff (2s, 4s, 8s, 16s)

### Recent Development History
```
254dfa8 Merge pull request #1 - improve slow code performance
8e56223 fix: preload hero background for faster paint
bb90bea Initial plan
76947e6 Add CI workflow for Jekyll site using Docker
5a005a2 Create generator-generic-ossf-slsa3-publish.yml
bbf1567 Fix background image URL in index.html
4a379dd Rename NorthernLights.JPG to northernlights.jpg
```

## Coding Conventions & Standards

### HTML Structure

**Standard Template Pattern**:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Title - Genesis Revelation Inc</title>
    <link rel="preload" as="image" href="northernlights.jpg">
    <style>
        /* Inline CSS here */
    </style>
</head>
<body>
    <nav><!-- Navigation --></nav>
    <main><!-- Content --></main>
    <footer><!-- Footer --></footer>
</body>
</html>
```

**Key Principles**:
- Semantic HTML5 elements (`<nav>`, `<main>`, `<footer>`, `<section>`)
- Proper heading hierarchy (single `<h1>` per page)
- Accessibility: `lang` attribute, meaningful alt text
- Performance: Image preloading via `<link rel="preload">`

### CSS Styling Conventions

**Architecture**: Inline styles (no external stylesheets)

**Color Palette**:
- Background: `#0b0b0b` (near black, dark theme)
- Text: `#ffffff` (white)
- Accents: `#dddddd`, `#cccccc` (light grays)
- Overlays: `rgba(0, 0, 0, 0.6)` (semi-transparent black)
- Borders: `rgba(255, 255, 255, 0.2)` (subtle white)

**Responsive Design**:
- Mobile-first approach with viewport meta tag
- Flexible containers: `max-width: 1200px`, `margin: 0 auto`
- Consistent padding: `20px` standard, `40px` for larger elements
- Text sizing: `18px` base, `42px` headings

**Layout Patterns**:
- Flexbox for navigation and alignment
- Linear gradients for overlays
- Transparent backgrounds for content containers

### File Naming Conventions

**Critical Rule**: All files must use lowercase names
- ✅ Correct: `northernlights.jpg`, `mission.html`
- ❌ Wrong: `NorthernLights.JPG`, `Mission.html`

**Rationale**: Case-sensitive file systems (Linux/Unix) require consistent naming.

### Navigation Structure

**Standard Navigation** (consistent across all pages):
```html
<nav style="...">
    <a href="index.html">Home</a>
    <a href="mission.html">Mission</a>
    <a href="resources.html">Resources</a>
    <a href="donate.html">Donate</a>
    <a href="contact.html">Contact</a>
</nav>
```

**Footer Pattern**:
```html
<footer style="...">
    <p>&copy; 2025 Genesis Revelation Inc. Sharing Christ's Truth.</p>
</footer>
```

## Performance Best Practices

### Image Optimization
- **Hero Images**: Preload critical images in `<head>`
  ```html
  <link rel="preload" as="image" href="northernlights.jpg">
  ```
- **File Size**: Keep images optimized (current: 263KB for hero)
- **Format**: JPEG for photos, PNG for graphics

### CSS Performance
- Inline critical CSS to avoid render-blocking requests
- Use hardware-accelerated properties (transform, opacity)
- Minimize reflows with fixed dimensions where possible

### HTML Optimization
- Minimize whitespace in production
- Use semantic elements for better browser optimization
- Proper meta tags for caching and viewport

## Common Tasks for AI Assistants

### 1. Adding a New Page
```bash
# Create new HTML file following template pattern
# Include standard navigation and footer
# Use consistent styling from existing pages
# Add to navigation in all other pages
# Test locally before committing
```

### 2. Updating Styles
- **Location**: Inline `<style>` tags in each HTML file
- **Consistency**: Apply changes across all pages if global
- **Testing**: Visual regression check on all pages

### 3. Image Updates
- **Naming**: Use lowercase filenames only
- **Optimization**: Compress before adding to repo
- **Preloading**: Add `<link rel="preload">` for above-fold images
- **Size**: Monitor repo size (currently 941KB total)

### 4. Content Changes
- **Mission**: Update `mission.html` for ministry messaging
- **Resources**: Modify `resources.html` for educational content
- **Donate**: Edit `donate.html` for contribution information
- **Contact**: Update `contact.html` for ministry contact details

### 5. Build & Deployment
```bash
# Local Jekyll build (if Jekyll installed)
jekyll build --future

# Docker-based build (mirrors CI)
docker run --rm -v "$PWD:/srv/jekyll" jekyll/builder:latest jekyll build --future

# GitHub Actions handles automatic deployment on push to main
```

## Important Constraints & Considerations

### DO
- ✅ Use lowercase filenames exclusively
- ✅ Maintain consistent navigation across all pages
- ✅ Test performance impact of changes (especially images)
- ✅ Follow conventional commit message format
- ✅ Preload critical images for faster paint times
- ✅ Keep inline styles consistent with existing patterns
- ✅ Ensure responsive design on all new features
- ✅ Update all pages when adding new navigation items

### DON'T
- ❌ Add mixed-case or uppercase filenames
- ❌ Create external CSS files without updating build process
- ❌ Add large images without optimization
- ❌ Break navigation consistency across pages
- ❌ Push directly to `main` (use feature branches)
- ❌ Skip preloading for above-fold images
- ❌ Add JavaScript without careful consideration
- ❌ Modify SLSA workflow without understanding security implications

### Security Considerations
- **SLSA Provenance**: Don't modify security workflows without review
- **External Dependencies**: Minimize to reduce attack surface
- **Static Content**: No server-side code = reduced vulnerability
- **HTTPS**: Cloudflare Pages provides automatic SSL

### Accessibility Requirements
- Always include `alt` attributes for images
- Maintain proper heading hierarchy
- Ensure sufficient color contrast (white on near-black passes WCAG)
- Keep navigation keyboard-accessible
- Use semantic HTML elements

## Testing Checklist

Before committing changes, verify:
- [ ] All filenames are lowercase
- [ ] Navigation links work on all pages
- [ ] Responsive design works on mobile/tablet/desktop
- [ ] Images load correctly and are optimized
- [ ] Footer copyright year is current
- [ ] HTML validates (W3C validator)
- [ ] Jekyll build succeeds (locally or via CI)
- [ ] No broken links
- [ ] Color contrast meets accessibility standards
- [ ] Performance: Critical images preloaded

## Future Enhancement Opportunities

### Areas for Improvement
1. **External CSS**: Extract inline styles to external stylesheet for maintainability
2. **JavaScript**: Consider adding progressive enhancements (form validation, analytics)
3. **Image Formats**: Migrate to WebP with JPEG fallbacks for better compression
4. **Build Process**: Add minification and bundling
5. **Testing**: Implement automated accessibility and performance testing
6. **Documentation**: Expand README with setup instructions
7. **Linting**: Add HTML/CSS linting to CI/CD pipeline
8. **CMS**: Consider headless CMS for content management
9. **Analytics**: Add privacy-respecting analytics (Plausible, Fathom)
10. **SEO**: Implement structured data (Schema.org) for better search visibility

### Missing Configuration Files
- `.gitignore`: No gitignore present (all files tracked including binaries)
- `_config.yml`: Jekyll configuration could be added for more control
- `package.json`: Could add for npm-based build tools
- `robots.txt`: For search engine guidance
- `sitemap.xml`: For better SEO

## Contact & Resources

**Ministry Website**: Genesis Revelation Inc (see index.html for details)
**Repository Owner**: genesisrevelationinc-debug organization
**CI/CD Platform**: GitHub Actions
**Hosting**: Cloudflare Pages

## Version History

- **Current Version**: Active development on `claude/add-claude-documentation-3z8wm`
- **Last Major Update**: Performance improvements (image preloading)
- **Recent PR**: #1 - Improve slow code performance (merged)

---

**Last Updated**: 2026-01-06
**Document Version**: 1.0
**Maintained By**: AI Assistants working on GenesisRevelationInc repository

## How to Use This Guide

This document serves as a comprehensive reference for AI assistants (like Claude) working on the GenesisRevelationInc codebase. When starting work:

1. **Read this entire document** to understand project context
2. **Check recent commits** to understand current development focus
3. **Review coding conventions** before making changes
4. **Follow testing checklist** before committing
5. **Update this document** if you discover new patterns or conventions

**Remember**: This is a ministry website. Maintain professionalism, respect the mission, and prioritize accessibility and performance for all users.
