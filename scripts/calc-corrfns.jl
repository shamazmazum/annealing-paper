#!/usr/bin/env julia

using CorrelationFunctions
using ArgParse
using DelimitedFiles
using Statistics

const functions_dir = [
    (Directional.s2, false, "s2diff"),
    (Directional.c2, true,  "c2diff"),
    (Directional.l2, false, "l2vdiff"),
    (Directional.l2, true,  "l2sdiff"),

    (Directional.surfsurf, false, "ssdiff"),
    (Directional.surfvoid, false, "svdiff")
]

const functions_map = [
    (Map.s2, "s2diff-map"),

    (Map.surfsurf, "ssdiff-map"),
#    (Map.surfvoid, "svdiff-map"),
]

function parse_commandline()
    s = ArgParseSettings()

    @add_arg_table! s begin
        "--size"
        help     = "Size of the input"
        arg_type = Int
        default  = 500
        "first"
        help     = "The first image"
        required = true
        "second"
        help     = "The second image"
        required = true
        "directory"
        help     = "Directory for the output"
        required = true
    end

    return parse_args(s)
end

function calc_difference(fn     :: Function,
                         phase  :: Bool,
                         image1 :: AbstractArray{Bool, N},
                         image2 :: AbstractArray{Bool, N}) where N
    cf1 = fn(image1, phase; periodic = true, directions = [:x, :y, :xy, :yx]) |> mean
    cf2 = fn(image2, phase; periodic = true, directions = [:x, :y, :xy, :yx]) |> mean
    return cf1 .- cf2
end

function calc_difference_map(fn     :: Function,
                             image1 :: AbstractArray{Bool, N},
                             image2 :: AbstractArray{Bool, N}) where N
    cf1 = fn(image1; periodic = true) |> Map.restore_full_map
    cf2 = fn(image2; periodic = true) |> Map.restore_full_map
    return cf1 .- cf2
end

function do_all()
    arguments = parse_commandline()

    name1     = arguments["first"]
    name2     = arguments["second"]
    s         = arguments["size"]
    directory = arguments["directory"]

    image1 = read_cuboid(name1, s, 2) |> BitArray
    image2 = read_cuboid(name2, s, 2) |> BitArray

    for (fn, phase, name) in functions_dir
        diff = calc_difference(fn, phase, image1, image2)
        path = joinpath(directory, "$(name).dat")
        open(path, "w") do io
            writedlm(io, diff)
        end
    end

    for (fn, name) in functions_map
        diff = calc_difference_map(fn, image1, image2)
        path = joinpath(directory, "$(name).dat")
        open(path, "w") do io
            write(io, Float64.(diff))
        end
    end
end

do_all()
