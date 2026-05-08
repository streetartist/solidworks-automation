# GetItem2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~GetItem2`

Gets the specified advanced component selection criterion.
Gets the specified advanced component selection criterion.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetItem2( _
   ByVal Index As System.Integer, _
   ByRef Category1 As System.String, _
   ByRef Category2 As System.String, _
   ByRef Condition As System.Integer, _
   ByRef Value As System.String, _
   ByRef IsAnd As System.Boolean _
) As System.Integer
```

```

Dim instance As IAdvancedSelectionCriteria
Dim Index As System.Integer
Dim Category1 As System.String
Dim Category2 As System.String
Dim Condition As System.Integer
Dim Value As System.String
Dim IsAnd As System.Boolean
Dim value As System.Integer
 
value = instance.GetItem2(Index, Category1, Category2, Condition, Value, IsAnd)
```

```

System.int GetItem2( 
   System.int Index,
   out System.string Category1,
   out System.string Category2,
   out System.int Condition,
   out System.string Value,
   out System.bool IsAnd
)
```

```

System.int GetItem2( 
   System.int Index,
   [Out] System.String^ Category1,
   [Out] System.String^ Category2,
   [Out] System.int Condition,
   [Out] System.String^ Value,
   [Out] System.bool IsAnd
) 
```

#### Parameters

*Index*
:   Index number of the criterion to retrieve

*Category1*
:   Name of Category1 (see **Remarks**)

*Category2*
:   Name of Category2 (see **Remarks**)

*Condition*
:   Condition as defined in [swAdvSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAdvSelectType_e.html) (see **Remarks**)

*Value*
:   Text value satisfying Condition (see **Remarks**)

*IsAnd*
:   True if all of the criteria in the advanced component selection criteria list must be met, false if only this criterion must be met

#### Return Value

Value of the Index argument or -1 if criterion specified by Index not found

Remarks

Call [IAdvancedSelectionCriteria::GetItemCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~GetItemCount.md) to get a valid value for Index before calling this method.

For a list of possible Category1, Category2, Condition, and Value values, see **Assemblies > Basic Component Operations > Selecting Components > Advanced Component Selection > Search Criteria for Advanced Component Selection** topic in the SOLIDWORKS user-interface help.

Example

See the [IAdvancedSelectionCriteria](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md)  
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.md)
