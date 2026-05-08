# SetParameters Method (IDetailCircle)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetParameters`

Sets the location and size of this detail circle.
Sets the location and size of this detail circle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetParameters( _
   ByVal XPosition As System.Double, _
   ByVal YPosition As System.Double, _
   ByVal Radius As System.Double _
) As System.Boolean
```

```

Dim instance As IDetailCircle
Dim XPosition As System.Double
Dim YPosition As System.Double
Dim Radius As System.Double
Dim value As System.Boolean
 
value = instance.SetParameters(XPosition, YPosition, Radius)
```

```

System.bool SetParameters( 
   System.double XPosition,
   System.double YPosition,
   System.double Radius
)
```

```

System.bool SetParameters( 
   System.double XPosition,
   System.double YPosition,
   System.double Radius
) 
```

#### Parameters

*XPosition*
:   x location of the detail circle

*YPosition*
:   y location of the detail circle

*Radius*
:   Size of the radius of the detail circle

#### Return Value

True if the detail circle is created at the specified location and at the specified size, false if not

Remarks

Use [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) to update the drawing, including the detail circle.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)
