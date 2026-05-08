# MinFacetWidth Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MinFacetWidth`

Gets or sets the minimum facet width for this tessellation.
Gets or sets the minimum facet width for this tessellation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MinFacetWidth As System.Double
```

```

Dim instance As ITessellation
Dim value As System.Double
 
instance.MinFacetWidth = value
 
value = instance.MinFacetWidth
```

```

System.double MinFacetWidth {get; set;}
```

```

property System.double MinFacetWidth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Minimum tessellation width

Remarks

The default value for the underlying modeler is used when tessellating.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellate::MaxFacetWidth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~MaxFacetWidth.md)
