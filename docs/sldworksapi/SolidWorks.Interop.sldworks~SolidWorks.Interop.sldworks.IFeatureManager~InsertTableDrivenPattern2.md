# InsertTableDrivenPattern2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertTableDrivenPattern2`

Obsolete. See IFeatureManager::CreateFeature and the Remarks in ITablePatternFeatureData.
Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) and the Remarks in [ITablePatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertTableDrivenPattern2( _
   ByVal FileName As System.String, _
   ByVal PointVar As System.Object, _
   ByVal UseCentroid As System.Boolean, _
   ByVal GeomPattern As System.Boolean, _
   ByVal PropVisProps As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim FileName As System.String
Dim PointVar As System.Object
Dim UseCentroid As System.Boolean
Dim GeomPattern As System.Boolean
Dim PropVisProps As System.Boolean
Dim value As Feature
 
value = instance.InsertTableDrivenPattern2(FileName, PointVar, UseCentroid, GeomPattern, PropVisProps)
```

```

Feature InsertTableDrivenPattern2( 
   System.string FileName,
   System.object PointVar,
   System.bool UseCentroid,
   System.bool GeomPattern,
   System.bool PropVisProps
)
```

```

Feature^ InsertTableDrivenPattern2( 
   System.String^ FileName,
   System.Object^ PointVar,
   System.bool UseCentroid,
   System.bool GeomPattern,
   System.bool PropVisProps
) 
```

#### Parameters

*FileName*
:   Name of the file that has the coordinates for the table-driven pattern; can be an empty string (see **Remarks**)

*PointVar*
:   Array of x, y coordinates of the points for the table-driven pattern (see **Remarks**)

*UseCentroid*
:   True to use the centroid of the seed feature, face, or body; false to use a different point as the reference point (see **Remarks**)

*GeomPattern*
:   True to pattern the geometry, false to not

*PropVisProps*
:   True to propagate visual properties, false to not

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Specify:

- coordinates for the input points in system units in a **.sldptab** or **.txt** file for FileName.  
  - or -
- input points in system units in PointVar. Because each point has two coordinates (x, y), the size of PointVar is (2 x number\_of\_points).

This method requires selecting the input entities using these selection marks:

| Input entity | Mark |
| --- | --- |
| Seed feature | 4 |
| Coordinate system | 16 |
| Reference point | 32 |
| Seed face | 128 |
| Seed body | 256 |

If UseCentroid is false, then you must specify a reference point.

See the SOLIDWORKS Help for more information about table-driven patterns.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
