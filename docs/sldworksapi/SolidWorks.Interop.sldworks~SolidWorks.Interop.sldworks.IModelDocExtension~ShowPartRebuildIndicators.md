# ShowPartRebuildIndicators Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ShowPartRebuildIndicators`

Gets or sets whether to display rebuild indicators on parts that have out-of-date frozen features.
Gets or sets whether to display rebuild indicators on parts that have out-of-date frozen features.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowPartRebuildIndicators As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
instance.ShowPartRebuildIndicators = value
 
value = instance.ShowPartRebuildIndicators
```

```

System.bool ShowPartRebuildIndicators {get; set;}
```

```

property System.bool ShowPartRebuildIndicators {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display rebuild indicators, false to not

Example

[Move Freeze Bar (VBA)](Move_Freeze_Bar_Example_VB.htm)  
[Move Freeze Bar (VB.NET)](Move_Freeze_Bar_Example_VBNET.htm)  
[Move Freeze Bar (C#)](Move_Freeze_Bar_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::NeedsRebuild2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild2.md)  
[IFeature::HasFrozenUpdatePending Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~HasFrozenUpdatePending.md)
