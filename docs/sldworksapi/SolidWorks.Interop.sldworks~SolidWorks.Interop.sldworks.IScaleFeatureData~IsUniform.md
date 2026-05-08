# IsUniform Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~IsUniform`

Gets or sets uniform scaling for this scale feature.
Gets or sets uniform scaling for this scale feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property IsUniform As System.Boolean
```

```

Dim instance As IScaleFeatureData
Dim value As System.Boolean
 
instance.IsUniform = value
 
value = instance.IsUniform
```

```

System.bool IsUniform {get; set;}
```

```

property System.bool IsUniform {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True for uniform scaling, false for non-uniform scaling

Example

See [IScaleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md)  
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.md)  
[IScaleFeatureData::GetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~GetScale.md)  
[IScaleFeatureData::SetScale Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~SetScale.md)  
[IScaleFeatureData::ScaleUniform Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~ScaleUniform.md)
