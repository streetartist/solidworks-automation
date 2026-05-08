# GetItem Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~GetItem`

Obsolete. Superseded by IAdvancedSelectionCriteria::GetItem2.
Obsolete. Superseded by [IAdvancedSelectionCriteria::GetItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~GetItem2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetItem( _
   ByVal Index As System.Integer, _
   ByRef Property As System.String, _
   ByRef Condition As System.Integer, _
   ByRef Value As System.String, _
   ByRef IsAnd As System.Boolean _
) As System.Integer
```

```

Dim instance As IAdvancedSelectionCriteria
Dim Index As System.Integer
Dim Property As System.String
Dim Condition As System.Integer
Dim Value As System.String
Dim IsAnd As System.Boolean
Dim value As System.Integer
 
value = instance.GetItem(Index, Property, Condition, Value, IsAnd)
```

```

System.int GetItem( 
   System.int Index,
   out System.string Property,
   out System.int Condition,
   out System.string Value,
   out System.bool IsAnd
)
```

```

System.int GetItem( 
   System.int Index,
   [Out] System.String^ Property,
   [Out] System.int Condition,
   [Out] System.String^ Value,
   [Out] System.bool IsAnd
) 
```

#### Parameters

*Index*
:   Index number of the criteria in the advanced component selection list

*Property*
:   Name of property

*Condition*
:   Condition as defined in [swAdvSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAdvSelectType_e.html)

*Value*
:   Text of the value

*IsAnd*
:   True if all of the criteria in the advanced component selection list must be met, false if only this criteria in the advanced component selection list must be met

#### Return Value

Value of the Index argument or -1 if criteria specified by Index not found

Remarks

Call [IAdvancedSelectionCriteria::GetItemCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~GetItemCount.md) to get a valid value for Index before calling this method.

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
