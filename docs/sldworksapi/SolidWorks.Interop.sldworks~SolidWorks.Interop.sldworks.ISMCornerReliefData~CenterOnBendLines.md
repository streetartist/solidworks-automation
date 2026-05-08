# CenterOnBendLines Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~CenterOnBendLines`

Gets and sets whether to center this corner relative to the bend lines.
Gets and sets whether to center this corner relative to the bend lines.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CenterOnBendLines As System.Boolean
```

```

Dim instance As ISMCornerReliefData
Dim value As System.Boolean
 
instance.CenterOnBendLines = value
 
value = instance.CenterOnBendLines
```

```

System.bool CenterOnBendLines {get; set;}
```

```

property System.bool CenterOnBendLines {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to center relative to the bend lines, false to not

Remarks

This property is valid only if:

- [ICornerReliefFeatureData::CornerType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~CornerType.md) is set to [swCornerReliefBendType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefBendType_e.html).swCornerReliefBendType\_TwoBend

    - And -

- [ISMCornerReliefData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~ReliefType.md) is set to [swCornerReliefType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html).:
  - swCornerCircularRelief
  - swCornerObroundRelief
  - swCornerRectangularRelief

Example

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.md)  
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.md)
