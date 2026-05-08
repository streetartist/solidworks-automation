# SetCoordinateSystem Method (IMassProperty2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2~SetCoordinateSystem`

Sets the coordinate system to use when calculating mass properties for this model.
Sets the coordinate system to use when calculating mass properties for this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCoordinateSystem( _
   ByVal Coords As System.Object _
) As System.Boolean
```

```

Dim instance As IMassProperty2
Dim Coords As System.Object
Dim value As System.Boolean
 
value = instance.SetCoordinateSystem(Coords)
```

```

System.bool SetCoordinateSystem( 
   System.object Coords
)
```

```

System.bool SetCoordinateSystem( 
   System.Object^ Coords
) 
```

#### Parameters

*Coords*
:   [Math transform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform.md)

#### Return Value

True if the coordinate system is set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2.md)  
[IMassProperty2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.md)
