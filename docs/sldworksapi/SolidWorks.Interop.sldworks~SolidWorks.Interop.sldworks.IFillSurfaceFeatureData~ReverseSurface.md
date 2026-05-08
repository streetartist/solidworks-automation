# ReverseSurface Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ReverseSurface`

Gets or sets direction of the surface patch.
Gets or sets direction of the surface patch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReverseSurface As System.Boolean
```

```

Dim instance As IFillSurfaceFeatureData
Dim value As System.Boolean
 
instance.ReverseSurface = value
 
value = instance.ReverseSurface
```

```

System.bool ReverseSurface {get; set;}
```

```

property System.bool ReverseSurface {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True reverses the direction of the surface patch, false does not

Remarks

This property is dynamic and is only available when:

- All boundary curves are coplanar
- No constraint points exist
- No interior constraints
- Fill surface is nonplanar

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.md)  
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.md)
