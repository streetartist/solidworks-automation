# GetHoleTopMateEntity Method (IHoleSeriesFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetHoleTopMateEntity`

Obsolete. Superseded by IHoleSeriesFeatureData2::GetHoleTopMateEntity.
Obsolete. Superseded by [IHoleSeriesFeatureData2::GetHoleTopMateEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetHoleTopMateEntity.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetHoleTopMateEntity( _
   ByVal HoleInstance As System.Integer, _
   ByVal HoleType As System.Short _
) As System.Object
```

```

Dim instance As IHoleSeriesFeatureData
Dim HoleInstance As System.Integer
Dim HoleType As System.Short
Dim value As System.Object
 
value = instance.GetHoleTopMateEntity(HoleInstance, HoleType)
```

```

System.object GetHoleTopMateEntity( 
   System.int HoleInstance,
   System.short HoleType
)
```

```

System.Object^ GetHoleTopMateEntity( 
   System.int HoleInstance,
   System.short HoleType
) 
```

#### Parameters

*HoleInstance*
:   Index number of the hole whose entity you want

*HoleType*
:   Type of hole as defined by [swWzdHoleTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleTypes_e.html)

#### Return Value

[Entity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) to which the top of the hole is mated

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.md)  
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.md)  
[IHoleSeriesFeatureData::IGetHoleTopMateEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetHoleTopMateEntity.md)  
[IHoleSeriesFeatureData::GetHoleBottomMateEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetHoleBottomMateEntity.md)  
[IHoleSeriesFeatureData::IGetHoleBottomMateEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetHoleBottomMateEntity.md)
