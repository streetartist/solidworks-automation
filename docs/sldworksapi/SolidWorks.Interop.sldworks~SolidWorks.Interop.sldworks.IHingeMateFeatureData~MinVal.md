# MinVal Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~MinVal`

Gets or sets the minimum angular rotation between the two components.
Gets or sets the minimum angular rotation between the two components.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MinVal As System.Double
```

```

Dim instance As IHingeMateFeatureData
Dim value As System.Double
 
instance.MinVal = value
 
value = instance.MinVal
```

```

System.double MinVal {get; set;}
```

```

property System.double MinVal {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Minimum angular rotation in radians

Remarks

This property is valid only if [IHingeMateFeatureData::AngleSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~AngleSelection.md) is set to true.

Example

See the [IHingeMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHingeMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData.md)  
[IHingeMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData_members.md)  
[IHingeMateFeatureData::MaxVal Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~MaxVal.md)  
[IHingeMateFeatureData::Angle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData~Angle.md)
