# D1EndConditionType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~D1EndConditionType`

Gets or sets the Direction 1 end condition type for this base flange feature.
Gets or sets the Direction 1 end condition type for this base flange feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D1EndConditionType As System.Integer
```

```

Dim instance As IBaseFlangeFeatureData
Dim value As System.Integer
 
instance.D1EndConditionType = value
 
value = instance.D1EndConditionType
```

```

System.int D1EndConditionType {get; set;}
```

```

property System.int D1EndConditionType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

End condition type as defined in [swFlangeOffsetTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFlangeOffsetTypes_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.md)  
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.md)
