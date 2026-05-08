# FastenerSize Property (IWizardHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FastenerSize`

Gets the fastener size for this Wizard Hole feature.
Gets the fastener size for this Wizard Hole feature.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FastenerSize As System.String
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As System.String
 
instance.FastenerSize = value
 
value = instance.FastenerSize
```

```

System.string FastenerSize {get; set;}
```

```

property System.String^ FastenerSize {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Fastener size

Remarks

To set the fastener size for a Hole Wizard feature, use [IWizardHoleFeatureData2::ChangeStandard](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ChangeStandard.md). To modify this property, use [IModeler::CopyWizardHole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~CopyWizardHole.md) or [IModeler::ICopyWizardHole](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICopyWizardHole.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)  
[IWizardHoleFeatureData2::FastenerType2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FastenerType2.md)  
[IWizardHoleFeatureData2::Standard2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Standard2.md)
