# IGetHoleTopMateEntity Method (IHoleSeriesFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~IGetHoleTopMateEntity`

Gets the entity to which the top of the hole is mated in this hole series.
Gets the entity to which the top of the hole is mated in this hole series.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetHoleTopMateEntity( _
   ByVal HoleInstance As System.Integer, _
   ByVal HoleType As System.Short _
) As Entity
```

```

Dim instance As IHoleSeriesFeatureData2
Dim HoleInstance As System.Integer
Dim HoleType As System.Short
Dim value As Entity
 
value = instance.IGetHoleTopMateEntity(HoleInstance, HoleType)
```

```

Entity IGetHoleTopMateEntity( 
   System.int HoleInstance,
   System.short HoleType
)
```

```

Entity^ IGetHoleTopMateEntity( 
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

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.md)  
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.md)  
[IHoleSeriesFeatureData2::GetHoleTopMateEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetHoleTopMateEntity.md)  
[IHoleSeriesFeatureData2::GetHoleBottomMateEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetHoleBottomMateEntity.md)  
[IHoleSeriesFeatureData2::IGetHoleBottomMateEntity Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~IGetHoleBottomMateEntity.md)
