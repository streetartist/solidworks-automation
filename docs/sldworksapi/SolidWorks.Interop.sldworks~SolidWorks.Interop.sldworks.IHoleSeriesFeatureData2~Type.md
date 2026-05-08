# Type Property (IHoleSeriesFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~Type`

Gets the type of fastener in the specified part in this hole series.
Gets the type of fastener in the specified part in this hole series.

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

Dim instance As IHoleSeriesFeatureData2
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

Example

See the examples in [IHoleSeriesFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.md)  
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.md)
