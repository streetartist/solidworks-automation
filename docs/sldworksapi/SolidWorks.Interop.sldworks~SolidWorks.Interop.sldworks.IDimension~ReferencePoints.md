# ReferencePoints Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReferencePoints`

Gets or sets the reference points for this dimension.
Gets or sets the reference points for this dimension.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferencePoints As System.Object
```

```

Dim instance As IDimension
Dim value As System.Object
 
instance.ReferencePoints = value
 
value = instance.ReferencePoints
```

```

System.object ReferencePoints {get; set;}
```

```

property System.Object^ ReferencePoints {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Reference points (see **Remarks**)

Remarks

The returned objects, the reference points, are actually [IMathPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md) objects.Reference point 1 and reference point 2 are valid for linear dimensions. Reference point 3 is the vertex for angular dimensions. This property does not distinguish between linear or angular dimensions or other types of dimensions. Three reference points are always returned.NOTE: When regenerating a [macro feature](sldworksapiprogguide.chm::/macro_features/Overview_of_Macro_Features.htm), this property gets and sets the reference points of a display dimension ([IDisplayDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) object).  In all other cases, this property gets and sets the reference points of a dimension ([IDimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md) object).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDimension::IGetReferencePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetReferencePoints.md)  
[IDimension::ISetReferencePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetReferencePoints.md)  
[IDimension::GetReferencePointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetReferencePointsCount.md)
