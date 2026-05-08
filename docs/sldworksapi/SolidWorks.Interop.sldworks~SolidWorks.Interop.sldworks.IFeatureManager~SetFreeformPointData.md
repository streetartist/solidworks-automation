# SetFreeformPointData Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetFreeformPointData`

Adds a point to a curve for a Freeform feature.
Adds a point to a curve for a Freeform feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetFreeformPointData( _
   ByVal Direction As System.Short, _
   ByVal CurveParameter As System.Double, _
   ByVal ParameterOnCurve As System.Double, _
   ByVal XOffset As System.Double, _
   ByVal YOffset As System.Double, _
   ByVal ZOffset As System.Double _
) 
```

```

Dim instance As IFeatureManager
Dim Direction As System.Short
Dim CurveParameter As System.Double
Dim ParameterOnCurve As System.Double
Dim XOffset As System.Double
Dim YOffset As System.Double
Dim ZOffset As System.Double
 
instance.SetFreeformPointData(Direction, CurveParameter, ParameterOnCurve, XOffset, YOffset, ZOffset)
```

```

void SetFreeformPointData( 
   System.short Direction,
   System.double CurveParameter,
   System.double ParameterOnCurve,
   System.double XOffset,
   System.double YOffset,
   System.double ZOffset
)
```

```

void SetFreeformPointData( 
   System.short Direction,
   System.double CurveParameter,
   System.double ParameterOnCurve,
   System.double XOffset,
   System.double YOffset,
   System.double ZOffset
) 
```

#### Parameters

*Direction*
:   Direction of the curve; valid values are either 0 or 1

*CurveParameter*
:   Curve where to add the point

*ParameterOnCurve*
:   Where on the curve to add the point

*XOffset*
:   Value by which to offset x (this value is typically 0, which indicates that the point  
    was not modified)

*YOffset*
:   Value by which to offset y (this value is typically 0, which indicates that the point  
    was not modified)

*ZOffset*
:   Value by which to offset z (this value is typically 0, which indicates that the point  
    was not modified)

Remarks

The SOLIDWORKS API Freeform-related methods are intended to journal the actions performed by an interactive user while creating the feature. Because user interaction is required to create a Freeform feature, fully automating the creation of it is not possible using the SOLIDWORKS API.

The typical steps performed by an interactive user to create a Freeform feature are:

1. Select the face to form.
2. Add curves on the selected face. Corresponds to [IFeatureManager::SetFreeformCurveData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetFreeformCurveData.md).
3. Add points on the curves. Corresponds to IFeatureManager::SetFreeformPointData.
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
