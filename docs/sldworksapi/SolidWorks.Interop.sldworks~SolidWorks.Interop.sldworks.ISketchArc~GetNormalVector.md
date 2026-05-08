# GetNormalVector Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~GetNormalVector`

Gets the normal to the arc.
Gets the normal to the arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetNormalVector() As System.Object
```

```

Dim instance As ISketchArc
Dim value As System.Object
 
value = instance.GetNormalVector()
```

```

System.object GetNormalVector()
```

```

System.Object^ GetNormalVector(); 
```

#### Return Value

Array of 3 doubles (x,y,z), which represents the unit vector normal to the arc

Example

See the [ISketchArc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.md) examples.

Example

[Create Imported Surface Body From Sketch (C#)](Create_Imported_Surface_Body_from_Sketch_Example_CSharp.htm)  
[Get All Elements of Sketch (VBA)](Get_All_Elements_of_Sketch_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.md)  
[ISketchArc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc_members.md)  
[ISketchArc::IGetNormalVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~IGetNormalVector.md)
