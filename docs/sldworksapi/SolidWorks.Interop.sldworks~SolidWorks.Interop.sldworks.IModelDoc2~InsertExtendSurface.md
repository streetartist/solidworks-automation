# InsertExtendSurface Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertExtendSurface`

Extends a surface along the selected faces or edges.
Extends a surface along the selected faces or edges.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InsertExtendSurface( _
   ByVal ExtendLinear As System.Boolean, _
   ByVal EndCondition As System.Integer, _
   ByVal Distance As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim ExtendLinear As System.Boolean
Dim EndCondition As System.Integer
Dim Distance As System.Double
 
instance.InsertExtendSurface(ExtendLinear, EndCondition, Distance)
```

```

void InsertExtendSurface( 
   System.bool ExtendLinear,
   System.int EndCondition,
   System.double Distance
)
```

```

void InsertExtendSurface( 
   System.bool ExtendLinear,
   System.int EndCondition,
   System.double Distance
) 
```

#### Parameters

*ExtendLinear*
:   True to extend surface linearly, false to extend along the same surface

*EndCondition*
:   - 0 - Extend surface by given distance
    - 1 - Extend surface up to a selected point
    - 2 - Extend surface up to a selected surface

*Distance*
:   Distance to extend surface along

Remarks

The selection list can contain faces or edges from the surface. These selected entities will be extended away from the surface according to the input arguments.

The selected point or surface to which to extend should be in the selection list. If EndCondition is to a selected surface, then currently only faces from solids are supported through the API.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.md)
