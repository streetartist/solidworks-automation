# HoleFit Property (IWizardHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~HoleFit`

Gets or sets the Hole Wizard feature fit information.
Gets or sets the Hole Wizard feature fit information.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HoleFit As System.Integer
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As System.Integer
 
instance.HoleFit = value
 
value = instance.HoleFit
```

```

System.int HoleFit {get; set;}
```

```

property System.int HoleFit {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Fit information as defined by [swWzdHoleScrewClearanceTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleScrewClearanceTypes_e.html)

Remarks

When this property is changed, the diameter of the Hole Wizard feature is changed as per the database. This property applies to counterbore and countersink Hole Wizard features only.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)
