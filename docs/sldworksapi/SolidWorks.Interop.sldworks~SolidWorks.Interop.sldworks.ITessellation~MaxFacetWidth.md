# MaxFacetWidth Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MaxFacetWidth`

Gets or sets the maximum width of any side of a facet.
Gets or sets the maximum width of any side of a facet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MaxFacetWidth As System.Double
```

```

Dim instance As ITessellation
Dim value As System.Double
 
instance.MaxFacetWidth = value
 
value = instance.MaxFacetWidth
```

```

System.double MaxFacetWidth {get; set;}
```

```

property System.double MaxFacetWidth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Maximum facet width

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellate::MinFacetWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MinFacetWidth.md)
