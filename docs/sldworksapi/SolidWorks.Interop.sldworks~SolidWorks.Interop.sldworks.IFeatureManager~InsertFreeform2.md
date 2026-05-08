# InsertFreeform2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFreeform2`

Inserts a Freeform feature.
Inserts a Freeform feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertFreeform2( _
   ByVal Nsided As System.Boolean, _
   ByVal Symmetric0 As System.Boolean, _
   ByVal Symmetric1 As System.Boolean, _
   ByVal Angle As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Nsided As System.Boolean
Dim Symmetric0 As System.Boolean
Dim Symmetric1 As System.Boolean
Dim Angle As System.Double
Dim value As Feature
 
value = instance.InsertFreeform2(Nsided, Symmetric0, Symmetric1, Angle)
```

```

Feature InsertFreeform2( 
   System.bool Nsided,
   System.bool Symmetric0,
   System.bool Symmetric1,
   System.double Angle
)
```

```

Feature^ InsertFreeform2( 
   System.bool Nsided,
   System.bool Symmetric0,
   System.bool Symmetric1,
   System.double Angle
) 
```

#### Parameters

*Nsided*
:   True to use the new Freeform algorithm, false to use the old one

    **NOTE:** Must be true for faces with three sides or more than four sides, or to enable rotation of UV lines

*Symmetric0*
:   True if symmetry is on in Direction 0, false if not

*Symmetric1*
:   True if symmetry is on in Direction 1, false if not

*Angle*
:   Value by which to rotate the U,V lines (in radians)

#### Return Value

[Freeform feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

The SOLIDWORKS API Freeform-related methods are intended to journal the actions performed by an interactive user while creating the feature. Because user interaction is required to create a Freeform feature, fully automating the creation of it is not possible using the SOLIDWORKS API.

The typical steps performed by an interactive user to create a Freeform feature are:

1. Select the face to form.
2. Add curves on the selected face. Corresponds to [IFeatureManager::SetFreeformCurveData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetFreeformCurveData.md).
3. Add points on the curves. Corresponds to [IFeatureManager::SetFreeformPointData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetFreeformPointData.md).
4. Specify boundary continuity. Corresponds to [IFeatureManager::SetFreeformBoundaryContinuity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetFreeformBoundaryContinuity.md).  
     
   Interactively pull or push the points to change the shape of the selected face.
5. Insert the Freeform feature. Corresponds to this method, IFeatureManager::InsertFreeform2.

Record a macro while interactively creating a Freeform feature, then examine the macro to see the order in which the Freeform-related methods are recorded.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
