# AddSelectionListObjects Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObjects`

Adds the specified objects to the selection list.
Adds the specified objects to the selection list.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddSelectionListObjects( _
   ByVal Objects As System.Object, _
   ByVal SelectData As System.Object _
) As System.Integer
```

```

Dim instance As ISelectionMgr
Dim Objects As System.Object
Dim SelectData As System.Object
Dim value As System.Integer
 
value = instance.AddSelectionListObjects(Objects, SelectData)
```

```

System.int AddSelectionListObjects( 
   System.object Objects,
   System.object SelectData
)
```

```

System.int AddSelectionListObjects( 
   System.Object^ Objects,
   System.Object^ SelectData
) 
```

#### Parameters

*Objects*
:   Array of objects to add to the selection list (see **Remarks**)

*SelectData*
:   [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md)

#### Return Value

Number of objects added to the selection list

Remarks

For VB.NET and C# applications, specify Objects as an array of System.Runtime.InteropServices.DispatchWrappers. See the examples and [IDispatch Object Arrays as Input in .NET](sldworksapiprogguide.chm::/OVERVIEW/IDispatch_Object_Arrays_as_Input_in_.NET.htm) for more information.

Call [ISelectionMgr::CreateSelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~CreateSelectData.md) to specify SelectData.

To add objects to a selection list without preselecting the objects in the user interface:

1. Call [ISelectionMgr::SuspendSelectionList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SuspendSelectionList.md) to suspend the current selection list, preserving its contents and starting a new selection list.
2. Call [ISelectionMgr::AddSelectionListObject](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~AddSelectionListObject.md) or ISelectionMgr::AddSelectionListObjects to populate a new selection list.
3. Process the objects in the new selection list.
4. Call [ISelectionMgr::ResumeSelectionList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ResumeSelectionList.md) to reinstate the suspended selection list.

To programmatically preselect objects in the user interface and add them to a selection list, use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

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
[ISelectionSetItem::GetCorrespondingItem Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem~GetCorrespondingItem.md)
