# OffsetPlanarWireBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~OffsetPlanarWireBody`

Offsets a planar wire body in the normal plane by the specified distance.
Offsets a planar wire body in the normal plane by the specified distance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function OffsetPlanarWireBody( _
   ByVal Distance As System.Double, _
   ByVal Normal As MathVector, _
   ByVal Option As System.Integer _
) As Body2
```

```

Dim instance As IBody2
Dim Distance As System.Double
Dim Normal As MathVector
Dim Option As System.Integer
Dim value As Body2
 
value = instance.OffsetPlanarWireBody(Distance, Normal, Option)
```

```

Body2 OffsetPlanarWireBody( 
   System.double Distance,
   MathVector Normal,
   System.int Option
)
```

```

Body2^ OffsetPlanarWireBody( 
   System.double Distance,
   MathVector^ Normal,
   System.int Option
) 
```

#### Parameters

*Distance*
:   Distance by which to offset the planar wire body

*Normal*
:   Plane normal

*Option*
:   How to fill the gap between edges as defined in [swOffsetPlanarWireBodyOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swOffsetPlanarWireBodyOptions_e.html)

#### Return Value

Pointer to the [IBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) object

Remarks

The offset direction is determined by the direction of the first edge and the normal. For example, imagine that you are standing on the plane with normal pointing upwards and you are looking along the first edge, then the offset is to your right.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
