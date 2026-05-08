# SetProjectionEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~SetProjectionEntity`

Sets the face or plane to which to project the measured distance.
Sets the face or plane to which to project the measured distance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetProjectionEntity( _
   ByVal Entity As System.Object _
) As System.Boolean
```

```

Dim instance As IMeasure
Dim Entity As System.Object
Dim value As System.Boolean
 
value = instance.SetProjectionEntity(Entity)
```

```

System.bool SetProjectionEntity( 
   System.object Entity
)
```

```

System.bool SetProjectionEntity( 
   System.Object^ Entity
) 
```

#### Parameters

*Entity*
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)

#### Return Value

True if Entity is set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMeasure Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure.md)  
[IMeasure Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.md)  
[IMeasure::Projection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~Projection.md)  
[IMeasure::ProjectionOption Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure~ProjectionOption.md)
