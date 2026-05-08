# GetTessellation Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTessellation`

Gets the ITessellation object.
Gets the [ITessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md) object.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTessellation( _
   ByVal FaceList As System.Object _
) As System.Object
```

```

Dim instance As IBody2
Dim FaceList As System.Object
Dim value As System.Object
 
value = instance.GetTessellation(FaceList)
```

```

System.object GetTessellation( 
   System.object FaceList
)
```

```

System.Object^ GetTessellation( 
   System.Object^ FaceList
) 
```

#### Parameters

*FaceList*
:   Array of faces to tessellate; if this is empty, then SOLIDWORKS will tessellate the body

#### Return Value

Object for the tessellation

Example

[Create and Convert Non-manifold Bodies (C#)](Create_and_Convert_Non-manifold_Bodies_Example_CSharp.htm)  
[Create and Convert Non-manifold Bodies (VB.NET)](Create_and_Convert_Non-manifold_Bodies_Example_VBNET.htm)  
[Create and Convert Non-manifold Bodies (VBA)](Create_and_Convert_Non-manifold_Bodies_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::IGetTessellation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetTessellation.md)
