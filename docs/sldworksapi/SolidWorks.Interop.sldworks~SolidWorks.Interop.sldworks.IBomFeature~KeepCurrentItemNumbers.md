# KeepCurrentItemNumbers Property (IBomFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepCurrentItemNumbers`

Gets or sets whether item numbers are kept with their components when reordering rows of a BOM table.
Gets or sets whether item numbers are kept with their components when reordering rows of a BOM table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KeepCurrentItemNumbers As System.Boolean
```

```

Dim instance As IBomFeature
Dim value As System.Boolean
 
instance.KeepCurrentItemNumbers = value
 
value = instance.KeepCurrentItemNumbers
```

```

System.bool KeepCurrentItemNumbers {get; set;}
```

```

property System.bool KeepCurrentItemNumbers {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if item numbers are kept with their components when reordering rows, false if not

Remarks

Rows in a BOM table can be reordered in several different ways. For example, you can interactively reorder the rows manually in the Bill of Materials Properties dialog box and you can programmatically reorder rows using [IBomFeature::FollowAssemblyOrder2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~FollowAssemblyOrder2.md).

Example

See [IBomFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)
