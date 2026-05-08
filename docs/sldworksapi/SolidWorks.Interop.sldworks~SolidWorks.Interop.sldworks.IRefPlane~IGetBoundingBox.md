# IGetBoundingBox Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~IGetBoundingBox`

Gets the bounding box of the reference plane, the top-left and bottom-right points.
Gets the bounding box of the reference plane, the top-left and bottom-right points.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetBoundingBox() As MathPoint
```

```

Dim instance As IRefPlane
Dim value As MathPoint
 
value = instance.IGetBoundingBox()
```

```

MathPoint IGetBoundingBox()
```

```

MathPoint^ IGetBoundingBox(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array containing the bounding box, always two (2) [IMathpoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) objects

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)  
[IRefPlane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane_members.md)  
[IRefPlane::BoundingBox Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~BoundingBox.md)
