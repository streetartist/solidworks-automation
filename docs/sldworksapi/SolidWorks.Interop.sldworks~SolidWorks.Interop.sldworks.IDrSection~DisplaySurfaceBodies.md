# DisplaySurfaceBodies Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection~DisplaySurfaceBodies`

Gets or sets whether to display surface bodies in this section view.
Gets or sets whether to display surface bodies in this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplaySurfaceBodies As System.Boolean
```

```

Dim instance As IDrSection
Dim value As System.Boolean
 
instance.DisplaySurfaceBodies = value
 
value = instance.DisplaySurfaceBodies
```

```

System.bool DisplaySurfaceBodies {get; set;}
```

```

property System.bool DisplaySurfaceBodies {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display surface bodies, false to not

Example

See the [IDrSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrSection Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection.md)  
[IDrSection Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.md)
