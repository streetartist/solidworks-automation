# FillVolume Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~FillVolume`

Gets or sets whether to fill a volume with this thicken feature.
Gets or sets whether to fill a volume with this thicken feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FillVolume As System.Boolean
```

```

Dim instance As IThickenFeatureData
Dim value As System.Boolean
 
instance.FillVolume = value
 
value = instance.FillVolume
```

```

System.bool FillVolume {get; set;}
```

```

property System.bool FillVolume {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to fill a volume, false to not

Example

See the [IThickenFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.md)  
[IThickenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData_members.md)
