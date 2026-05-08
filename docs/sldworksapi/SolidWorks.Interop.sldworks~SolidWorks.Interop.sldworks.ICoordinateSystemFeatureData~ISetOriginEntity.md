# ISetOriginEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~ISetOriginEntity`

Sets the entity for the origin of this coordinate feature data.
Sets the entity for the origin of this coordinate feature data.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetOriginEntity( _
   ByVal Ent As System.Object _
) 
```

```

Dim instance As ICoordinateSystemFeatureData
Dim Ent As System.Object
 
instance.ISetOriginEntity(Ent)
```

```

void ISetOriginEntity( 
   System.object Ent
)
```

```

void ISetOriginEntity( 
   System.Object^ Ent
) 
```

#### Parameters

*Ent*
:   Entity for origin

Remarks

See SOLIDWORKS Help for a list of valid entities.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoordinateSystemFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData.md)  
[ICoordinateSystemFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.md)  
[ICoordinateSystemFeatureData::IGetOriginEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetOriginEntity.md)  
[ICoordinateSystemFeatureData::OriginEntity Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~OriginEntity.md)  
[ICoordinateSystemFeatureData::GetOriginEntityType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~GetOriginEntityType.md)  
[ICoordinateSystemFeatureData::IGetOriginEntityType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData~IGetOriginEntityType.md)
