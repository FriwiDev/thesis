import json
import pathlib
import typing
from os import PathLike

methods = ["get", "post", "put", "delete"]
checkmark = "\\ding{51}"
cross = "\\ding{55}"


def process(in_file: pathlib.Path):
    print(f"Processing {str(in_file)}")
    out = open(in_file.name.replace(".json", "") + ".tex", "w")
    obj = json.load(open(in_file, "r"))
    name = in_file.name.replace(".json", "").lower()

    # Heading
    out.write("\\section{" + escape(obj["info"]["title"]) + "}\n")
    out.write("\\label{spec_" + obj["info"]["title"].lower() + "}\n")
    out.write("\n")

    # Description
    out.write(escape(obj["info"]["description"]) + "\n\n")

    # Build categories
    categories = {}  # Tag -> (path, method)
    for path in obj["paths"].keys():
        for method in obj["paths"][path].keys():
            if method.lower() in methods:
                for tag in obj["paths"][path][method]["tags"]:
                    if tag in categories.keys():
                        categories[tag].append((path, method))
                    else:
                        categories[tag] = [(path, method)]

    # Print categories
    for category in categories.keys():
        out.write("\\subsection{" + category + "}\n")
        for path, method in categories[category]:
            # Print one endpoint
            endpoint = obj["paths"][path][method]

            # Title
            out.write("\\subsubsection{" + method.upper() + " " + escape(path) + "}\n")

            # Description
            out.write(escape(endpoint["description"]) + "\n")

            # Parameters
            out.write(
                "\\begin{longtable}{ |p{2.5cm}|p{1.5cm}|p{4cm}|p{2cm}| }\n\\hline\n")
            out.write("\\multicolumn{4}{|c|}{\\textbf{Parameters}} \\\\\n \\hline \n")

            parameters = []
            if "parameters" in obj["paths"][path].keys():
                for param in obj["paths"][path]["parameters"]:
                    parameters.append(param)
            if "parameters" in endpoint.keys():
                for param in endpoint["parameters"]:
                    parameters.append(param)

            if len(parameters) == 0:
                out.write("\\multicolumn{4}{|p{11.34cm}|}{\\centering{\\textit{No parameters}}} \\\\\n \\hline \n")
            else:
                out.write("\\textbf{Name} & \\centering{\\textbf{Location}} & \\textbf{Description} & "
                          "\\textbf{Type} \\\\\n")
                out.write("\\hline \n")
                # Print each parameter
                for param in parameters:
                    #required = True if "required" not in param.keys() else param["required"]
                    out.write(escape(param["name"]) + " & \\centering{" +
                              escape(param["in"]).upper() + "} & " +
                              #(checkmark if required else cross) + "} & " +
                              escape(param["description"]) + " & " +
                              get_data_type(name, obj, param["schema"]) +
                              ("" if "example" not in param.keys() else ", e.g. " + escape(param["example"])) +
                              " \\\\\n \\hline \n")

            # End of parameters
            out.write("\\endhead \\end{longtable} \n")
            out.write("\n")

            # Request body
            out.write("\\begin{longtable}{ |p{3cm}|p{7.88cm}| }\n\\hline\n")
            out.write("\\multicolumn{2}{|c|}{\\textbf{Request Body}} \\\\\n \\hline \n")

            if "requestBody" not in endpoint.keys():
                out.write("\\multicolumn{2}{|p{11.34cm}|}{\\centering{\\textit{No request body}}} \\\\\n \\hline \\endhead \n")
            else:
                out.write("\\textbf{Content Type} & \\textbf{Data Type} \\\\\n")
                out.write("\\hline \n")
                first = True
                for t in endpoint["requestBody"]["content"].keys():
                    body = endpoint["requestBody"]["content"][t]
                    listings = build_lstlstings(get_data_type_structure_json(obj, body["schema"]))
                    for lst in listings:
                        if first:
                            out.write(escape(t) + " & " +
                                      get_data_type(name, obj, body["schema"]) +
                                      # lst +
                                      " \\\\\n \\hline \n")
                            first = False
                        else:
                            #out.write("\\pagebreak\n")
                            #out.write("\\hline\n")
                            #out.write("~ & " +
                                      # lst +
                            #          " \\\\\n \\hline \n")
                            pass
            # End of request body
            out.write("\\end{longtable} \n")
            out.write("\n")

            # Responses
            out.write("\\begin{longtable}{ |p{1.0cm}|p{3cm}|p{6.44cm}| }\n\\hline\n")
            out.write("\\multicolumn{3}{|c|}{\\textbf{Responses}} \\\\\n \\hline \n")
            out.write(
                "\\centering{\\textbf{Code}} & \\centering{\\textbf{Content Type}} & \\textbf{Description, Data Type} \\\\\n")
            out.write("\\hline \n")

            if "responses" not in endpoint.keys():
                out.write("\\multicolumn{3}{|c|}{\\textit{No responses}} \\\\\n \\hline \n")  # Should never happen
            else:
                codes = [int(x) for x in endpoint["responses"].keys()]
                codes.sort()
                first = True
                for code in codes:
                    code = str(code)
                    description = endpoint["responses"][code]["description"]
                    if "content" in endpoint["responses"][code].keys():
                        for t in endpoint["responses"][code]["content"].keys():
                            body = endpoint["responses"][code]["content"][t]
                            out.write("\\centering{" + escape(code) + "} & " +
                                      "\\centering{" + escape(t) + "} & " +
                                      description + "\n\n" +
                                      "\\paragraph{Data} " +
                                      get_data_type(name, obj, body["schema"]) +
                                      #"\\begin{lstlisting}[language=bash]\n" +
                                      #get_data_type_structure_json(obj, body["schema"])
                                      #+ "\n\\end{lstlisting}" +
                                      " \\\\\n \\hline \n")
                    else:
                        out.write("\\centering{"+escape(code) + "} & " +
                                  "\\centering{text/plain}" + " & " +
                                  description +
                                  " \\\\\n \\hline \n")
                    if first:
                        first = False
                        out.write("\\endhead\n")
            # End of request body
            out.write("\\end{longtable} \n")
            out.write("\n")

            out.write("\\newpage\n")

    # Print schemas
    out.write("\\subsection{Schemas}\n\n")

    keys = []
    for k in obj["components"]["schemas"].keys():
        keys.append(k)
    keys.sort()
    for k in keys:
        schema = obj["components"]["schemas"][k]
        out.write("\\subsubsection{Schema " + escape(k) + ":}\n\\label{" + name + "_" + k.lower() + "}\n")
        if "description" in schema.keys():
            #out.write("\\begin{codes} \n")
            out.write(escape(schema["description"]) + "\n")
            #out.write("\\end{codes} \n")
        out.write("\\begin{codes}\n")
        out.write("\\item[Structure] \\begin{lstlisting}[language=bash]\n" +
                  get_data_type_structure_json(obj, schema) +
                  "\n\\end{lstlisting} \n")
        out.write("\\end{codes} \n")
        out.write("\\begin{codes}\n")
        out.write("\\item[Example] \\begin{lstlisting}[language=bash]\n" +
                  get_data_example_structure_json(obj, schema) +
                  "\n\\end{lstlisting}\n")
        out.write("\\end{codes} \n")
        out.write("\n")
        out.write("\\newpage\n")

    out.close()


def main(in_dict: PathLike):
    print(f"Processing from {str(in_dict)}")
    process(pathlib.Path(in_dict).joinpath("esmf.json"))
    process(pathlib.Path(in_dict).joinpath("dsmf.json"))
    process(pathlib.Path(in_dict).joinpath("ctmf.json"))
    process(pathlib.Path(in_dict).joinpath("dtmf.json"))
    process(pathlib.Path(in_dict).joinpath("controller.json"))
    process(pathlib.Path(in_dict).joinpath("vpn_gateway.json"))
    process(pathlib.Path(in_dict).joinpath("switch.json"))


def build_lstlstings(src: str) -> [str]:
    lines_per = 35
    spl = src.split("\n")
    i = 0
    ret = []
    build = "\\begin{lstlisting}[language=bash]\n"
    for s in spl:
        build += s + "\n"
        i += 1
        if i % lines_per == 0:
            build += "\\end{lstlisting}"
            ret.append(build)
            build = "\\begin{lstlisting}[language=bash, firstnumber="+str(i+1)+"]\n"
    if i % lines_per != 0:
        build += "\\end{lstlisting}"
        ret.append(build)
    return ret


def get_data_type(name, obj, schema) -> str:
    if "format" in schema.keys():
        return schema["type"] + "/" + schema["format"]
    if "$ref" in schema.keys():
        ref = schema["$ref"].replace("#/", "").split("/")
        return "\\hyperref[" + name + "_" + ref[len(ref) - 1] + "]{" + escape(ref[len(ref) - 1]) + "}"
    if "oneOf" in schema.keys():
        types = schema["oneOf"]
        return " \\textit{OR} ".join([get_data_type(name, obj, x) for x in types])
    if schema["type"].lower() == "array":
        return "[" + get_data_type(name, obj, schema["items"]) + "]"
    if schema["type"].lower() == "object":
        if "additionalProperties" in schema.keys():
            if isinstance(schema["additionalProperties"], dict):
                return get_data_type(name, obj, schema["additionalProperties"])
    return schema["type"].lower()


def get_data_type_structure_json(obj, schema) -> str:
    d = get_data_type_structure(obj, schema)
    if isinstance(d, str):
        return "\"str\"" if d == "str" else d
    return json.dumps(d, indent=2)


def get_data_example_structure_json(obj, schema) -> str:
    d = get_data_example_structure(obj, schema)
    if isinstance(d, str):
        return "\"str\"" if d == "str" else d
    return json.dumps(d, indent=2)


def get_data_type_structure(obj, schema) -> typing.Any:
    if "format" in schema.keys():
        return "int"
    if "$ref" in schema.keys():
        ref = schema["$ref"].replace("#/", "").split("/")
        schema = obj
        for x in ref:
            schema = schema[x]
        return get_data_type_structure(obj, schema)
    if "oneOf" in schema.keys():
        types = schema["oneOf"]
        return " | ".join([get_data_type_structure_json(obj, x) for x in types])
    if schema["type"].lower() == "array":
        return [get_data_type_structure(obj, schema["items"])]
    if schema["type"].lower() == "string":
        return "str"
    if schema["type"].lower() == "integer":
        return "int"
    if schema["type"].lower() == "object":
        if "properties" in schema.keys():
            ret = {}
            properties = schema["properties"]
            for x in properties.keys():
                ret[x] = get_data_type_structure(obj, properties[x])
            return ret
        if "additionalProperties" in schema.keys():
            if isinstance(schema["additionalProperties"], dict):
                return get_data_type_structure(obj, schema["additionalProperties"])
            else:
                return {}
    raise Exception("Unknown data type: " + schema["type"] + " from " + str(schema))


def get_data_example_structure(obj, schema) -> typing.Any:
    if "example" in schema.keys():
        return schema["example"]
    if "format" in schema.keys():
        return "0"
    if "$ref" in schema.keys():
        ref = schema["$ref"].replace("#/", "").split("/")
        schema = obj
        for x in ref:
            schema = schema[x]
        return get_data_example_structure(obj, schema)
    if "oneOf" in schema.keys():
        types = schema["oneOf"]
        return " | ".join([get_data_example_structure_json(obj, x) for x in types])
    if schema["type"].lower() == "array":
        return [get_data_example_structure(obj, schema["items"])]
    if schema["type"].lower() == "string":
        return "example"
    if schema["type"].lower() == "integer":
        return "0"
    if schema["type"].lower() == "object":
        if "properties" in schema.keys():
            ret = {}
            properties = schema["properties"]
            for x in properties.keys():
                ret[x] = get_data_example_structure(obj, properties[x])
            return ret
        if "additionalProperties" in schema.keys():
            if isinstance(schema["additionalProperties"], dict):
                return get_data_example_structure(obj, schema["additionalProperties"])
            else:
                return {}
    raise Exception("Unknown data type: " + schema["type"] + " from " + str(schema))


def escape(text: str):
    # HTML link to url
    if text.__contains__("<a href=\""):
        first = text.split("<a href=\"")[0]
        j = text.split("<a href=\"")
        j.pop(0)
        last = "<a href=\"".join(j)
        url = last.split("\">")[1].split("</a>")[0]
        caption = last.split("\">")[0]
        j = last.split("</a>")
        j.pop(0)
        last = "</a>".join(j)
        return escape(first) + "\\href{" + escape(caption) + "}{" + escape(url) + "}" + escape(last)
    return (text.replace("_", "\\_")
            .replace("{", "\\{")
            .replace("}", "\\}"))


main(pathlib.Path("..").absolute())
