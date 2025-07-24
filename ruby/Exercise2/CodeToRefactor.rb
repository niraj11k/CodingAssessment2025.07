require 'date'

module Refactor
  class People
    UNDER_16 = DateTime.now - (15 * 365)
    
    attr_reader :name, :dob
    
    def initialize(name, dob = nil)
      @name = name
      @dob = dob || UNDER_16
    end
  end

  class BirthingUnit
    # MaxItemsToRetrieve
    def initialize
      @people = []
    end

    # GetPeoples
    # @param j
    # @return Array<Object>
    def get_people(i)
      i.times do |j|
        begin
          # Creates a dandon Name
          name = ""
          if rand(0..1) == 0
            name = "Bob"
          else
            name = "Betty"
          end
          # Adds new people to the list
          @people << People.new(name, DateTime.now - (rand(18..85) * 356))
        rescue => e
          # Dont think this should ever happen
          raise "Something failed in user creation"
        end
      end
      @people
    end

    private

    def get_bobs(older_than_30)
      if older_than_30
        @people.select { |x| x.name == "Bob" && x.dob >= (DateTime.now - (30 * 356)) }
      else
        @people.select { |x| x.name == "Bob" }
      end
    end

    public

    def get_married(p, last_name)
      return p.name if last_name.include?("test")
      
      if (p.name.length + last_name).length > 255
        (p.name + " " + last_name)[0, 255]
      end

      p.name + " " + last_name
    end
  end
end
