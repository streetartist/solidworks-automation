# Position Property (IEdgePoint)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint~Position`

Gets or sets the position of the midpoint on an edge or an endpoint or midpoint on a reference curve.
Gets or sets the position of the midpoint on an [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) or an endpoint or midpoint on a [reference curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Position As System.Double
```

```

Dim instance As IEdgePoint
Dim value As System.Double
 
instance.Position = value
 
value = instance.Position
```

```

System.double Position {get; set;}
```

```

property System.double Position {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0 (start) to 100 (end)

Example

[Create Reference Curve (C#)](Create_Reference_Curve_Example_CSharp.htm)  
[Create Reference Curve (VB.NET)](Create_Reference_Curve_Example_VBNET.htm)  
[Create Reference Curve (VBA)](Create_Reference_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IEdgePoint Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint.md)  
[IEdgePoint Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint_members.md)
