# ExcludeFasteners Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ExcludeFasteners`

Gets or sets whether to exclude fasteners in the section view.
Gets or sets whether to exclude fasteners in the section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ExcludeFasteners As System.Boolean
```

```

Dim instance As IDrSection
Dim value As System.Boolean
 
instance.ExcludeFasteners = value
 
value = instance.ExcludeFasteners
```

```

System.bool ExcludeFasteners {get; set;}
```

```

property System.bool ExcludeFasteners {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to exclude fasteners, false to include them

Remarks

Call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) after calling this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)
