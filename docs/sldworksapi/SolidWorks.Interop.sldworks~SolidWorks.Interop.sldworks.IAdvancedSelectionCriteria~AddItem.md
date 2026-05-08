# AddItem Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~AddItem`

Obsolete. Superseded by IAdvancedSelectionCriteria::AddItem2.
Obsolete. Superseded by [IAdvancedSelectionCriteria::AddItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~AddItem2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddItem( _
   ByVal Property As System.String, _
   ByVal Condition As System.Integer, _
   ByVal Value As System.String, _
   ByVal IsAnd As System.Boolean _
) As System.Integer
```

```

Dim instance As IAdvancedSelectionCriteria
Dim Property As System.String
Dim Condition As System.Integer
Dim Value As System.String
Dim IsAnd As System.Boolean
Dim value As System.Integer
 
value = instance.AddItem(Property, Condition, Value, IsAnd)
```

```

System.int AddItem( 
   System.string Property,
   System.int Condition,
   System.string Value,
   System.bool IsAnd
)
```

```

System.int AddItem( 
   System.String^ Property,
   System.int Condition,
   System.String^ Value,
   System.bool IsAnd
) 
```

#### Parameters

*Property*
:   Name of property

*Condition*
:   Condition as defined in [swAdvSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAdvSelectType_e.html)

*Value*
:   Text of the value

*IsAnd*
:   True if all of the criteria in the advanced component selection list must be met, false if only this criteria in the advanced component selection list must be met

#### Return Value

Index number of the newly added criteria in the advanced component selection list

Example

[Use Advanced Component Selection (VBA)](Use_Advanced_Component_Selection_Example_VB.htm)  
[Use Advanced Component Selection (VB.NET)](Use_Advanced_Component_Selection_Example_VBNET.htm)  
[Use Advanced Component Selection (C#)](Use_Advanced_Component_Selection_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md)  
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.md)
