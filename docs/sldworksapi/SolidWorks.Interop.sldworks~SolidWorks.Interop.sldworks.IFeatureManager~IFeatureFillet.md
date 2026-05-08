# IFeatureFillet Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IFeatureFillet`

Obsolete. Superseded by IFeatureManager::IFeatureFillet2.
Obsolete. Superseded by [IFeatureManager::IFeatureFillet2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~IFeatureFillet2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IFeatureFillet( _
   ByVal Options As System.Integer, _
   ByVal R1 As System.Double, _
   ByVal Ftyp As System.Integer, _
   ByVal OverflowType As System.Integer, _
   ByVal NRadii As System.Integer, _
   ByRef Radii As System.Double, _
   ByVal SetbackDistCount As System.Integer, _
   ByRef SetBackDistances As System.Double, _
   ByVal PointCount As System.Integer, _
   ByRef PointRadiusArray As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Options As System.Integer
Dim R1 As System.Double
Dim Ftyp As System.Integer
Dim OverflowType As System.Integer
Dim NRadii As System.Integer
Dim Radii As System.Double
Dim SetbackDistCount As System.Integer
Dim SetBackDistances As System.Double
Dim PointCount As System.Integer
Dim PointRadiusArray As System.Double
Dim value As Feature
 
value = instance.IFeatureFillet(Options, R1, Ftyp, OverflowType, NRadii, Radii, SetbackDistCount, SetBackDistances, PointCount, PointRadiusArray)
```

```

Feature IFeatureFillet( 
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType,
   System.int NRadii,
   ref System.double Radii,
   System.int SetbackDistCount,
   ref System.double SetBackDistances,
   System.int PointCount,
   ref System.double PointRadiusArray
)
```

```

Feature^ IFeatureFillet( 
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType,
   System.int NRadii,
   System.double% Radii,
   System.int SetbackDistCount,
   System.double% SetBackDistances,
   System.int PointCount,
   System.double% PointRadiusArray
) 
```

#### Parameters

*Options*
:   Feature fillet options as defined in [swFeatureFilletOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html)

*R1*
:   Radius for uniform radius edge fillet

*Ftyp*
:   Type of fillet as defined in [swFeatureFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html)

*OverflowType*
:   Control of fillet overflowing onto adjacent surfaces as defined in [swFilletOverFlowType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFilletOverFlowType_e.html)

*NRadii*
:   Number of radii for variable radius fillet

*Radii*
:   - in-process, unmanaged C++: Pointer to an array of doubles containing the radii for the variable radius fillet
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*SetbackDistCount*
:   Number of setback distances for the fillet along the edge

*SetBackDistances*
:   - in-process, unmanaged C++: Pointer to an array of doubles containing setback distances for the fillet along the edge of size SetbackDistCount
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*PointCount*
:   Number of control point radii at various points along the length of the edge

*PointRadiusArray*
:   - in-process, unmanaged C++: Pointer to an array of doubles containing the control point radii of size PointCount
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) pointer

Remarks

See the [IFeatureManager::FeatureFillet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet.md) Remarks.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::FilletXpertChange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange.md)  
[IFeatureManager::FilletXpertRemove Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.md)
