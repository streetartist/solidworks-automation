# SlotLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~SlotLength`

Gets and sets the length of this corner relief slot.
Gets and sets the length of this corner relief slot.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SlotLength As System.Double
```

```

Dim instance As ISMCornerReliefData
Dim value As System.Double
 
instance.SlotLength = value
 
value = instance.SlotLength
```

```

System.double SlotLength {get; set;}
```

```

property System.double SlotLength {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Length

Remarks

This property is valid only if [ISMCornerReliefData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~ReliefType.md) is set to [swCornerReliefType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html).:

- swCornerRectangularRelief
- swCornerObroundRelief

Example

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.md)  
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.md)
