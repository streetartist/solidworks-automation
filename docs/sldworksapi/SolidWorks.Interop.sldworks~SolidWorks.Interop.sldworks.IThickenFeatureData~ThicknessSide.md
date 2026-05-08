# ThicknessSide Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~ThicknessSide`

Gets or sets which side to apply thickness.
Gets or sets which side to apply thickness.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ThicknessSide As System.Short
```

```

Dim instance As IThickenFeatureData
Dim value As System.Short
 
instance.ThicknessSide = value
 
value = instance.ThicknessSide
```

```

System.short ThicknessSide {get; set;}
```

```

property System.short ThicknessSide {
   System.short get();
   void set (    System.short value);
}
```

#### Property Value

Side thickness type as defined in [swThickenThicknessType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swThickenThicknessType_e.html)

Example

See the [IThickenFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThickenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData.md)  
[IThickenFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData_members.md)  
[IThickenFeatureData::Thickness Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData~Thickness.md)
