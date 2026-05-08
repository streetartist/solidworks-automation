# ResumeSelectionList Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList`

Obsolete. Superseded by ISelectionMgr::ResumeSelectionList2.
Obsolete. Superseded by [ISelectionMgr::ResumeSelectionList2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ResumeSelectionList() 
```

```

Dim instance As ISelectionMgr
 
instance.ResumeSelectionList()
```

```

void ResumeSelectionList()
```

```

void ResumeSelectionList(); 
```

Remarks

To add objects to a selection list without preselecting the objects in the user interface:

1. Call [ISelectionMgr::SuspendSelectionList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SuspendSelectionList.md) to suspend the current selection list, preserving its contents and starting a new selection list.
2. To populate a new selection list, call [ISelectionMgr::AddSelectionListObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObject.md) or [ISelectionMgr::AddSelectionListObjects](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.md).  
     
   **NOTE**: To add objects in a [selection set](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.md) in a new selection list, call [ISelectionSet::Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~Select.md).
3. Process the objects in the new selection list.
4. Call ISelectionMgr::ResumeSelectionList to reinstate the suspended selection list.

To programmatically preselect objects in the user interface and add them to a selection list, use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

Example

[Get Objects in Selection List (C#)](Get_Objects_in_Selection_Set_Example_CSharp.htm)  
[Get Objects in Selection List (VB.NET)](Get_Objects_in_Selection_Set_Example_VBNET.htm)  
[Get Objects in Selection List (VBA)](Get_Objects_in_Selection_Set_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)
