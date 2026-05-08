# Select Method (ISelectionSet)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~Select`

Selects all of the objects in this selection set.
Selects all of the objects in this selection set.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select() As System.Boolean
```

```

Dim instance As ISelectionSet
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

True if all of the objects in this selection set are selected, false if not (see **Remarks**)

Remarks

To use this method:

1. Call [ISelectionMgr::SuspendSelectionList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SuspendSelectionList.md) to suspend the current selection list, preserving its contents and starting a new selection list.
2. Call ISelectionSet::Select to add the objects in the selection set to the new selection list.
3. Process the objects in the new selection list.
4. Call [ISelectionMgr::ResumeSelectionList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList.md) to reinstate the suspended selection list.

Example

[Get Objects in Selection Set (C#)](Get_Objects_in_Selection_Set_Example_CSharp.htm)  
[Get Objects in Selection Set (VB.NET)](Get_Objects_in_Selection_Set_Example_VBNET.htm)  
[Get Objects in Selection Set (VBA)](Get_Objects_in_Selection_Set_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionSet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.md)  
[ISelectionSet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet_members.md)
