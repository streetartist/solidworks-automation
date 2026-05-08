# ExcludeSliceSectionBodies Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~ExcludeSliceSectionBodies`

Gets or sets whether to exclude slice section bodies in this section view.
Gets or sets whether to exclude slice section bodies in this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ExcludeSliceSectionBodies As System.Boolean
```

```

Dim instance As IDrSection
Dim value As System.Boolean
 
instance.ExcludeSliceSectionBodies = value
 
value = instance.ExcludeSliceSectionBodies
```

```

System.bool ExcludeSliceSectionBodies {get; set;}
```

```

property System.bool ExcludeSliceSectionBodies {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to exclude slice section bodies, false to include them

Example

See the [IDrSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)
