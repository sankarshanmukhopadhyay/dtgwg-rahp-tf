# frozen_string_literal: true

require "yaml"
require "json"

module RahpPagesProjection
  STRUCTURED_ROOTS = %w[corpora method data build/derived build/jsonld examples].freeze
  STRUCTURED_EXTENSIONS = %w[.yaml .yml .json .jsonld].freeze
  MARKDOWN_ROOTS = %w[examples build].freeze
  TOP_LEVEL_MARKDOWN = %w[README.md ADOPTION.md QUICKSTART.md CONTRIBUTING.md ROADMAP.md CHANGELOG.md].freeze

  class ProjectionPage < Jekyll::Page
    def initialize(site, relative_path, title, body)
      @site = site
      @base = site.source
      @dir = File.dirname(relative_path)
      @dir = "" if @dir == "."
      # Use a Markdown source extension internally so Jekyll runs the Markdown converter,
      # but publish to the original repository path through permalink.
      @name = "#{File.basename(relative_path)}.md"
      process(@name)
      self.data = {
        "layout" => "default",
        "title" => title,
        "has_toc" => true,
        "nav_exclude" => true,
        "permalink" => "/#{relative_path}"
      }
      self.content = body
    end
  end

  class Generator < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
      rendered_relpaths = []
      structured_files(site).each do |path|
        relative = relative_path(site, path)
        raw = File.read(path)
        parsed = parse_structured(path, raw)
        next if parsed.nil?
        title = structured_title(relative, parsed)
        site.pages << ProjectionPage.new(site, relative, title, structured_body(site, relative, parsed, raw))
        rendered_relpaths << "/#{relative}"
      end

      markdown_files(site).each do |path|
        raw = File.read(path)
        next if raw.start_with?("---\n") # already a normal Jekyll page
        relative = relative_path(site, path)
        site.pages << ProjectionPage.new(site, relative, markdown_title(relative, raw), markdown_body(site, relative, raw))
        rendered_relpaths << "/#{relative}"
      end

      site.static_files.reject! { |file| rendered_relpaths.include?(file.relative_path) }
      Jekyll.logger.info "RAHP Pages projection:", "rendered #{rendered_relpaths.length} repository files"
    end

    private

    def structured_files(site)
      STRUCTURED_ROOTS.flat_map do |root|
        absolute_root = File.join(site.source, root)
        next [] unless Dir.exist?(absolute_root)
        Dir.glob(File.join(absolute_root, "**", "*")).select do |path|
          File.file?(path) && STRUCTURED_EXTENSIONS.include?(File.extname(path).downcase)
        end
      end
    end

    def markdown_files(site)
      paths = TOP_LEVEL_MARKDOWN.map { |name| File.join(site.source, name) }.select { |path| File.file?(path) }
      MARKDOWN_ROOTS.each do |root|
        absolute_root = File.join(site.source, root)
        next unless Dir.exist?(absolute_root)
        paths.concat(Dir.glob(File.join(absolute_root, "**", "*.md")).select { |path| File.file?(path) })
      end
      paths.uniq
    end

    def relative_path(site, path)
      path.delete_prefix(site.source + File::SEPARATOR)
    end

    def parse_structured(path, raw)
      case File.extname(path).downcase
      when ".yaml", ".yml"
        YAML.safe_load(raw, aliases: true)
      when ".json", ".jsonld"
        JSON.parse(raw)
      end
    rescue StandardError => e
      Jekyll.logger.warn "RAHP Pages projection:", "skipping #{path}: #{e.message}"
      nil
    end

    def structured_title(path, parsed)
      if parsed.is_a?(Hash) && parsed["corpus"].is_a?(Hash)
        parsed["corpus"]["title"] || File.basename(path)
      else
        File.basename(path)
      end
    end

    def markdown_title(path, raw)
      heading = raw.each_line.find { |line| line.start_with?("# ") }
      heading ? heading.sub(/^#\s+/, "").strip : File.basename(path)
    end

    def source_button(site, path)
      "[View canonical source on GitHub](https://github.com/#{site.config['repository']}/blob/main/#{path}){: .btn .btn-primary }"
    end

    def markdown_body(site, path, raw)
      <<~MD
        > This GitHub Pages view renders the repository Markdown at `#{path}`. The GitHub repository remains the canonical source.

        #{source_button(site, path)}

        #{raw}
      MD
    end

    def structured_body(site, path, parsed, raw)
      lines = []
      lines << "# #{structured_title(path, parsed)}"
      lines << ""
      lines << "> This is a human-readable GitHub Pages projection of the canonical structured source at `#{path}`. The repository source remains the authoritative machine-readable record."
      lines << ""
      lines << source_button(site, path)
      lines << ""
      if parsed.is_a?(Hash) && parsed["corpus"].is_a?(Hash)
        lines.concat(corpus_summary(parsed["corpus"]))
      else
        lines.concat(generic_summary(parsed))
      end
      lines << ""
      lines << "## Canonical source"
      lines << ""
      language = File.extname(path).sub(".", "")
      language = "yaml" if %w[yaml yml].include?(language)
      lines << "```#{language}"
      lines << raw.rstrip
      lines << "```"
      lines.join("\n")
    end

    def corpus_summary(corpus)
      scenarios = Array(corpus["scenarios"])
      out = ["## Corpus metadata", "", "| Field | Value |", "|---|---|"]
      %w[id source_repository source_path source_commit adapter_version description].each do |key|
        next unless corpus.key?(key)
        out << "| `#{key}` | #{escape_cell(corpus[key])} |"
      end
      out << "| `scenario_count` | #{scenarios.length} |"
      unless scenarios.empty?
        out += ["", "## Scenarios", "", "| ID | Title | Domain | Pressure | Priority | RAHP patterns |", "|---|---|---|---|---|---|"]
        scenarios.each do |scenario|
          patterns = Array(scenario["scenario_patterns"]).map { |v| "`#{v}`" }.join(", ")
          out << "| `#{scenario['id']}` | #{escape_cell(scenario['title'])} | #{escape_cell(scenario['domain'])} | #{escape_cell(scenario['primary_pressure'])} | #{escape_cell(scenario['priority'])} | #{patterns} |"
        end
      end
      out
    end

    def generic_summary(parsed)
      out = ["## Structured-data overview", ""]
      case parsed
      when Hash
        out << "Top-level keys: #{parsed.keys.map { |k| "`#{k}`" }.join(', ')}."
      when Array
        out << "This record contains **#{parsed.length}** top-level entries."
      else
        out << "This structured record is rendered below exactly as stored."
      end
      out
    end

    def escape_cell(value)
      value.to_s.gsub("|", "\\|").gsub("\n", " ")
    end
  end
end
