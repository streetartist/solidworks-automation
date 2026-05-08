# SetFreeformCurveData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetFreeformCurveData`

Adds a curve to the pre-selected face for a Freeform feature.
Adds a curve to the pre-selected face for a Freeform feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetFreeformCurveData( _
   ByVal Direction As System.Short, _
   ByVal CurveParameter As System.Double, _
   ByVal Tangent0X As System.Double, _
   ByVal Tangent0Y As System.Double, _
   ByVal Tangent0Z As System.Double, _
   ByVal Tangent1X As System.Double, _
   ByVal Tangent1Y As System.Double, _
   ByVal Tangent1Z As System.Double _
) 
```

```

Dim instance As IFeatureManager
Dim Direction As System.Short
Dim CurveParameter As System.Double
Dim Tangent0X As System.Double
Dim Tangent0Y As System.Double
Dim Tangent0Z As System.Double
Dim Tangent1X As System.Double
Dim Tangent1Y As System.Double
Dim Tangent1Z As System.Double
 
instance.SetFreeformCurveData(Direction, CurveParameter, Tangent0X, Tangent0Y, Tangent0Z, Tangent1X, Tangent1Y, Tangent1Z)
```

```

void SetFreeformCurveData( 
   System.short Direction,
   System.double CurveParameter,
   System.double Tangent0X,
   System.double Tangent0Y,
   System.double Tangent0Z,
   System.double Tangent1X,
   System.double Tangent1Y,
   System.double Tangent1Z
)
```

```

void SetFreeformCurveData( 
   System.short Direction,
   System.double CurveParameter,
   System.double Tangent0X,
   System.double Tangent0Y,
   System.double Tangent0Z,
   System.double Tangent1X,
   System.double Tangent1Y,
   System.double Tangent1Z
) 
```

#### Parameters

*Direction*
:   Direction of the curve; valid values are either 0 or 1

*CurveParameter*
:   [Where on the face to add the curve](sldworksAPIProgGuide.chm::/Miscellaneous/FreeFormCurves.htm); valid values are between 0 and 1

*Tangent0X*
:   Tangent vector at one end of curve

*Tangent0Y*
:   Tangent vector at one end of curve

*Tangent0Z*
:   Tangent vector at one end of curve

*Tangent1X*
:   Tangent vector at other end of curve

*Tangent1Y*
:   Tangent vector at other end of curve

*Tangent1Z*
:   Tangent vector at other end of curve

Remarks

The SOLIDWORKS API Freeform-related methods are intended to journal the actions performed by an interactive user while creating the feature. Because user interaction is required to create a Freeform feature, fully automating the creation of it is not possible using the SOLIDWORKS API.

The typical steps performed by an interactive user to create a Freeform feature are:

1. Select the face to form.
2. Add curves on the selected face. Corresponds to IFeatureManager::SetFreeformCurveData.
3. Add points on the curves. Corresponds to [IFeatureManager::SetFreeformPointData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetFreeformPointData.md).
4. Specify boundary continuity. Corresponds to [IFeatureManager::SetFreeformBoundaryContinuity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetFreeformBoundaryContinuity.md).  
     
   Interactively pull or push the points to change the shape of the selected face.
5. Insert the Freeform feature. Corresponds to this method, [IFeatureManager::InsertFreeform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFreeform2.md).

Record a macro while interactively creating a Freeform feature, then examine the macro to see the order in which the Freeform-related methods are recorded.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
