# TryToFormSolid Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~TryToFormSolid`

Gets or sets whether to form a solid.
Gets or sets whether to form a solid.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TryToFormSolid As System.Boolean
```

```

Dim instance As IFillSurfaceFeatureData
Dim value As System.Boolean
 
instance.TryToFormSolid = value
 
value = instance.TryToFormSolid
```

```

System.bool TryToFormSolid {get; set;}
```

```

property System.bool TryToFormSolid {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if trying to form solid, false if not

Remarks

The behavior for this option depends on the boundaries.

- When all the boundaries belong to the same solid body, you can use the surface fill to patch the solid.
- If at least one of the edges is an open sheet edge and you merge results, then the fill knits with the surfaces to which the edges belong. See [IFillSurfaceFeatureData::Merge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~Merge.md) for details about merging results.
- If all the boundary entities are open edges, then a solid may be created.

See [IFillSurfaceFeatureData::GetPatchBoundary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundary.md) or [IFillSurfaceFeatureData::IGetPatchBoundary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~IGetPatchBoundary.md) and [IFillSurfaceFeatureData::SetPatchBoundary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~SetPatchBoundary.md) or [IFillSurfaceFeatureData::ISetPatchBoundary](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ISetPatchBoundary.md) for details about boundary entities.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.md)  
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.md)
