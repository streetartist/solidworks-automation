# DeleteItem Method (IAdvancedSelectionCriteria)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~DeleteItem`

Deletes a criteria from the advanced component selection list.
Deletes a criteria from the advanced component selection list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function DeleteItem( _
   ByVal Index As System.Integer _
) As System.Boolean
```

```

Dim instance As IAdvancedSelectionCriteria
Dim Index As System.Integer
Dim value As System.Boolean
 
value = instance.DeleteItem(Index)
```

```

System.bool DeleteItem( 
   System.int Index
)
```

```

System.bool DeleteItem( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Index number of the criteria to delete

#### Return Value

True if criteria is deleted, false if not

Remarks

Call [IAdvancedSelectionCriteria::GetItemCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~GetItemCount.md) to get a valid value for Index before calling this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md)  
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.md)
