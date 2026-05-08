# KFactor Property (IBaseFlangeFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~KFactor`

Gets or sets the K-factor for this base-flange feature.
Gets or sets the K-factor for this base-flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KFactor As System.Double
```

```

Dim instance As IBaseFlangeFeatureData
Dim value As System.Double
 
instance.KFactor = value
 
value = instance.KFactor
```

```

System.double KFactor {get; set;}
```

```

property System.double KFactor {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

K-factor

Example

[Create Base-Flange Feature Using Gauge Table (VBA)](Create_Base-Flange_Feature_Using_Gauge_Table_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)  
[IBaseFlangeFeatureData::OverrideKFactor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~OverrideKFactor.md)  
[IBaseFlangeFeatureData::TableKFactor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~TableKFactor.md)
