# TapDrillDepth Property (IWizardHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~TapDrillDepth`

Gets or sets the Hole Wizard feature tap drill depth.
Gets or sets the Hole Wizard feature tap drill depth.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TapDrillDepth As System.Double
```

```

Dim instance As IWizardHoleFeatureData2
Dim value As System.Double
 
instance.TapDrillDepth = value
 
value = instance.TapDrillDepth
```

```

System.double TapDrillDepth {get; set;}
```

```

property System.double TapDrillDepth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Tap drill depth

Remarks

This property is relevant only for:

- swTapBlind
- swTapBlindCounterSinkTop
- swTapThru
- swTapThruCounterSinkBottom
- swTapThruCounterSinkTop
- swTapThruCounterSinkTopBottom

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See **Create Holes Using Hole Wizard and Sketch Points** examples in [IWizardHoleFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWizardHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2.md)  
[IWizardHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.md)  
[IWizardHoleFeatureData2::TapDrillDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~TapDrillDiameter.md)  
[IWizardHoleFeatureData2::TapType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~TapType.md)  
[IWizardHoleFeatureData2::ThruTapDrillDepth Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThruTapDrillDepth.md)  
[IWizardHoleFeatureData2::ThruTapDrillDiameter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2~ThruTapDrillDiameter.md)
