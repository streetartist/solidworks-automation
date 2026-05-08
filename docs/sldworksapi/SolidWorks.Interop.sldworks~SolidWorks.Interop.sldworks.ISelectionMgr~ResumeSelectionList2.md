# ResumeSelectionList2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList2`

Reinstates the previously suspended selection list.
Reinstates the previously suspended selection list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ResumeSelectionList2( _
   ByVal Append As System.Boolean _
) 
```

```

Dim instance As ISelectionMgr
Dim Append As System.Boolean
 
instance.ResumeSelectionList2(Append)
```

```

void ResumeSelectionList2( 
   System.bool Append
)
```

```

void ResumeSelectionList2( 
   System.bool Append
) 
```

#### Parameters

*Append*
:   True to append the new selection list to the suspended selection list and resume the combined selection list, false to just resume the suspended selection list

Remarks

To add objects to a selection list without pre-selecting the objects in the user interface:

1. Call [ISelectionMgr::SuspendSelectionList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SuspendSelectionList.md) to suspend the current selection list, preserving its contents and starting a new selection list.
2. To populate the new selection list, call [ISelectionMgr::AddSelectionListObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObject.md),  [ISelectionMgr::AddSelectionListObjects](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.md), or [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).  
     
   **NOTE**: To add objects in a [selection set](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet.md) to a new selection list, call [ISelectionSet::Select](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet~Select.md).
3. Process the objects in the new selection list.
4. Call this method to reinstate the suspended selection list, setting Append to true to append the new selection list.

Example

[Add Objects to Selection List (VBA)](Add_Objects_to_Selection_List_Example_VB.htm)  
[Add Objects to Selection List (VB.NET)](Add_Objects_to_Selection_List_Example_VBNET.htm)  
[Add Objects to Selection List (C#)](Add_Objects_to_Selection_List_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)
