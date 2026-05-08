# InsertCosmeticWeldBead Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticWeldBead`

Obsolete. Superseded by IFeatureManager::InsertCosmeticWeldBead2.
Obsolete. Superseded by [IFeatureManager::InsertCosmeticWeldBead2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertCosmeticWeldBead2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertCosmeticWeldBead( _
   ByVal WeldSize As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim WeldSize As System.Double
Dim value As Feature
 
value = instance.InsertCosmeticWeldBead(WeldSize)
```

```

Feature InsertCosmeticWeldBead( 
   System.double WeldSize
)
```

```

Feature^ InsertCosmeticWeldBead( 
   System.double WeldSize
) 
```

#### Parameters

*WeldSize*
:   Size of the weld bead

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method, select the contact faces for the weld bead.

Example

[Insert Cosmetic Weld Bead (VBA)](Insert_Cosmetic_Weld_Bead_Example_VB.htm)  
[Insert Cosmetic Weld Bead (VB.NET)](Insert_Cosmetic_Weld_Bead_Example_VBNET.htm)  
[Insert Cosmetic Weld Bead (C#)](Insert_Cosmetic_Weld_Bead_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
