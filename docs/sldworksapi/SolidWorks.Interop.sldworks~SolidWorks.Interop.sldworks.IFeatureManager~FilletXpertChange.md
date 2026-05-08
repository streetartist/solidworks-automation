# FilletXpertChange Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertChange`

Changes the parameters on the selected filleted faces, regardless of whether the filleted faces were created manually or with FilletXpert, provided that FilletXpert can process them.
Changes the parameters on the selected filleted faces, regardless of whether the filleted faces were created manually or with FilletXpert, provided that FilletXpert can process them.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FilletXpertChange( _
   ByVal Options As System.Integer, _
   ByVal R1 As System.Double, _
   ByVal Ftyp As System.Integer, _
   ByVal OverflowType As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Options As System.Integer
Dim R1 As System.Double
Dim Ftyp As System.Integer
Dim OverflowType As System.Integer
Dim value As Feature
 
value = instance.FilletXpertChange(Options, R1, Ftyp, OverflowType)
```

```

Feature FilletXpertChange( 
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType
)
```

```

Feature^ FilletXpertChange( 
   System.int Options,
   System.double R1,
   System.int Ftyp,
   System.int OverflowType
) 
```

#### Parameters

*Options*
:   Feature fillet option as defined in [swFeatureFilletOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletOptions_e.html)

*R1*
:   Radius for uniform radius edge fillet

*Ftyp*
:   Type of fillet as defined in [swFeatureFilletType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureFilletType_e.html)

*OverflowType*
:   Control of fillet overflowing onto adjacent surfaces as defined in [swFilletOverFlowType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFilletOverFlowType_e.html)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::FeatureFillet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFillet.md)  
[IFeatureManager::FilletXpertRemove Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FilletXpertRemove.md)
