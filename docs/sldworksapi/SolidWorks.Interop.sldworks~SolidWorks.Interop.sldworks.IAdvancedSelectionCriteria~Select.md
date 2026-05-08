# Select Method (IAdvancedSelectionCriteria)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~Select`

Selects the assembly components that satisfy the current advanced selection criteria.
Selects the assembly components that satisfy the current advanced selection criteria.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select() As System.Boolean
```

```

Dim instance As IAdvancedSelectionCriteria
Dim value As System.Boolean
 
value = instance.Select()
```

```

System.bool Select()
```

```

System.bool Select(); 
```

#### Return Value

True if the components are selected, false if not

Remarks

Call this method after either:

- [Loading](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~LoadCriteria.md) the criteria from a **\*.xml** file or a **\*.sqy** legacy file.

    - or -

- [Adding](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria~AddItem2.md) items to the advanced component selection criteria list.

Example

See the [IAdvancedSelectionCriteria](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSelectionCriteria Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria.md)  
[IAdvancedSelectionCriteria Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.md)
