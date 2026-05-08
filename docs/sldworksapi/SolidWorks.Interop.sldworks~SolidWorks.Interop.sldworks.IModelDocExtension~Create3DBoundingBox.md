# Create3DBoundingBox Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Create3DBoundingBox`

Creates a 3D bounding box for a cut list item in a weldment part.
Creates a 3D bounding box for a cut list item in a weldment part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Create3DBoundingBox() 
```

```

Dim instance As IModelDocExtension
 
instance.Create3DBoundingBox()
```

```

void Create3DBoundingBox()
```

```

void Create3DBoundingBox(); 
```

Remarks

After selecting the bounding box, [ISelectionMgr::GetSelectedObjectType3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObjectType3.md) returns [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html).swSelSKETCHES, while [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md) returns an [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) instead of an [ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md).

Example

[Create 3D Bounding Box for Cut List Item (VBA)](Create_3D_Bounding_Box_Example_VB.htm)  
[Create 3D Bounding Box for Cut List Item (VB.NET)](Create_3D_Bounding_Box_Example_VBNET.htm)  
[Create 3D Bounding Box for Cut List Item (C#)](Create_3D_Bounding_Box_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
