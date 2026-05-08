# CreateCustomBendAllowance Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateCustomBendAllowance`

Creates a custom bend allowance to use when creating a sheet metal feature.
Creates a custom bend allowance to use when creating a sheet metal feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateCustomBendAllowance() As CustomBendAllowance
```

```

Dim instance As IFeatureManager
Dim value As CustomBendAllowance
 
value = instance.CreateCustomBendAllowance()
```

```

CustomBendAllowance CreateCustomBendAllowance()
```

```

CustomBendAllowance^ CreateCustomBendAllowance(); 
```

#### Return Value

Pointer to the [ICustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance.md) object

Example

[Insert Sheet Metal Hem (VBA)](Insert_Sheet_Metal_Hem_Example_VB.htm)  
[Insert Sheet Metal Hem (VB.NET)](Insert_Sheet_Metal_Hem_Example_VBNET.htm)  
[Insert Sheet Metal Hem (C#)](Insert_Sheet_Metal_Hem_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[BendsFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~SetCustomBendAllowance.md)  
[IEdgeFlangeFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~SetCustomBendAllowance.md)  
[IFeature::InsertSheetMetalBaseFlange Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalBaseFlange.md)  
[IHemFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData~SetCustomBendAllowance.md)  
[IJogFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~SetCustomBendAllowance.md)  
[IMiterFlangeFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData~SetCustomBendAllowance.md)  
[IOneBendFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData~SetCustomBendAllowance.md)  
[ISheetMetalFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetCustomBendAllowance.md)  
[ISketchBendFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData~SetCustomBendAllowance.md)  
[IFeatureManager::InsertSheetMetalHem2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSheetMetalHem2.md)
