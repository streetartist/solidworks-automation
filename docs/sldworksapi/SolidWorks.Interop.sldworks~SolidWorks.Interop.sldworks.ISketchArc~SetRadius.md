# SetRadius Method (ISketchArc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~SetRadius`

Sets the radius of the arc.
Sets the radius of the arc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetRadius( _
   ByVal Radius As System.Double _
) As System.Boolean
```

```

Dim instance As ISketchArc
Dim Radius As System.Double
Dim value As System.Boolean
 
value = instance.SetRadius(Radius)
```

```

System.bool SetRadius( 
   System.double Radius
)
```

```

System.bool SetRadius( 
   System.double Radius
) 
```

#### Parameters

*Radius*
:   Radius in meters of the arc

#### Return Value

True if successful, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchArc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc.md)  
[ISketchArc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc_members.md)  
[ISketchArc::GetRadius Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc~GetRadius.md)
