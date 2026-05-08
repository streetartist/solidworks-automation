# GetPathAlignmentDirectionVector Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathAlignmentDirectionVector`

Gets the direction vector of the specified type for this sweep feature.
Gets the direction vector of the specified type for this sweep feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPathAlignmentDirectionVector( _
   ByRef Type As System.Integer _
) As System.Object
```

```

Dim instance As ISweepFeatureData
Dim Type As System.Integer
Dim value As System.Object
 
value = instance.GetPathAlignmentDirectionVector(Type)
```

```

System.object GetPathAlignmentDirectionVector( 
   out System.int Type
)
```

```

System.Object^ GetPathAlignmentDirectionVector( 
   [Out] System.int Type
) 
```

#### Parameters

*Type*
:   Type of direction vector as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html):

    - swSelDATAMAXES (axis)
    - swSelDATUMPLANES (plane)
    - swSelEDGES (edge)
    - swSelFACES (face)

#### Return Value

[Plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), [line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md), [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md), [cylinder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md), [axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md), or a pair of [vertices](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) that defines the direction

Remarks

This method is valid only if:

- [ISweepFeatureData:TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.md) is set to [swTwistControlType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html).swTwistControlFollowPath.

     - and -

- [ISweepFeatureData::PathAlignmentType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PathAlignmentType.md) is set to [swTangencyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTangencyType_e.html).swTangencyDirectionVector.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)  
[ISweepFeatureData::SetPathAlignmentDirectionVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetPathAlignmentDirectionVector.md)  
[ISweepFeatureData::PathAlignmentType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PathAlignmentType.md)  
[ISweepFeatureData::Path Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~Path.md)  
[ISweepFeatureData::GetPathType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathType.md)
