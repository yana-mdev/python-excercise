def list_roman_emperors(*args, **kwargs):
    successful_imperators = {}
    unsuccessful_imperators = {}

    for name, success_status in args:
        if success_status:
            successful_imperators[name] = kwargs[name]
        else:
            unsuccessful_imperators[name] = kwargs[name]

    sorted_successful_imperators = sorted(successful_imperators.items(), key=lambda x: (-x[1], x[0]))
    sorted_unsuccessful_imperators = sorted(unsuccessful_imperators.items(),key=lambda x: (x[1], x[0]))

    result = [f"Total number of emperors: {len(args)}"]
    if sorted_successful_imperators:
        result.append("Successful emperors:")
        for name, years in sorted_successful_imperators:
            result.append(f"****{name}: {years}")

    if sorted_unsuccessful_imperators:
        result.append("Unsuccessful emperors:")
        for name, years in sorted_unsuccessful_imperators:
            result.append(f"****{name}: {years}")

    return "\n".join(result)