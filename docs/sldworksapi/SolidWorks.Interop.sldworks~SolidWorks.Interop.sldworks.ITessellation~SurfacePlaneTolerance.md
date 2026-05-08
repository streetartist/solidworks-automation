# SurfacePlaneTolerance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~SurfacePlaneTolerance`

Gets or sets the surface plane tolerance.
Gets or sets the surface plane tolerance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SurfacePlaneTolerance As System.Double
```

```

Dim instance As ITessellation
Dim value As System.Double
 
instance.SurfacePlaneTolerance = value
 
value = instance.SurfacePlaneTolerance
```

```

System.double SurfacePlaneTolerance {get; set;}
```

```

property System.double SurfacePlaneTolerance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Surface plane tolerance

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITessellation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation.md)  
[ITessellation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation_members.md)  
[ITessellate::SurfacePlaneAngleTolerance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITessellation~SurfacePlaneAngleTolerance.md)
