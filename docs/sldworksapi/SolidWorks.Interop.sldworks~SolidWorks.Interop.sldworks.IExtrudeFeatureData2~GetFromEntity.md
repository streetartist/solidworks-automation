# GetFromEntity Method (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetFromEntity`

Gets the entity and its type from which the extrusion was created.
Gets the entity and its type from which the extrusion was created.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetFromEntity( _
   ByRef FromEntity As System.Object, _
   ByRef Type As System.Integer _
) 
```

```

Dim instance As IExtrudeFeatureData2
Dim FromEntity As System.Object
Dim Type As System.Integer
 
instance.GetFromEntity(FromEntity, Type)
```

```

void GetFromEntity( 
   out System.object FromEntity,
   out System.int Type
)
```

```

void GetFromEntity( 
   [Out] System.Object^ FromEntity,
   [Out] System.int Type
) 
```

#### Parameters

*FromEntity*
:   Entity from which the extrusion was created:

    - Surface
    - Face
    - Plane
    - Vertex
    - Sketch point

*Type*
:   Type of entity from which to create the extrusion as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)  
[IExtrudeFeatureData2::FromType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FromType.md)  
[IExtrudeFeatureData2::SetFromEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~SetFromEntity.md)
