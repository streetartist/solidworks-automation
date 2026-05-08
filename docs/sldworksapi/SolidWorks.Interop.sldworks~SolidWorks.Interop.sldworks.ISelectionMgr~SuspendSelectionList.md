# SuspendSelectionList Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SuspendSelectionList`

Suspends the current selection list.
Suspends the current selection list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SuspendSelectionList() As System.Integer
```

```

Dim instance As ISelectionMgr
Dim value As System.Integer
 
value = instance.SuspendSelectionList()
```

```

System.int SuspendSelectionList()
```

```

System.int SuspendSelectionList(); 
```

#### Return Value

0 if the suspended list is empty, 1 if not

Remarks

To add objects to a selection list without preselecting the objects in the user interface:

1. Call ISelectionMgr::SuspendSelectionList to suspend the current selection list, preserving its contents and starting a new selection list.
2. To populate a new selection list, call [ISelectionMgr::AddSelectionListObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObject.md) or [ISelectionMgr::AddSelectionListObjects](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.md).  
     
   **NOTE**: To add objects in a [selection set](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.md) to a new selection list, call [ISelectionSet::Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~Select.md).
3. Call [ISelectionMgr::ResumeSelectionList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList.md) to reinstate the suspended selection list.

To programmatically preselect objects in the user interface and add them to a selection list, use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

[IModelDoc2::ClearSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2.md) works like ISelectionMgr::SuspendSelectionList to clear the selection list. Unlike IModelDoc2::ClearSelection2, this method preserves the list for future reinstatement.

Example

[Add Objects to Selection List (C#)](Add_Objects_to_Selection_List_Example_CSharp.htm)  
[Add Objects to Selection List (VB.NET)](Add_Objects_to_Selection_List_Example_VBNET.htm)  
[Add Objects to Selection List (VBA)](Add_Objects_to_Selection_List_Example_VB.htm)  
[Get Objects in Selection List (C#)](Get_Objects_in_Selection_Set_Example_CSharp.htm)  
[Get Objects in Selection List (VB.NET)](Get_Objects_in_Selection_Set_Example_VBNET.htm)  
[Get Objects in Selection List (VBA)](Get_Objects_in_Selection_Set_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)
