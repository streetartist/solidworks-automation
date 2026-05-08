# CreateBoundaryHatch Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateBoundaryHatch`

Creates area hatch/fill boundary hatches using closed sketch profiles.
Creates area hatch/fill boundary hatches using closed sketch profiles.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateBoundaryHatch( _
   ByVal Angle As System.Double, _
   ByVal Scale As System.Double, _
   ByVal Color As System.Integer, _
   ByVal Hatchname As System.String, _
   ByVal Layername As System.String _
) As System.Object
```

```

Dim instance As ISketchManager
Dim Angle As System.Double
Dim Scale As System.Double
Dim Color As System.Integer
Dim Hatchname As System.String
Dim Layername As System.String
Dim value As System.Object
 
value = instance.CreateBoundaryHatch(Angle, Scale, Color, Hatchname, Layername)
```

```

System.object CreateBoundaryHatch( 
   System.double Angle,
   System.double Scale,
   System.int Color,
   System.string Hatchname,
   System.string Layername
)
```

```

System.Object^ CreateBoundaryHatch( 
   System.double Angle,
   System.double Scale,
   System.int Color,
   System.String^ Hatchname,
   System.String^ Layername
) 
```

#### Parameters

*Angle*
:   Angle of the hatch if hatch is not solid

*Scale*
:   Scale factor for the hatch if hatch is not solid

*Color*
:   COLORREF value describing the color used for this hatch

*Hatchname*
:   Type or name of the hatch from the **Sldwks.ptn** file

*Layername*
:   Layer name for the hatch if a drawing document

#### Return Value

Array of [sketch hatches](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)

Remarks

Before calling this method, select the closed sketch profile for the area hatch/fill boundary hatch.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::CreateRegionHatch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateRegionHatch.md)  
[IModelDoc2::InsertHatchedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHatchedFace.md)
