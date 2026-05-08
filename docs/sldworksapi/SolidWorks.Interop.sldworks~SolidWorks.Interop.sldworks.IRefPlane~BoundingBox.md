# BoundingBox Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~BoundingBox`

Gets the bounding box of the reference plane, the top-left and bottom-right points.
Gets the bounding box of the reference plane, the top-left and bottom-right points.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property BoundingBox As System.Object
```

```

Dim instance As IRefPlane
Dim value As System.Object
 
value = instance.BoundingBox
```

```

System.object BoundingBox {get;}
```

```

property System.Object^ BoundingBox {
   System.Object^ get();
}
```

#### Property Value

Array containing bounding box, always two (2) [IMathpoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) objects

Example

[Get Coordinates of the Plane's Bounding Box (C#)](Get_Coordinates_of_the_Plane's_Bounding_Box_Example_CSharp.htm)  
[Get Coordinates of the Plane's Bounding Box (VB.NET)](Get_Coordinates_of_the_Plane's_Bounding_Box_Example_VBNET.htm)  
[Get Coordinates of the Plane's Bounding Box (VBA)](Get_Coordinates_of_the_Plane's_Bounding_Box_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRefPlane Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)  
[IRefPlane Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane_members.md)  
[IRefPlane::IGetBoundingBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane~IGetBoundingBox.md)
