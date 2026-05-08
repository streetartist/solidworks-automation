# CapPlanar Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~CapPlanar`

Gets or sets whether to close the flat openings of surfaces.
Gets or sets whether to close the flat openings of surfaces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CapPlanar As System.Boolean
```

```

Dim instance As IIntersectFeatureData
Dim value As System.Boolean
 
instance.CapPlanar = value
 
value = instance.CapPlanar
```

```

System.bool CapPlanar {get; set;}
```

```

property System.bool CapPlanar {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to close the flat openings, false to not

Example

See the [IIntersectFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.md)  
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.md)
