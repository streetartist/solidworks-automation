# SetFromEntity Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetFromEntity`

Sets the entity from which to create an extrusion.
Sets the entity from which to create an extrusion.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetFromEntity( _
   ByVal FromEntity As System.Object _
) 
```

```

Dim instance As IExtrudeFeatureData2
Dim FromEntity As System.Object
 
instance.SetFromEntity(FromEntity)
```

```

void SetFromEntity( 
   System.object FromEntity
)
```

```

void SetFromEntity( 
   System.Object^ FromEntity
) 
```

#### Parameters

*FromEntity*
:   Entity from which to create the extrusion:  

    - Surface
    - Face
    - Plane
    - Vertex
    - Sketch point

Remarks

You must also set the type of entity using [IExtrudeFeatureData2::FromType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromType.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::GetFromEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetFromEntity.md)
