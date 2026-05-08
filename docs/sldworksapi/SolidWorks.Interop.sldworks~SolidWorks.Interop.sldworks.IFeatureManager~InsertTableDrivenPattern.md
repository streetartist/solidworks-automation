# InsertTableDrivenPattern Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertTableDrivenPattern`

Obsolete. Superseded by IFeatureManager::InsertTableDrivenPattern2.
Obsolete. Superseded by [IFeatureManager::InsertTableDrivenPattern2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertTableDrivenPattern2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertTableDrivenPattern( _
   ByVal FileName As System.String, _
   ByVal PointVar As System.Object, _
   ByVal UseCentrod As System.Boolean, _
   ByVal GeomPatt As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim FileName As System.String
Dim PointVar As System.Object
Dim UseCentrod As System.Boolean
Dim GeomPatt As System.Boolean
Dim value As Feature
 
value = instance.InsertTableDrivenPattern(FileName, PointVar, UseCentrod, GeomPatt)
```

```

Feature InsertTableDrivenPattern( 
   System.string FileName,
   System.object PointVar,
   System.bool UseCentrod,
   System.bool GeomPatt
)
```

```

Feature^ InsertTableDrivenPattern( 
   System.String^ FileName,
   System.Object^ PointVar,
   System.bool UseCentrod,
   System.bool GeomPatt
) 
```

#### Parameters

*FileName*
:   Name of the file that has the coordinates information; can be an empty string (see **Remarks**)

*PointVar*
:   Array of x, y coordinates of the points (see **Remarks**)

*UseCentrod*
:   True to use the centroid of the seed feature, face, or body; false to use another point as the reference point (see **Remarks**)

*GeomPatt*
:   True to pattern the geometry, false to not

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Specify:

- coordinates for the input points in system units in a **.sldptab** or **.txt** file for FileName.  
  - or -
- input points in system units in PointVar. Because each point has two coordinates (x, y), the size of PointVar is (2 x number\_of\_points).

This method requires selecting the input entities using these selection marks:

- 4 = Seed feature
- 16 = Coordinate system
- 32 = Reference point
- 128 = Seed face
- 256 = Seed body

If UseCentrod is false, then you must specify a reference point.

See the SOLIDWORKS Help for more information about table-driven patterns.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[IFeatureManager::IInsertTableDrivenPattern Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertTableDrivenPattern.md)
