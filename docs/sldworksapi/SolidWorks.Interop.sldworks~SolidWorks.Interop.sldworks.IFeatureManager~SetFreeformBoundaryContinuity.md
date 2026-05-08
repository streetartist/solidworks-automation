# SetFreeformBoundaryContinuity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetFreeformBoundaryContinuity`

Sets the boundary continuity for this Freeform feature.
Sets the boundary continuity for this Freeform feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetFreeformBoundaryContinuity( _
   ByVal BoundaryIndex As System.Short, _
   ByVal Continuity As System.Short _
) 
```

```

Dim instance As IFeatureManager
Dim BoundaryIndex As System.Short
Dim Continuity As System.Short
 
instance.SetFreeformBoundaryContinuity(BoundaryIndex, Continuity)
```

```

void SetFreeformBoundaryContinuity( 
   System.short BoundaryIndex,
   System.short Continuity
)
```

```

void SetFreeformBoundaryContinuity( 
   System.short BoundaryIndex,
   System.short Continuity
) 
```

#### Parameters

*BoundaryIndex*
:   0-based index of the boundary to modify (i.e., a value ranging from 0 to (Number of face boundaries-1))

*Continuity*
:   - -1 = Movaeable
    - 0 = Contact
    - 1 = Tangenet
    - 2= Curvature

Remarks

The SOLIDWORKS API Freeform-related methods are intended to journal the actions performed by an interactive user while creating the feature. Because user interaction is required to create a Freeform feature, fully automating the creation of it is not possible using the SOLIDWORKS API.

The typical steps performed by an interactive user to create a Freeform feature are:

1. Select the face to form.
2. Add curves on the selected face. Corresponds to [IFeatureManager::SetFreeformCurveData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetFreeformCurveData.md).
3. Add points on the curves. Corresponds to [IFeatureManager::SetFreeformPointData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetFreeformPointData.md).
4. Specify boundary continuity. Corresponds to IFeatureManager::SetFreeformBoundaryContinuity.  
     
   Interactively pull or push the points to change the shape of the selected face.
5. Insert the Freeform feature. Corresponds to this method, [IFeatureManager::InsertFreeform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFreeform2.md).

Record a macro while interactively creating a Freeform feature, then examine the macro to see the order in which the Freeform-related methods are recorded.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
