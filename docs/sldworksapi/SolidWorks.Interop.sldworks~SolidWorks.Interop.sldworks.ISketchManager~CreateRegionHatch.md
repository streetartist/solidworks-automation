# CreateRegionHatch Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateRegionHatch`

Creates an area hatch/fill region hatch using a closed sketch profile.
Creates an area hatch/fill region hatch using a closed sketch profile.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateRegionHatch( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal Angle As System.Double, _
   ByVal Scale As System.Double, _
   ByVal Color As System.Integer, _
   ByVal Hatchname As System.String, _
   ByVal Layername As System.String _
) As SketchHatch
```

```

Dim instance As ISketchManager
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim Angle As System.Double
Dim Scale As System.Double
Dim Color As System.Integer
Dim Hatchname As System.String
Dim Layername As System.String
Dim value As SketchHatch
 
value = instance.CreateRegionHatch(X, Y, Z, Angle, Scale, Color, Hatchname, Layername)
```

```

SketchHatch CreateRegionHatch( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double Angle,
   System.double Scale,
   System.int Color,
   System.string Hatchname,
   System.string Layername
)
```

```

SketchHatch^ CreateRegionHatch( 
   System.double X,
   System.double Y,
   System.double Z,
   System.double Angle,
   System.double Scale,
   System.int Color,
   System.String^ Hatchname,
   System.String^ Layername
) 
```

#### Parameters

*X*
:   X coordinate anywhere within the closed sketch profile

*Y*
:   Y coordinate anywhere within the closed sketch profile

*Z*
:   Z coordinate anywhere within the closed sketch profile

*Angle*
:   Angle of the hatch if the hatch is not solid

*Scale*
:   Scale factor for the hatch if the hatch is not solid

*Color*
:   COLORREF value describing the color used for the hatch

*Hatchname*
:   Type or name of the hatch from the **Sldwks.ptn** file

*Layername*
:   Layer name for the hatch if a drawing document

#### Return Value

[Sketch hatch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.md)

Remarks

This method creates a single area hatch/fill region hatch. All three point coordinates are important. This point is compared to all sketch contours to determine one unique external sketch region that contains the point.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)  
[ISketchManager::CreateBoundaryHatch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateBoundaryHatch.md)  
[IModelDoc2::InsertHatchedFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertHatchedFace.md)
