using System.Collections.Generic;

namespace Company.Function
{
    public class ResultContract
    {
        public string FirstName;
        public string LastName;

        public class ProgramResult
        {
            public string ProgramName;
            public string CourseName;
            public string Grade;
            public string Score;
            public string Result;
        }

        public List<ProgramResult> Results = new List<ProgramResult>();
    }
}
