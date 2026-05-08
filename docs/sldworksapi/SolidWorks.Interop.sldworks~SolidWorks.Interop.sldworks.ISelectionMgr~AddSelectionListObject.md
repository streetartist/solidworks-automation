# AddSelectionListObject Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObject`

Adds the specified object to the selection list.
Adds the specified object to the selection list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddSelectionListObject( _
   ByVal Object As System.Object, _
   ByVal SelectData As System.Object _
) As System.Boolean
```

```

Dim instance As ISelectionMgr
Dim Object As System.Object
Dim SelectData As System.Object
Dim value As System.Boolean
 
value = instance.AddSelectionListObject(Object, SelectData)
```

```

System.bool AddSelectionListObject( 
   System.object Object,
   System.object SelectData
)
```

```

System.bool AddSelectionListObject( 
   System.Object^ Object,
   System.Object^ SelectData
) 
```

#### Parameters

*Object*
:   Object to add to the selection list (see **Remarks**)

*SelectData*
:   [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md)

#### Return Value

True if successful, false if not

Remarks

Call [ISelectionMgr::CreateSelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~CreateSelectData.md) to specify SelectData.

To add objects to a selection list without pre-selecting the objects in the user interface:

1. Call [ISelectionMgr::SuspendSelectionList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SuspendSelectionList.md) to suspend the current selection list, preserving its contents and starting a new selection list.
2. Call ISelectionMgr::AddSelectionListObject or [ISelectionMgr::AddSelectionListObjects](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObjects.md) to populate the new selection list.
3. Process the objects in the new selection list.
4. Call [ISelectionMgr::ResumeSelectionList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList.md) to reinstate the suspended selection list.

To programmatically pre-select objects in the user interface and add them to a selection list, use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

Example

[Insert Indent Feature (C#)](Insert_Indent_Feature_Example_CSharp.htm)  
[Insert Indent Feature (VB.NET)](Insert_Indent_Feature_Example_VBNET.htm)  
[Insert Indent Feature (VBA)](Insert_Indent_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)  
[ISelectionSetItem::GetCorrespondingItem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem~GetCorrespondingItem.md)
