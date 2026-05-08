# ScaleX Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleX`

Gets or sets the scaling factor in the X direction when uniform scaling is disabled.
Gets or sets the scaling factor in the X direction when uniform scaling is disabled.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ScaleX As System.Double
```

```

Dim instance As IScaleFeatureData
Dim value As System.Double
 
instance.ScaleX = value
 
value = instance.ScaleX
```

```

System.double ScaleX {get; set;}
```

```

property System.double ScaleX {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

X-direction scale factor

Remarks

|  |  |
| --- | --- |
| **To get or set...** | **Use...** |
| Uniform scaling | [IScaleFeatureData::IsUniform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~IsUniform.md) |
| All scale-related values in the same call | [IScaleFeatureData::GetScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~GetScale.md) or [IScaleFeatureData::SetScale](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~SetScale.md) |

NOTE: To get or set the scaling factor when uniform scaling is enabled, use [IScaleFeatureData::ScaleUniform](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleUniform.md).

Example

See [IScaleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md)  
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.md)  
[IScaleFeatureData::ScaleY Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleY.md)  
[IScaleFeatureData::ScaleZ Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleZ.md)
