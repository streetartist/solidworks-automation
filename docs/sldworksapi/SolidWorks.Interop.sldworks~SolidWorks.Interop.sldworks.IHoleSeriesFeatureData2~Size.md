# Size Property (IHoleSeriesFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~Size`

Gets the fastener size in the specified part in this hole series.
Gets the fastener size in the specified part in this hole series.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Size( _
   ByVal HoleSeriesWhichPart As System.Integer _
) As System.String
```

```

Dim instance As IHoleSeriesFeatureData2
Dim HoleSeriesWhichPart As System.Integer
Dim value As System.String
 
value = instance.Size(HoleSeriesWhichPart)
```

```

System.string Size( 
   System.int HoleSeriesWhichPart
) {get;}
```

```

property System.String^ Size {
   System.String^ get(System.int HoleSeriesWhichPart);
}
```

#### Parameters

*HoleSeriesWhichPart*
:   Which part the hole series passes through as defined by [swHoleSeriesWhichParts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swHoleSeriesWhichParts_e.html)

#### Property Value

Fastener size

Example

See the examples in [IHoleSeriesFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.md)  
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.md)
