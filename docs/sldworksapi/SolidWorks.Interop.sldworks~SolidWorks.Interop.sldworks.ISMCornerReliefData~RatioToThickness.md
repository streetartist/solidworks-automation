# RatioToThickness Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~RatioToThickness`

Gets and sets whether to use a ratio of length/width over sheet metal thickness to cut the bend area so that the body can be folded.
Gets and sets whether to use a ratio of length/width over sheet metal thickness to cut the bend area so that the body can be folded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RatioToThickness As System.Boolean
```

```

Dim instance As ISMCornerReliefData
Dim value As System.Boolean
 
instance.RatioToThickness = value
 
value = instance.RatioToThickness
```

```

System.bool RatioToThickness {get; set;}
```

```

property System.bool RatioToThickness {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use a ratio value to cut the bend area, false to not

Remarks

This property is valid only if [ISMCornerReliefData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~ReliefType.md) is set to [swCornerReliefType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html).:

- swCornerCircularRelief
- swCornerObroundRelief
- swCornerRectangularRelief

| If [ISMCornerReliefData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~ReliefType.md) is set to [swCornerReliefType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html).swCornerRectangularRelief. | Then the calculated ratio(s) is(are)... |
| --- | --- |
| swCornerCircularRelief | slot length / thickness of sheet metal |
| swCornerRectangularRelief | slot length / thickness of sheet metal |
| swCornerObroundRelief | slot length / thickness of sheet metal  - And -  slot width / thickness of sheet metal |

Example

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.md)  
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.md)
