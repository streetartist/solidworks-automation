# GetEndConditionEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetEndConditionEntity`

Gets the entity to which the Move Face feature is translated.
Gets the entity to which the Move Face feature is translated.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEndConditionEntity() As System.Object
```

```

Dim instance As IMoveFaceFeatureData
Dim value As System.Object
 
value = instance.GetEndConditionEntity()
```

```

System.object GetEndConditionEntity()
```

```

System.Object^ GetEndConditionEntity(); 
```

#### Return Value

[Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md), [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md), or [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) to which the face of the Move Face feature is translated (see **Remarks**)

Remarks

The type of entity depends on the type of [end condition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~EndCondition.md).

| **End condition** | **Type of entity** |
| --- | --- |
| **Up To Vertex** | Vertex |
| **Up To Surface** or **Offset From Surface** | Face, plane, or surface |
| **Up To Body** | Body or surface |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)  
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.md)  
[IMoveFaceFeatureData::SetEndConditionEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetEndConditionEntity.md)  
[IMoveFaceFeatureData::GetFromEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetFromEntity.md)  
[IMoveFaceFeatureData::SetFromEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetFromEntity.md)
