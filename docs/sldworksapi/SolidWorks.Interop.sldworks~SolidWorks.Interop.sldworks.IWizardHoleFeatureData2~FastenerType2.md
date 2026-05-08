# FastenerType2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FastenerType2`

Gets the fastener type for this Wizard Hole feature.
Gets the fastener type for this Wizard Hole feature.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FastenerType2 As System.Integer
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As System.Integer
 
instance.FastenerType2 = value
 
value = instance.FastenerType2
```

```

System.int FastenerType2 {get; set;}
```

```

property System.int FastenerType2 {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Fastener type as defined in [swWzdHoleStandardFastenerTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWzdHoleStandardFastenerTypes_e.html)

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
[IWizardHoleFeatureData2::FastenerSize Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~FastenerSize.md)  
[IWizardHoleFeatureData2::Standard2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~Standard2.md)
