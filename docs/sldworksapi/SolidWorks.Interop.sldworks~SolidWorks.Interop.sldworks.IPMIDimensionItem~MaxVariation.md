# MaxVariation Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~MaxVariation`

Gets the maximum variation of tolerance for this PMI dimension item.
Gets the maximum variation of tolerance for this PMI dimension item.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaxVariation As System.Double
```

```

Dim instance As IPMIDimensionItem
Dim value As System.Double
 
instance.MaxVariation = value
 
value = instance.MaxVariation
```

```

System.double MaxVariation {get; set;}
```

```

property System.double MaxVariation {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Maximum variation of tolerance

Remarks

This property is valid only if [IPMIDimensionItem::TolType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~TolType.md) returns [swTolType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html):

- swTolBILAT
- swTolLIMIT
- swTolSYMMETRIC
- swTolFITWITHTOL
- swTolFITTOLONLY

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIDimensionItem Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.md)  
[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.md)  
[IPMIDimensionItem::Unit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~Unit.md)  
[IPMIDimensionItem::TolerancePrecision Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~TolerancePrecision.md)
