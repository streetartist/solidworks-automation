# InsertSewRefSurface Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSewRefSurface`

Creates a surface by knitting the selected surfaces together.
Creates a surface by knitting the selected surfaces together.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSewRefSurface( _
   ByVal UseGapFilters As System.Boolean, _
   ByVal TryToFormSolid As System.Boolean, _
   ByVal MergeEntities As System.Boolean, _
   ByVal KnitTolerance As System.Double, _
   ByVal MaxValueForGapRange As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim UseGapFilters As System.Boolean
Dim TryToFormSolid As System.Boolean
Dim MergeEntities As System.Boolean
Dim KnitTolerance As System.Double
Dim MaxValueForGapRange As System.Double
Dim value As Feature
 
value = instance.InsertSewRefSurface(UseGapFilters, TryToFormSolid, MergeEntities, KnitTolerance, MaxValueForGapRange)
```

```

Feature InsertSewRefSurface( 
   System.bool UseGapFilters,
   System.bool TryToFormSolid,
   System.bool MergeEntities,
   System.double KnitTolerance,
   System.double MaxValueForGapRange
)
```

```

Feature^ InsertSewRefSurface( 
   System.bool UseGapFilters,
   System.bool TryToFormSolid,
   System.bool MergeEntities,
   System.double KnitTolerance,
   System.double MaxValueForGapRange
) 
```

#### Parameters

*UseGapFilters*
:   True to use gap filters, false to not

*TryToFormSolid*
:   True to form a solid body, false to no

*MergeEntities*
:   True to merge edges and faces by removing redundant vertices and edges, false to not

*KnitTolerance*
:   Knit tolerance (see **Remarks**)

*MaxValueForGapRange*
:   Maximum value of gap range for gap filters

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Make selections using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with a mark number of 1. See the SOLIDWORKS Help for information about what entities are valid for selection.

A knit tolerance's:

- lower limit is 0.0001 mm
- upper limit is 0.1 mm

The knit tolerance value should be in a gap range such that:

(Minimum gap) <= (Knit tolerance) <= MIN(0.1 mm, Maximum gap)

Example

[Create Surface Knit Feature (VB.NET)](Create_Surface_Knit_Feature_Example_VBNET.htm)  
[Create Surface Knit Feature (VBA)](Create_Surface_Knit_Feature_Example_VB6.htm)  
[Create Surface Knit Feature (C#)](Create_Surface_Knit_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.md)
