# IGetCornerPoints Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~IGetCornerPoints`

Gets the corner points of this reference plane.
Gets the corner points of this reference plane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetCornerPoints() As MathPoint
```

```

Dim instance As IRefPlane
Dim value As MathPoint
 
value = instance.IGetCornerPoints()
```

```

MathPoint IGetCornerPoints()
```

```

MathPoint^ IGetCornerPoints(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of four (4) [IMathpoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) objects

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)  
[IRefPlane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane_members.md)  
[IRefPlane::CornerPoints Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~CornerPoints.md)
