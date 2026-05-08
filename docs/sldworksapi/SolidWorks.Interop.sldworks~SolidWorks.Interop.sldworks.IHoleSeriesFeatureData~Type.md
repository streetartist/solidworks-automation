# Type Property (IHoleSeriesFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Type`

Obsolete. Superseded by IHoleSeriesFeatureData2::Type.
Obsolete. Superseded by [IHoleSeriesFeatureData2::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~Type.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Type( _
   ByVal HoleSeriesWhichPart As System.Integer _
) As System.Integer
```

```

Dim instance As IHoleSeriesFeatureData
Dim HoleSeriesWhichPart As System.Integer
Dim value As System.Integer
 
value = instance.Type(HoleSeriesWhichPart)
```

```

System.int Type( 
   System.int HoleSeriesWhichPart
) {get;}
```

```

property System.int Type {
   System.int get(System.int HoleSeriesWhichPart);
}
```

#### Parameters

*HoleSeriesWhichPart*
:   Which part the hole series passes through as defined by [swHoleSeriesWhichParts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHoleSeriesWhichParts_e.html)

#### Property Value

Type of fastener as defined by [swWzdHoleStandardFastenerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.md)  
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.md)  
[IHoleSeriesFeatureData::FastenerBottomHoleType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerBottomHoleType.md)  
[IHoleSeriesFeatureData::FastenerDefaultUnits Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerDefaultUnits.md)  
[IHoleSeriesFeatureData::FastenerHoleCount Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerHoleCount.md)  
[IHoleSeriesFeatureData::FastenerTopHoleType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~FastenerTopHoleType.md)  
[IHoleSeriesFeatureData::Size Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~Size.md)
