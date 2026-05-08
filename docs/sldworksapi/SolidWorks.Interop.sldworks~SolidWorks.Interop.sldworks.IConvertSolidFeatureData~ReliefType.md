# ReliefType Property (IConvertSolidFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~ReliefType`

Gets or sets the bend relief type in this convert solid feature.
Gets or sets the bend relief type in this convert solid feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReliefType As System.Integer
```

```

Dim instance As IConvertSolidFeatureData
Dim value As System.Integer
 
instance.ReliefType = value
 
value = instance.ReliefType
```

```

System.int ReliefType {get; set;}
```

```

property System.int ReliefType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Bend relief type as defined by [swSheetMetalAutoReliefTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSheetMetalAutoReliefTypes_e.html)

Remarks

The setter of this property is valid only if [IConvertSolidFeatureData::OverrideDefaultAutoReliefParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData~OverrideDefaultAutoReliefParameters.md) is true.

Example

See the [IConvertSolidFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConvertSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData.md)  
[IConvertSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConvertSolidFeatureData_members.md)
