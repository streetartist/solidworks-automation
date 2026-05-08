# CreateSelectData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~CreateSelectData`

Creates a ISelectData object to use as argument with Select methods.
Creates a [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object to use as argument with Select methods.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateSelectData() As SelectData
```

```

Dim instance As ISelectionMgr
Dim value As SelectData
 
value = instance.CreateSelectData()
```

```

SelectData CreateSelectData()
```

```

SelectData^ CreateSelectData(); 
```

#### Return Value

[ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

Example

[Check Interference Using IAssemblyDoc::ToolsCheckInterference2 (VBA)](Check_Interference_using_AssemblyDoc_ToolsCheckInterference2_Example_VB.htm)  
[Create Plane Thru 3 Points In-context (VBA)](Create_Plane_Thru_3_Points_In-context_Example_VB.htm)  
[Get Faces Associated with Feature (VBA)](Get_Faces_Associated_with_Feature_Example_VB.htm)  
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Select Loop of Edges (VBA)](Select_Loop_of_Edges_Example_VB_.htm)  
[Use Safe Entity (VBA)](Use_Safe_Entity_Example_VB.htm)  
[Select Multiple Objects for Selection Boxes (C#)](Select_Multiple_Objects_for_Selection_Boxes_Example_CSharp.htm)  
[Select Multiple Objects for Selection Boxes (VB.NET)](Select_Multiple_Objects_for_Selection_Boxes_Example_VBNET.htm)  
[Select Multiple Objects for Selection Boxes (VBA)](Select_Multiple_Objects_for_Selection_Boxes_Example_VB.htm)  
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)  
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)  
[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)
