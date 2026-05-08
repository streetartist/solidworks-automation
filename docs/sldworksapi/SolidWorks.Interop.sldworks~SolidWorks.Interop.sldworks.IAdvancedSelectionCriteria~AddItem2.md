# AddItem2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~AddItem2`

Adds the specified advanced component selection criterion to the list.
Adds the specified advanced component selection criterion to the list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddItem2( _
   ByVal Category1 As System.String, _
   ByVal Category2 As System.String, _
   ByVal Condition As System.Integer, _
   ByVal Value As System.String, _
   ByVal IsAnd As System.Boolean _
) As System.Integer
```

```

Dim instance As IAdvancedSelectionCriteria
Dim Category1 As System.String
Dim Category2 As System.String
Dim Condition As System.Integer
Dim Value As System.String
Dim IsAnd As System.Boolean
Dim value As System.Integer
 
value = instance.AddItem2(Category1, Category2, Condition, Value, IsAnd)
```

```

System.int AddItem2( 
   System.string Category1,
   System.string Category2,
   System.int Condition,
   System.string Value,
   System.bool IsAnd
)
```

```

System.int AddItem2( 
   System.String^ Category1,
   System.String^ Category2,
   System.int Condition,
   System.String^ Value,
   System.bool IsAnd
) 
```

#### Parameters

*Category1*
:   Name of Category1 (see **Remarks**)

*Category2*
:   Name of Category2 (see **Remarks**)

*Condition*
:   Condition as defined in [swAdvSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAdvSelectType_e.html) (see **Remarks**)

*Value*
:   Text value satisfying Condition (see **Remarks**)

*IsAnd*
:   True if all of the criteria in the advanced component selection list must be met, false if only this criteria in the advanced component selection list must be met

#### Return Value

Index number of the newly added criterion in the advanced component selection criteria list

Remarks

For a list of possible Category1, Category2, Condition, and Value values, see the **Assemblies > Basic Component Operations > Selecting Components > Advanced Component Selection > Search Criteria for Advanced Component Selection** topic in the SOLIDWORKS user-interface help.

After calling this method multiple times to add criteria:

- [Save](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~SaveCriteria.md) the criteria.
- [Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~Select.md) the components satisfying the criteria.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md)  
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.md)
