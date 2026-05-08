# GetArea Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetArea`

Gets the area of this face.
Gets the area of this face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArea() As System.Double
```

```

Dim instance As IFace2
Dim value As System.Double
 
value = instance.GetArea()
```

```

System.double GetArea()
```

```

System.double GetArea(); 
```

#### Return Value

Face area in square meters (see **Remarks**)

Remarks

This method calculates and returns an approximate value. If your application requires a more accurate value for a face area, then use tessellation. See [IBody2::GetTessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetTessellation.md) and [ITessellation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md) for details.

Example

[Find Outside Edges of Face (VBA)](Find_Outside_Edges_of_Face_Example_VB.htm)  
[Sweep Planar Loop Along Vector (VBA)](Sweep_Planar_Loop_Along_Vector_Example_VB.htm)  
[Get Areas of MidSurface Faces (C#)](Get_Areas_of_MidSurface_Faces_Example_CSharp.htm)  
[Get Areas of MidSurface Faces (VB.NET)](Get_Areas_of_MidSurface_FAces_Example_VBNET.htm)  
[Get Areas of MidSurface Faces (VBA)](Get_Areas_of_MidSurface_Faces_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)
