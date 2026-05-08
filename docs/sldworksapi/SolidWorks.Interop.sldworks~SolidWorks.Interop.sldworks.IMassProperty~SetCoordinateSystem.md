# SetCoordinateSystem Method (IMassProperty)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetCoordinateSystem`

Sets the coordinate system to use when calculating mass properties for this model.
Sets the coordinate system to use when calculating mass properties for this model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetCoordinateSystem( _
   ByVal Coords As MathTransform _
) As System.Boolean
```

```

Dim instance As IMassProperty
Dim Coords As MathTransform
Dim value As System.Boolean
 
value = instance.SetCoordinateSystem(Coords)
```

```

System.bool SetCoordinateSystem( 
   MathTransform Coords
)
```

```

System.bool SetCoordinateSystem( 
   MathTransform^ Coords
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

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.md)  
[IModelDoc2::GetCurrentCoordinateSystemName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetCurrentCoordinateSystemName.md)  
[IModelDoc2::InsertCoordinateSystem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCoordinateSystem.md)  
[IModelDocExtension::GetCoordinateSystemTransformByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCoordinateSystemTransformByName.md)
