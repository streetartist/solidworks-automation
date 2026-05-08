# RandomizeScale Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~RandomizeScale`

Gets or sets whether to randomize the scale when auto hatching this section view.
Gets or sets whether to randomize the scale when auto hatching this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RandomizeScale As System.Boolean
```

```

Dim instance As IDrSection
Dim value As System.Boolean
 
instance.RandomizeScale = value
 
value = instance.RandomizeScale
```

```

System.bool RandomizeScale {get; set;}
```

```

property System.bool RandomizeScale {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to randomize the scale when auto hatching, false to not

Remarks

This property is valid only if [IDrSectionView::GetAutoHatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~GetAutoHatch.md) is true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)  
[IDrSection::ScaleHatchPattern Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ScaleHatchPattern.md)
