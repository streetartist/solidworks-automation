# IInsertTableDrivenPattern Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IInsertTableDrivenPattern`

Obsolete. Superseded by IFeatureManager::InsertTableDrivenPattern2.
Obsolete. Superseded by [IFeatureManager::InsertTableDrivenPattern2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertTableDrivenPattern2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertTableDrivenPattern( _
   ByVal FileName As System.String, _
   ByVal Count As System.Integer, _
   ByRef PointArr As System.Double, _
   ByVal UseCentrod As System.Boolean, _
   ByVal GeomPatt As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim FileName As System.String
Dim Count As System.Integer
Dim PointArr As System.Double
Dim UseCentrod As System.Boolean
Dim GeomPatt As System.Boolean
Dim value As Feature
 
value = instance.IInsertTableDrivenPattern(FileName, Count, PointArr, UseCentrod, GeomPatt)
```

```

Feature IInsertTableDrivenPattern( 
   System.string FileName,
   System.int Count,
   ref System.double PointArr,
   System.bool UseCentrod,
   System.bool GeomPatt
)
```

```

Feature^ IInsertTableDrivenPattern( 
   System.String^ FileName,
   System.int Count,
   System.double% PointArr,
   System.bool UseCentrod,
   System.bool GeomPatt
) 
```

#### Parameters

*FileName*
:   Name of the file that has the coordinates information; can be an empty string (see **Remarks**)

*Count*
:   Number of points specified

*PointArr*
:   Array of x, y coordinate points (see **Remarks**)

*UseCentrod*
:   True to use the centroid of the seed feature, face, or body; false to use another point as the reference point (see **Remarks**)

*GeomPatt*
:   True to pattern the geometry, false to not

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

You can specify:

- coordinates for the input points in system units in a **.sldptab** or **.txt** file for FileName.  
  - or -
- input points in system units in PointArr. Because each point has two coordinates (x, y), the size of PointArr is (2 x number\_of\_points).

This method requires selecting the input entities using these selection marks:

- 4 = Seed feature
- 16 = Coordinate system
- 32 = Reference point
- 128 = Seed face
- 256 = Seed body

If UseCentrod is false, then you must specify a reference point.

See the SOLIDWORKS Help for more information about table-driven patterns.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[IFeatureManager::InsertTableDrivenPattern Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertTableDrivenPattern.md)
