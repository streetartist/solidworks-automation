# HoleCentersVisible Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable~HoleCentersVisible`

Gets or sets whether to show the hole center marks for this hole table.
Gets or sets whether to show the hole center marks for this hole table.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HoleCentersVisible As System.Boolean
```

```

Dim instance As IHoleTable
Dim value As System.Boolean
 
instance.HoleCentersVisible = value
 
value = instance.HoleCentersVisible
```

```

System.bool HoleCentersVisible {get; set;}
```

```

property System.bool HoleCentersVisible {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the hole center marks are visible, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IHoleTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable.md)  
[IHoleTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.md)
