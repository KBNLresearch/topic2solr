#!/usr/bin/ruby

require 'rubygems'
require 'sinatra'
require 'json'
require 'mongo'

@@client = Mongo::Connection.new
@@db = @@client['topics']
@@coll = @@db['topic1']

@@totals = false;
@@stats = {}
@@keywords = [
	"arbeid",
	"bedrijf",
	"beheer",
	"controle",
	"economische",
	"factoren",
	"functies",
	"kosten",
	"leiding",
	"loon",
	"maatregelen",
	"management",
	"methode",
	"model",
	"normen",
	"organisatie",
	"plannen",
	"prijs",
	"productie",
	"rationeel",
	"rendement",
	"reorganisatie",
	"resultaten",
	"rol",
	"statistiek",
	"taylor",
	"tijd",
	"verantwoordelijkheid",
	"verdeeling",
	"werk",
	"werkbesparing",
	"werkverdeeling",
	"wetenschappelijke"
]

get '/stats' do
	content_type :json
	@@stats[params[:amt]] = @@coll.aggregate([
            {"$match" => {"tok_amount" => {"$gte" => params[:amt].to_i}}},
            {"$group" => {"_id" => "$year", "total" => {"$sum" => 1}}}
        ]) unless @@stats.has_key?(params[:amt])
	return JSON(@@stats[params[:amt]])
end

get '/wordstats' do
	content_type :json
	return JSON(@@coll.aggregate([
		{"$match" => {"tokens" => {"$all" => params[:words]}}},
		{"$group" => {"_id" => "$year", "total" => {"$sum" => 1}}}
	]))
end


get "/totals" do
	content_type :json
	@@totals = @@coll.find({"total_year" => {"$exists" => true}}).to_a if @@totals == false
	return JSON(@@totals)
end

get "/" do
	erb :index
end
