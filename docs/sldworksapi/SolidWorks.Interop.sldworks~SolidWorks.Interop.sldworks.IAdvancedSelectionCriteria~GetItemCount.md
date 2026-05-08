# GetItemCount Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~GetItemCount`

Gets the number of criteria in the advanced component selection criteria list.
Gets the number of criteria in the advanced component selection criteria list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetItemCount() As System.Integer
```

```

Dim instance As IAdvancedSelectionCriteria
Dim value As System.Integer
 
value = instance.GetItemCount()
```

```

System.int GetItemCount()
```

```

System.int GetItemCount(); 
```

#### Return Value

Number of criteria in the advanced component selection criteria list

Remarks

Call this method before calling [IAdvancedSelectionCriteriaClass::GetItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~GetItem.md) and [IAdvancedSelectionCriteriaClass::DeleteItem](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~DeleteItem.md) to get the number of criteria in the advanced component selection criteria list.

Example

See the [IAdvancedSelectionCriteria](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md)  
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.md)
