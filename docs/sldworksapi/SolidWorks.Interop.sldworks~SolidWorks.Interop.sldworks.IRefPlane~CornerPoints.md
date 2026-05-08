# CornerPoints Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~CornerPoints`

Gets the corner points of this reference plane.
Gets the corner points of this reference plane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property CornerPoints As System.Object
```

```

Dim instance As IRefPlane
Dim value As System.Object
 
value = instance.CornerPoints
```

```

System.object CornerPoints {get;}
```

```

property System.Object^ CornerPoints {
   System.Object^ get();
}
```

#### Property Value

Array of four (4) [IMathpoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) objects

Example

[Get Corner Points of Reference Plane (VBA)](Get_Corner_Points_of_Reference_Plane_Example_VB.htm)  
[Get Corner Points of Reference Plane (VB.NET)](Get_Corner_Points_of_Reference_Plane_Example_VBNET.htm)  
[Get Corner Points of Reference Plane (C#)](Get_Corner_Points_of_Reference_Plane_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)  
[IRefPlane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane_members.md)  
[IRefPlane::IGetCornerPoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~IGetCornerPoints.md)
