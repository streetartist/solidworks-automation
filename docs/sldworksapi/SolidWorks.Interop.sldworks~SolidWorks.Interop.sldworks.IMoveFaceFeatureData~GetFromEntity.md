# GetFromEntity Method (IMoveFaceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetFromEntity`

Gets the entity from which the face of the Move Face feature is translated.
Gets the entity from which the face of the Move Face feature is translated.

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

Dim instance As IMoveFaceFeatureData
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
:   [Face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), or [surface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) from which the face of the Move Face feature is translated

*Type*
:   Type of end condition as defined in [swEndConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndConditions_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)  
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.md)  
[IMoveFaceFeatureData::SetFromEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetFromEntity.md)  
[IMoveFaceFeatureData::GetEndConditionEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~GetEndConditionEntity.md)  
[IMoveFaceFeatureData::SetEndConditionEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~SetEndConditionEntity.md)  
[IMoveFaceFeatureData::EndCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~EndCondition.md)
