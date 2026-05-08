# Diameter Property (ICosmeticThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~Diameter`

Gets or sets the value of the diameter of the cosmetic thread.
Gets or sets the value of the diameter of the cosmetic thread.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Diameter As System.Double
```

```

Dim instance As ICosmeticThreadFeatureData
Dim value As System.Double
 
instance.Diameter = value
 
value = instance.Diameter
```

```

System.double Diameter {get; set;}
```

```

property System.double Diameter {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Depth of the diameter (see **Remarks**)

Remarks

|  |  |
| --- | --- |
| **If** [**ICosmeticThreadFeatureData::DiameterType**](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~DiameterType.md)**...** | **Then the value of Diameter is the...** |
| swCosmeticThread\_MajorDiameter  - or -  swCosmeticThread\_MinorDiameter | Diameter of the cosmetic thread |
| swCosmeticThread\_ConicalOffset | Offset of the cosmetic thread from the edge of the conical hole |

Example

See the [ICosmeticThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData.md)  
[ICosmeticThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.md)  
[ICosmeticThreadFeatureData::DiameterType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData~DiameterType.md)
