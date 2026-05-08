# GetSelectedFaceCount Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSelectedFaceCount`

Gets the number of selected faces on this body. For use with IBody2::GetProcessedBodyWithSelFace and IBody2::IGetPrcoessedBodyWithSelFace and intended for IGES routines.
Gets the number of selected faces on this body. For use with [IBody2::GetProcessedBodyWithSelFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.md) and [IBody2::IGetPrcoessedBodyWithSelFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.md) and intended for IGES routines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSelectedFaceCount() As System.Integer
```

```

Dim instance As IBody2
Dim value As System.Integer
 
value = instance.GetSelectedFaceCount()
```

```

System.int GetSelectedFaceCount()
```

```

System.int GetSelectedFaceCount(); 
```

#### Return Value

Number of selected faces

Remarks

Do not use this method for general selection handling. If you want to handle items selected by the user or items selected with [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md), use [ISelectionMgr::GetSelectedObjectCount2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectCount2.md).

Example

[Get Selected Faces on Processed Body (C#)](Get_Selected_Faces_on_Process_Body_Example_CSharp.htm)  
[Get Selected Faces on Processed Body (VB.NET)](Get_Selected_Faces_on_Process_Body_Example_VBNET.htm)  
[Get Selected Faces on Processed Body (VBA)](Get_Selected_Faces_on_Process_Body_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::GetFirstSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetFirstSelectedFace.md)  
[IBody2::GetNextSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetNextSelectedFace.md)  
[IBody2::IGetFirstSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetFirstSelectedFace.md)  
[IBody2::IGetNextSelectedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetNextSelectedFace.md)  
[IBody2::IGetSelectedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetSelectedFaces.md)  
[IBody2::GetSelectedFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSelectedFaces.md)
